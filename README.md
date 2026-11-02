<div align="center">



<a href="https://github.com/0xcircuitbreaker">
  <img src="./assets/readme/profile-hero-ghost-mesh.svg" width="100%" alt="0xcircuitbreaker - Founder and Lead Engineer; signal locked and systems online"/>
</a>

<br/>

<a href="https://daedalusdevelopmentgroup.com"><img src="https://img.shields.io/badge/daedalusdevelopmentgroup.com-39ff88?style=for-the-badge&logo=googlechrome&logoColor=020403" alt="Portfolio"/></a>

<br/><br/>

<p align="center"><sub><code>Building autonomous AI infrastructure, high-performance DeFi,<br/>and privacy-first blockchain protocols from the ground up.</code></sub></p>

<br/>

<a href="#solidus-network--high-performance-multi-chain-perps-exchange"><img src="https://img.shields.io/badge/01-SOLIDUS%20NETWORK-020403?style=for-the-badge&labelColor=39ff88" alt="01"/></a>
<a href="#innova-inn--privacy-first-blockchain-protocol"><img src="https://img.shields.io/badge/02-INNOVA%20%2F%20IDAG-020403?style=for-the-badge&labelColor=39ff88" alt="02"/></a>
<a href="#project-lavalamp--hardware-level-side-channel-mitigation"><img src="https://img.shields.io/badge/03-PROJECT%20LAVALAMP-0d1117?style=for-the-badge&labelColor=ff6b2b" alt="03"/></a>
<a href="#opentine--git-shaped-provenance-for-agent-runs"><img src="https://img.shields.io/badge/04-OPENTINE-020403?style=for-the-badge&labelColor=b7ff3c" alt="04"/></a>

</div>

<br/>

---

<br/>

<div align="center">

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- SOLIDUS NETWORK                                                    -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-39ff88?style=flat-square&labelColor=39ff88" height="12"/>
SOLIDUS NETWORK — High-Performance Multi-Chain Perps Exchange
</h2>

<img src="https://img.shields.io/badge/STATUS-Active%20Development-39ff88?style=for-the-badge&labelColor=020403" alt="Status"/>

</div>

<br/>

**Solidus Network** is an active-development perpetuals exchange targeting a **multi-algorithm, multi-chain DAGKNIGHT architecture**. The design proposes **4 zones per region**, each mapped to a **different mining algorithm and hardware class** — ASIC, GPU, CPU, and mobile — plus a built-in perps core with on-chain order matching. Performance figures below are engineering targets, not deployed benchmarks.

### DAGKNIGHT Zone-Level DAG Architecture

The target design places DAGKNIGHT consensus **at the zone level** where transaction throughput matters, while Region and Prime chains use **entropic block ordering**.

<p align="center">
  <a href="./assets/readme/solidus-network-topology.svg">
    <img src="./assets/readme/solidus-network-topology.svg" width="100%" alt="Solidus Network target architecture with hierarchical topology, proposed zone consensus, hash lanes, and planned perps core"/>
  </a>
</p>

### Multi-Algorithm Zone Architecture — Dedicated Hardware Lanes

Each planned region contains **4 parallel zones**, each mapped to a distinct consensus algorithm. The design gives each hardware class a dedicated lane with separately balanced difficulty, from enterprise ASICs down to mobile devices.

| Zone | Algorithm | Hardware Class | Design Goal |
|:---|:---|:---|:---|
| **Zone 1** | SHA-256 | ASIC miners | Maximum hashrate throughput |
| **Zone 2** | ProgPoW | GPU miners (NVIDIA/AMD) | Memory-hard, ASIC-resistant |
| **Zone 3** | RandomX-S | CPU miners | Modified RandomX — breaks Antminer RandomX ASICs |
| **Zone 4** | Panthera | Mobile devices | Lightweight mobile-optimized algorithm |

### Performance Targets

| Metric | Target |
|:---|:---|
| **Throughput** | Hyperliquid-competitive throughput; benchmark pending |
| **Zone Consensus** | Proposed DAGKNIGHT-based ordering |
| **Region/Prime** | Target entropic block ordering without a DAG |
| **Order Matching** | Target sub-second on-chain execution |
| **Finality** | Target zone-level and cross-region finality model |
| **Architecture** | Quai fork — hierarchical, sharded, merged-mined |

