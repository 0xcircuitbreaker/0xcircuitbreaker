"""Add a daily contribution summary to the generated snake SVG."""
import json
import os
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / 'assets/readme/contribution-snake.svg'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def decorate(calendar):
    days = [day for week in calendar['weeks'] for day in week['contributionDays']]
    if not days:
        raise ValueError('Contribution calendar is empty')
    total = sum(day['contributionCount'] for day in days)
    active = sum(day['contributionCount'] > 0 for day in days)
    busiest = max(day['contributionCount'] for day in days)
    start, end = min(day['date'] for day in days), max(day['date'] for day in days)
    tree = ET.parse(SVG)
    svg = tree.getroot()
    svg.set('viewBox', '-16 -152 880 312')
    svg.set('height', '312')
    svg.set('role', 'img')
    svg.set('aria-labelledby', 'snake-title snake-description')
    header = ET.Element(f'{{{NS}}}g', {'id': 'contribution-summary'})
    ET.SubElement(header, f'{{{NS}}}rect', {
        'x': '-16', 'y': '-152', 'width': '880', 'height': '312',
        'rx': '12', 'fill': '#020403',
    })

    def text(x, y, value, size, color, weight='400'):
        node = ET.SubElement(header, f'{{{NS}}}text', {
            'x': str(x), 'y': str(y), 'fill': color, 'font-size': str(size),
            'font-family': 'Segoe UI, Ubuntu, sans-serif', 'font-weight': weight,
        })
        node.text = value

    text(8, -113, f'{total:,} contributions in the last year', 25, '#39ff88', '600')
    pretty = lambda value: date.fromisoformat(value).strftime('%b %d, %Y')
    text(8, -88, f'{pretty(start)} – {pretty(end)} · Updated daily', 13, '#7a8b80')
    ET.SubElement(header, f'{{{NS}}}path', {
        'd': 'M8 -73 H840', 'stroke': '#173b28', 'stroke-width': '1',
    })
    text(8, -48, f'{total:,} TOTAL CONTRIBUTIONS', 13, '#d8ffe7', '600')
    text(320, -48, f'{active:,} ACTIVE DAYS', 13, '#d8ffe7', '600')
    text(576, -48, f'{busiest:,} ON BUSIEST DAY', 13, '#b7ff3c', '600')
    svg.insert(0, header)
    title = ET.Element(f'{{{NS}}}title', {'id': 'snake-title'})
    title.text = f'{total:,} contributions in the last year'
    description = ET.Element(f'{{{NS}}}desc', {'id': 'snake-description'})
    description.text = f'{start} through {end}. {active} active days; busiest day: {busiest} contributions. Animated contribution snake.'
    svg.insert(0, description)
    svg.insert(0, title)
    tree.write(SVG, encoding='unicode')
    print(f'Contribution summary: {total:,} total, {active} active days, {busiest} busiest day; {start}–{end}')


if __name__ == '__main__':
    query = '''query($login:String!){user(login:$login){contributionsCollection{
      contributionCalendar{weeks{contributionDays{date contributionCount}}}
    }}}'''
    request = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': query, 'variables': {'login': os.environ['GITHUB_REPOSITORY_OWNER']}}).encode(),
        headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'],
                 'Content-Type': 'application/json', 'User-Agent': 'profile-contribution-summary'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get('errors'):
        raise RuntimeError(result['errors'])
    decorate(result['data']['user']['contributionsCollection']['contributionCalendar'])