### Planned Perps Core

| Feature | Description |
|:---|:---|
| **On-Chain Order Book** | Fully on-chain limit/market order matching — no off-chain sequencer |
| **Cross-Margin** | Unified margin across positions with portfolio-level risk |
| **Liquidation Engine** | MEV-resistant liquidation with keeper incentives |
| **Funding Rates** | Decentralized oracle-fed funding rate mechanism |
| **Multi-Collateral** | Multiple collateral types with real-time mark pricing |

### Tech Stack

<div align="center">

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![DAGKNIGHT](https://img.shields.io/badge/DAGKNIGHT-0d1117?style=flat-square)
![SHA-256](https://img.shields.io/badge/SHA--256-0d1117?style=flat-square)
![ProgPoW](https://img.shields.io/badge/ProgPoW-0d1117?style=flat-square)
![RandomX-S](https://img.shields.io/badge/RandomX--S-0d1117?style=flat-square)
![Panthera](https://img.shields.io/badge/Panthera-0d1117?style=flat-square)

</div>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- INNOVA + IDAG + INVS                                               -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-39ff88?style=flat-square&labelColor=39ff88" height="12"/>
INNOVA (INN) — Privacy-First Blockchain Protocol
</h2>

<a href="https://innova-foundation.com"><img src="https://img.shields.io/badge/LIVE-innova--foundation.com-39ff88?style=for-the-badge&labelColor=020403" alt="Live"/></a>&nbsp;
<a href="https://github.com/innova-foundation"><img src="https://img.shields.io/badge/GitHub-innova--foundation-39ff88?style=for-the-badge&logo=github&labelColor=020403" alt="Org"/></a>

<br/><br/>

[![Commits](https://img.shields.io/github/commit-activity/y/innova-foundation/innova?style=flat-square&color=39ff88&labelColor=020403&label=Commit%20Activity)](https://github.com/innova-foundation/innova)
[![Last Commit](https://img.shields.io/github/last-commit/innova-foundation/innova?style=flat-square&color=39ff88&labelColor=020403)](https://github.com/innova-foundation/innova)
[![Stars](https://img.shields.io/github/stars/innova-foundation/innova?style=flat-square&color=39ff88&labelColor=020403)](https://github.com/innova-foundation/innova)
[![License](https://img.shields.io/github/license/innova-foundation/innova?style=flat-square&color=39ff88&labelColor=020403)](https://github.com/innova-foundation/innova)

</div>

<br/>

**Innova** is a hybrid PoW/PoS privacy blockchain with **1,500+ commits**, built on the **Tribus** hashing algorithm (three NIST5 algorithms), ~15s block times, and a hardcapped 18M supply. Its protocol combines composable privacy surfaces, a decentralized services layer, and a Collateral Node network.

### Privacy Surfaces & Proof Paths

<p align="center">
  <a href="./assets/readme/innova-privacy-stack.svg">
    <img src="./assets/readme/innova-privacy-stack.svg" width="100%" alt="Innova privacy surfaces for network origin, receiving, alternative membership-proof paths, and confidential values"/>
  </a>
</p>

<sub>¹ Silent Shielding: RPC commands registered (`sp_send`, `sp_getnewaddress`);</sub>

### Protocol Features

<table>
<tr>
<td width="50%" valign="top">

**Privacy & Staking**

| Feature | Description |
|:---|:---|
| **NullStake V1** | Sigma protocol anonymous staking (block 7,325,000) |
| **NullStake V2** | Poseidon2 + BPAC compact proofs with viewing-key auditability (block 7,330,000) |
| **NullStake V3** | Enhanced ZK staking circuits (block 7,335,000) |
| **Stealth Addresses** | One-time destination addresses for every transaction |
| **Native Tor** | Built-in onion routing for network-level privacy |
| **Dynamic Selective Privacy** | 8 configurable privacy modes (IIP-0004) |
| **Ring Signatures** | Transaction path obfuscation |

</td>
<td width="50%" valign="top">

**Decentralized Services**

| Feature | Description |
|:---|:---|
| **Nyx** | Encrypted messaging system — currently live with AES-256-CBC + HMAC-SHA256 via SMSG, Dandelion++ relay, and FCMP++ membership proofs. Planned upgrade to triple-layer encryption: ML-KEM-1024 (post-quantum) + XChaCha20-Poly1305 + AES-256-GCM with group chats (16 participants) and 10 TB file transfers via encrypted Hyperfile/IPFS chunks |
| **IDNS** | Blockchain-native DNS — A, AAAA, NS, PTR, MX, TXT, CNAME records anchored on-chain for decentralized service routing |
| **Proof of Data (PoD)** | On-chain timestamped record anchoring via `proofofdata` / `hyperfilepod` RPC — digital artifact integrity verification |
| **Hyperfile** | IPFS-based anonymous file uploads with on-chain integrity references |

</td>
</tr>
</table>

<details>
<summary><b>Nyx Encryption Stack (Detail)</b></summary>

<br/>

**Live now:**
<p align="center">
  <a href="./assets/readme/nyx-current-live.svg">
    <img src="./assets/readme/nyx-current-live.svg" width="100%" alt="Nyx current live secure messaging stack"/>
  </a>
</p>

**Proposed upgrade (IIP):**
<p align="center">
  <a href="./assets/readme/nyx-planned-triple-encryption.svg">
    <img src="./assets/readme/nyx-planned-triple-encryption.svg" width="100%" alt="Nyx planned post-quantum triple-encryption roadmap"/>
  </a>
</p>

</details>

<details>
<summary><b>Innova Improvement Proposals (IIPs)</b></summary>

<br/>

<p align="center">
  <a href="./assets/readme/innova-iips.svg">
    <img src="./assets/readme/innova-iips.svg" width="100%" alt="Innova Improvement Proposals IIP-0001 through IIP-0010"/>
  </a>
</p>

</details>

<details>
<summary><b>Network Specifications</b></summary>

<br/>

| Parameter | Value |
|:---|:---|
| **Algorithm** | Tribus PoW (3x NIST5) + PoS (6% annual) |
| **Block Time** | ~15 seconds |
| **Total Supply** | 18,000,000 INN |
| **Collateral Nodes** | 25,000 INN collateral, 65% block reward |
| **Confirmations** | 10 required, 75 block maturity |
| **Stake Age** | 10-hour minimum |
| **BIP39 Coin Type** | 116 |
| **Ports** | P2P 14530, RPC 14531, CN 14539 |
| **Atomic Swaps** | BIP65 CLTV |
| **Multi-Sig** | Native support |

</details>

<br/>

### IDAG — Incremental DAG Consensus

> *The first block DAG with DAGKNIGHT adaptive ordering, PoS finality, and full zero-knowledge privacy.*

IDAG is Innova's next-generation consensus — a four-phase migration from linear blockchain to a high-throughput block DAG. First to implement **epoch-anchored FCMP++ membership proofs** in a DAG and **adaptive DAGKNIGHT k inference**.

<p align="center">
  <a href="./assets/readme/idag-consensus-flow.svg">
    <img src="./assets/readme/idag-consensus-flow.svg" width="100%" alt="IDAG consensus flow from GHOSTDAG ordering through DAGKNIGHT adaptation to proof-of-stake finality"/>
  </a>
</p>

| Parameter | Value |
|:---|:---|
| **Block Interval** | ~1 second (post-DAG fork at block 7,950,000) |
| **Block Size** | 300 KB floor – 8 MB ceiling (adaptive median over 1000-block window) |
| **Finality** | `TENTATIVE` (⅓ stake) → `SOFT` (½ stake) → `HARD` (⅔ stake, 3 consecutive epochs) |
| **GHOSTDAG** | Fixed k=18, pre-DAGKNIGHT ordering |
| **DAGKNIGHT** | Adaptive k=3..32 (EMA-inferred, activates at block 8,000,000) |
| **Fork Resolution** | POEM — `GetBlockEntropy()` computes entropy from inverted block hash (staged) |
| **Epoch** | 300 blocks (~5 min), min 2 unique voters for finality |
| **Privacy** | Epoch-anchored FCMP++ membership proofs via dual curve tree (secp256k1 + Ed25519) with deterministic DAG-ordered commits |

<br/>

### INVS — Shielded Asset Protocol

**INVS** is the shielded asset layer within the Innova ecosystem — private value transfer with ZK-proof verification, leveraging Innova's privacy surfaces and IDAG's throughput for confidential transactions.

### Innova Tech Stack

<div align="center">

![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?style=flat-square&logo=gnubash&logoColor=white)
![Bulletproofs](https://img.shields.io/badge/Bulletproofs-0d1117?style=flat-square)
![Lelantus](https://img.shields.io/badge/Lelantus-0d1117?style=flat-square)
![FCMP++](https://img.shields.io/badge/FCMP++-0d1117?style=flat-square)
![Poseidon2](https://img.shields.io/badge/Poseidon2-0d1117?style=flat-square)
![ZK Proofs](https://img.shields.io/badge/ZK--Proofs-0d1117?style=flat-square)
![Tor](https://img.shields.io/badge/Tor-7D4698?style=flat-square&logo=torproject&logoColor=white)
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?style=flat-square&logo=ipfs&logoColor=white)
![GHOSTDAG](https://img.shields.io/badge/GHOSTDAG-0d1117?style=flat-square)
![DAGKNIGHT](https://img.shields.io/badge/DAGKNIGHT-0d1117?style=flat-square)

</div>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- PROJECT LAVALAMP                                                   -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-ff6b2b?style=flat-square&labelColor=ff6b2b" height="12"/>
PROJECT LAVALAMP — Hardware-Level Side-Channel Mitigation
</h2>

<img src="https://img.shields.io/badge/STATUS-Hardware%20Validated-ff6b2b?style=for-the-badge&labelColor=0d1117" alt="Status"/>&nbsp;
<img src="https://img.shields.io/badge/LEAK%20REDUCTION-93%E2%80%9399%25-ff6b2b?style=for-the-badge&labelColor=0d1117" alt="Leak"/>&nbsp;
<img src="https://img.shields.io/badge/ENTROPY-98.4%25-ff6b2b?style=for-the-badge&labelColor=0d1117" alt="Entropy"/>

</div>

<br/>

**Project Lavalamp** is a hardware-software security product that masks the **AMD Zen 5 SMT port contention timing side-channel** — a **27.6% signal leakage** vulnerability that AMD, Google, Microsoft, and NVIDIA all declined to fix. At its core is a proprietary entropy engine that generates high-quality dither patterns to bury timing signals below the detection floor. Validated on live FPGA hardware — **8/8 NIST-class statistical quality tests pass, 98.4% Shannon entropy efficiency**, with integrity sealing across every released bitstream.

### Recent Milestones

- **Hardware validation complete** on the Artix-7 reference platform — full end-to-end signal-masking loop running on live silicon.
- **Shield (software) tier** daemon feature-complete on x86 and ARM Neoverse with 93% leak reduction at ~6% CPU overhead.
- **Lite (USB-FPGA) tier** shipping across 7 Artix-7 boards with 99%+ leak reduction at <1% host overhead.
- **Pro (PCIe) tier** in active development — kernel driver and TLP-inference pipeline under bring-up.
- **Phase 2 porting effort underway** — extending the FPGA build system to 17 boards across 6 vendors.

<p align="center">
  <a href="./assets/readme/lavalamp-architecture.svg">
    <img src="./assets/readme/lavalamp-architecture.svg" alt="Project Lavalamp architecture and deployment tiers"/>
  </a>
</p>

### Three Deployment Tiers

| Tier | Form Factor | Leak Reduction | CPU Overhead |
|:---|:---|:---|:---|
| **Shield** | CPU-only software daemon (x86 / ARM Neoverse) | 93% | 6% |
| **Lite** | USB FPGA bitstream + host daemon — 7+ Artix-7 boards | 99%+ | <1% |
| **Pro** *(in dev)* | PCIe FPGA card + kernel driver + TLP inference | 99%+ | ~0% |

### Universal FPGA Build System

One command per supported board — `vivado -mode batch -source build_board.tcl -tclargs <board>`. Currently shipping on the Artix-7 family; Phase 2 validates across **17 FPGA boards spanning 6 vendors** (AMD/Xilinx, Intel/Altera, Lattice, Gowin, Microchip).

| Vendor | Families | Status |
|:---|:---|:---|
| **AMD / Xilinx** | Artix-7, Kintex-7, Virtex UltraScale+ | 7 boards shipping · Kintex/UltraScale validation in progress |
| **Intel / Altera** | Cyclone V SoC | Planned (Phase 2) |
| **Lattice** | ECP5 | Planned (Phase 2) |
| **Gowin** | GW2A | Planned (Phase 2) |
| **Microchip** | PolarFire SoC | Planned (Phase 2) |

### Vendor Refusal — Why This Product Exists

| Vendor | Tracking ID | Response |
|:---|:---|:---|
| AMD | `AMD-NSACNT3N` | *"Expected Behavior"* |
| Google / Chromium | Issue `475937586` | *"Won't Fix"* |
| Microsoft MSRC | `VULN-171518` | *"Does not meet criteria"* |
| NVIDIA PSIRT | Tracking `5775002` | *"Expected behavior"* |

Disabling SMT mitigates the leak but costs **~50% of compute capacity**. Lavalamp recovers 97% of that capacity while reducing leakage by **93–99%** depending on tier. No other product targets this specific vulnerability at the hardware level.

### Tech Stack

<div align="center">

![Verilog](https://img.shields.io/badge/Verilog-B31E1F?style=flat-square)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-B31E1F?style=flat-square)
![Vivado](https://img.shields.io/badge/Vivado-EE2E24?style=flat-square)
![Xilinx](https://img.shields.io/badge/Xilinx%20Artix--7-EE2E24?style=flat-square)
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Linux Kernel](https://img.shields.io/badge/Linux%20Kernel-FCC624?style=flat-square&logo=linux&logoColor=black)
![PCIe](https://img.shields.io/badge/PCIe%20DMA-0d1117?style=flat-square)
![AES-GCM](https://img.shields.io/badge/AES--GCM-0d1117?style=flat-square)
![Entropy Engine](https://img.shields.io/badge/Proprietary%20Entropy%20Engine-ff6b2b?style=flat-square&labelColor=0d1117)

</div>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- OPENTINE                                                           -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-b7ff3c?style=flat-square&labelColor=b7ff3c" height="12"/>
OpenTine — Git-Shaped Provenance for Agent Runs
</h2>

<p align="center"><strong>Record, verify, fork, compare, attest, and synchronize agent execution history.</strong><br/>
<sub>&le;250-line trusted kernel · Portable v2 artifacts + verified v3 repositories · <strong>Beta v0.5.0</strong> on PyPI</sub></p>

<a href="https://opentine.com"><img src="https://img.shields.io/badge/LIVE-opentine.com-b7ff3c?style=for-the-badge&labelColor=020403" alt="Live"/></a>&nbsp;
<a href="https://github.com/0xcircuitbreaker/opentine"><img src="https://img.shields.io/badge/GitHub-opentine-b7ff3c?style=for-the-badge&logo=github&labelColor=020403" alt="Repo"/></a>&nbsp;
<a href="https://github.com/0xcircuitbreaker/opentine/releases/tag/v0.5.0"><img src="https://img.shields.io/badge/release-v0.5.0-b7ff3c?style=for-the-badge&labelColor=020403" alt="OpenTine v0.5.0 release"/></a>&nbsp;
<a href="https://pypi.org/project/opentine/"><img src="https://img.shields.io/pypi/v/opentine?style=for-the-badge&color=b7ff3c&labelColor=020403" alt="PyPI version"/></a>&nbsp;
<a href="https://github.com/0xcircuitbreaker/opentine/blob/v0.5.0/LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-b7ff3c?style=for-the-badge&labelColor=020403" alt="License"/></a>&nbsp;
<a href="https://pypi.org/project/opentine/"><img src="https://img.shields.io/pypi/pyversions/opentine?style=for-the-badge&color=b7ff3c&labelColor=020403" alt="Python"/></a>&nbsp;
<a href="https://github.com/0xcircuitbreaker/opentine/actions"><img src="https://img.shields.io/github/actions/workflow/status/0xcircuitbreaker/opentine/ci.yml?style=for-the-badge&color=b7ff3c&labelColor=020403" alt="CI"/></a>

</div>

<br/>

A **tine** is the prong of a fork. OpenTine gives agent execution history Git-shaped provenance without requiring a hosted control plane.

OpenTine v0.5.0 keeps two deliberately separate, compatible storage surfaces:

| Surface | Format | Purpose |
|:---|:---|:---|
| **Portable run** | `*.tine` v2 | Save, sign, verify, fork, replay, diff, resume, tag, search, and migrate individual run trees. Readers still load v1 and v2 artifacts. |
| **Verified repository** | `.tine/` v3 | Store typed content-addressed objects, refs/reflogs, attestations, annotations, packs, semantic diffs, causal context, and synchronized remotes. |

### Quickstart

OpenTine v0.5.0 supports **Python 3.11–3.14**. This example uses the optional Anthropic adapter and expects `ANTHROPIC_API_KEY` in the environment.

```bash
pip install "opentine[anthropic]==0.5.0"
```

```python
from opentine import Agent
from opentine.models.anthropic import Anthropic

agent = Agent(model=Anthropic("claude-sonnet-5"))
run = agent.run_sync("Explain the current branch")
run.save("result.tine")
```

```bash
tine show result.tine
tine verify result.tine
tine cost result.tine
```

### v0.5.0 — Ecosystem Release

Released July 31, 2026, v0.5.0 extends the verified run model into the surrounding agent ecosystem while keeping prior stored data readable. [Read the v0.5.0 changelog →](https://github.com/0xcircuitbreaker/opentine/blob/v0.5.0/CHANGELOG.md)

| Area | Current capability |
|:---|:---|
| **OpenTelemetry GenAI** | Imports modern GenAI spans and complete OTLP/JSON documents; exports portable or repository runs back to matching GenAI spans. |
| **Framework interoperability** | Imports LangChain, LlamaIndex, AutoGen, CrewAI, and OpenAI Agents logs; optional `opentine[langchain]` records LangChain/LangGraph runs live. |
| **Verification** | Content-addressed run history, integrity checks, HMAC-SHA256 and Ed25519 signing, typed links, deep `fsck`, and attestation objects. |
| **Usage and billing** | Normalized provider usage, explicit complete/partial/unknown/unmetered billing states, signed pricing catalogs, and strict cost budgets. |
| **Automation** | `tine import`, stable `--json` output, MCP operations, external CLI harness capture, and a bounded self-hosted reference remote. |
| **Compatibility** | Golden-fixture gates verify that artifacts and repositories written by v0.3.0 and v0.4.0 still load under v0.5.0. |

<p align="center">
  <a href="./assets/readme/opentine-run-tree.svg">
    <img src="./assets/readme/opentine-run-tree.svg" alt="OpenTine v0.5.0 run tree and fork diagram"/>
  </a>
</p>

### Fork-and-diff workflow

When a run fails after many steps, branch from the last good point and compare the resulting histories:

```bash
tine show failed_run.tine
tine fork failed_run.tine --from-step 3 --save fixed_run.tine
tine diff failed_run.tine fixed_run.tine
```

### Selected CLI surface

The `tine` CLI ships **27 subcommands** across portable artifacts, interoperability, pricing, verified repositories, and self-hosted synchronization.

```bash
# Portable artifacts
tine run <script.py> --save result.tine
tine show result.tine
tine verify result.tine --json
tine fork result.tine --from-step 3 --save fork.tine
tine replay result.tine --from-step 3 --mode cache --save replay.tine
tine diff result.tine fork.tine

# Verified repository and trace interoperability
tine init .
tine migrate-v3 result.tine --repo . --ref heads/main
tine import trace.json --format otel-json --repo . --ref heads/imported
tine fsck --repo .
```

### Built-in tools and policy boundaries

Tools remain ordinary typed Python callables, but host-owned policy objects control filesystem, network, shell, and Python execution boundaries.

| Capability | Symbols | Default boundary |
|:---|:---|:---|
| **Web** | `web.fetch`, `web.fetch_raw` | Scheme, DNS, redirect, body-size, and timeout checks. |
| **Search** | `search.search` | Bounded Tavily, Exa, Brave, or DuckDuckGo retrieval. |
| **Filesystem** | `fs.read`, `fs.write`, `fs.edit`, `fs.ls` | Scoped roots; writes require an allowed write root. |
| **Execution** | `shell.run`, `python.execute` | Disabled until the embedding host supplies an explicit enabling policy. |

[Read the v0.5.0 security model →](https://github.com/0xcircuitbreaker/opentine/blob/v0.5.0/docs/SECURITY_MODEL.md)

### Model and ecosystem support

| Surface | Coverage |
|:---|:---|
| **Native adapters** | Anthropic, OpenAI Responses API, Google Gemini, and Ollama. |
| **Hosted compatible adapters** | Kimi/Moonshot, DeepSeek, GLM/Z.AI, xAI/Grok, Groq, Qwen, Together, Mistral/Ministral, OpenRouter, and Nous/Hermes. |
| **Local and generic runtimes** | LM Studio, vLLM, Unsloth, llama.cpp, LocalAI, Jan, SGLang, TGI, MLX-LM, NVIDIA NIM, TensorRT-LLM, KoboldCpp, LiteLLM, and exact-base OpenAI-compatible servers. |
| **Trace ecosystems** | OpenTelemetry GenAI, LangChain/LangGraph, LlamaIndex, AutoGen, CrewAI, and OpenAI Agents. |

Unknown model identifiers remain runnable through their supported transport and are reported as **unpriced** rather than receiving a guessed cost.

### Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat-square)
![Anthropic](https://img.shields.io/badge/Anthropic-D97757?style=flat-square&logo=anthropic&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-0d1117?style=flat-square)
![Rich](https://img.shields.io/badge/Rich-0d1117?style=flat-square)
![Verified Provenance](https://img.shields.io/badge/Verified%20Provenance-0d1117?style=flat-square)
![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-b7ff3c?style=flat-square&labelColor=020403)

</div>

<br/>

---

<br/>


<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- FULL TECH STACK                                                    -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-39ff88?style=flat-square&labelColor=39ff88" height="12"/>
Full Tech Stack
</h2>
</div>

<div align="center">

#### Languages

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?style=for-the-badge&logo=gnubash&logoColor=white)

#### Cryptography & Privacy

![Bulletproofs](https://img.shields.io/badge/Bulletproofs-0d1117?style=for-the-badge)
![Lelantus](https://img.shields.io/badge/Lelantus-0d1117?style=for-the-badge)
![FCMP++](https://img.shields.io/badge/FCMP++-0d1117?style=for-the-badge)
![Pedersen](https://img.shields.io/badge/Pedersen%20Commitments-0d1117?style=for-the-badge)
![Poseidon2](https://img.shields.io/badge/Poseidon2-0d1117?style=for-the-badge)
![ML-KEM-1024](https://img.shields.io/badge/ML--KEM--1024%20(PQ%20%E2%80%94%20Planned)-0d1117?style=for-the-badge)
![ZK-Proofs](https://img.shields.io/badge/Zero--Knowledge%20Proofs-0d1117?style=for-the-badge)
![Tor](https://img.shields.io/badge/Tor-7D4698?style=for-the-badge&logo=torproject&logoColor=white)
![Dandelion++](https://img.shields.io/badge/Dandelion++-0d1117?style=for-the-badge)

#### Consensus & Networking

![DAGKNIGHT](https://img.shields.io/badge/DAGKNIGHT-0d1117?style=for-the-badge)
![GHOSTDAG](https://img.shields.io/badge/GHOSTDAG-0d1117?style=for-the-badge)
![Tribus](https://img.shields.io/badge/Tribus%20PoW-0d1117?style=for-the-badge)
![PoS](https://img.shields.io/badge/Proof%20of%20Stake-0d1117?style=for-the-badge)
![SHA-256](https://img.shields.io/badge/SHA--256-0d1117?style=for-the-badge)
![ProgPoW](https://img.shields.io/badge/ProgPoW-0d1117?style=for-the-badge)
![RandomX-S](https://img.shields.io/badge/RandomX--S-0d1117?style=for-the-badge)
![Panthera](https://img.shields.io/badge/Panthera-0d1117?style=for-the-badge)
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?style=for-the-badge&logo=ipfs&logoColor=white)
![P2P](https://img.shields.io/badge/P2P%20Networking-0d1117?style=for-the-badge)

#### Infrastructure

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- GITHUB ANALYTICS                                                   -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-39ff88?style=flat-square&labelColor=39ff88" height="12"/>
GitHub Analytics
</h2>

<img src="https://github-stats-extended.vercel.app/api?username=0xcircuitbreaker&show_icons=true&hide_border=true&bg_color=020403&title_color=39ff88&icon_color=b7ff3c&text_color=7a8b80&ring_color=39ff88&include_all_commits=true" width="49%" alt="GitHub stats"/>
<img src="https://streak-stats.demolab.com/?user=0xcircuitbreaker&hide_border=true&background=020403&ring=39ff88&fire=b7ff3c&currStreakLabel=39ff88&sideLabels=7a8b80&currStreakNum=b7ff3c&sideNums=d8ffe7&dates=7a8b80&stroke=39ff8840" width="49%" alt="Contribution streak"/>

<br/>

<img src="https://github-stats-extended.vercel.app/api/top-langs/?username=0xcircuitbreaker&layout=compact&hide_border=true&bg_color=020403&title_color=39ff88&text_color=7a8b80&langs_count=10" width="49%" alt="Top languages"/>

<br/><br/>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=0xcircuitbreaker&amp;theme=github_dark&amp;name=CB%20Contribution%20History" width="98%" alt="CB contribution history — GitHub contributions over the past year"/>

</div>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- PINNED REPOS                                                       -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<h2>
<img src="https://img.shields.io/badge/●-39ff88?style=flat-square&labelColor=39ff88" height="12"/>
Pinned Repositories
</h2>

</div>

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/innova-foundation/innova">innova-foundation/innova</a></h3>
<p>Privacy-first hybrid PoW/PoS blockchain with collateral nodes, native Tor, selective privacy, and IDAG research.</p>
<p>
<a href="https://github.com/innova-foundation/innova"><img src="https://img.shields.io/github/stars/innova-foundation/innova?style=flat-square&amp;color=39ff88&amp;labelColor=020403" alt="Innova stars"/></a>
<a href="https://github.com/innova-foundation/innova/forks"><img src="https://img.shields.io/github/forks/innova-foundation/innova?style=flat-square&amp;color=39ff88&amp;labelColor=020403" alt="Innova forks"/></a>
<a href="https://github.com/innova-foundation/innova/commits"><img src="https://img.shields.io/github/last-commit/innova-foundation/innova?style=flat-square&amp;color=39ff88&amp;labelColor=020403" alt="Innova last commit"/></a>
</p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/0xcircuitbreaker/opentine">0xcircuitbreaker/opentine</a></h3>
<p>Git for agent runs: content-addressed execution trees that can be forked, replayed, diffed, paused, and resumed.</p>
<p>
<a href="https://pypi.org/project/opentine/"><img src="https://img.shields.io/pypi/v/opentine?style=flat-square&amp;color=b7ff3c&amp;labelColor=020403" alt="OpenTine on PyPI"/></a>
<a href="https://github.com/0xcircuitbreaker/opentine"><img src="https://img.shields.io/github/stars/0xcircuitbreaker/opentine?style=flat-square&amp;color=b7ff3c&amp;labelColor=020403" alt="OpenTine stars"/></a>
<a href="https://github.com/0xcircuitbreaker/opentine/commits"><img src="https://img.shields.io/github/last-commit/0xcircuitbreaker/opentine?style=flat-square&amp;color=b7ff3c&amp;labelColor=020403" alt="OpenTine last commit"/></a>
</p>
</td>
</tr>
</table>

<br/>

---

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- ADDITIONAL ECOSYSTEM                                               -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<details align="center" open>
<summary><h3>Additional Research</h3></summary>

<br/>

**MEV & Ethereum Infrastructure** — Block builder tooling (Rust), P2P mempool crawlers, EVM benchmarking, and DeFi protocol analysis.

**Cryptanalysis & Bitcoin Research** — UTXO analysis, chainstate parsing, vanity address generation, and parallel cryptanalysis tooling.

**Priscus Research** — Applied AI systems research under private development. Public releases will focus on verifiable claims, reproducible evaluation summaries, and externally reviewable findings while keeping proprietary code, architecture details, model weights, datasets, and internal design materials confidential.

**AI/ML** — Autonomous agent architectures, multimodal models, and research aligned with agent-first design philosophy.

</details>

</div>

<br/>

---

<div align="center">

<br/>

<sub>Building autonomous AI infrastructure, high-performance DeFi, and privacy-first blockchain protocols.</sub>

<br/><br/>

<img src="./assets/readme/profile-footer-ghost-mesh.svg" width="100%" alt="Ghost Mesh terminal signal footer"/>

</div>
