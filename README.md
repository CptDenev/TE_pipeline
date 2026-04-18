# TE — Procedural Earth Evolution
### Real-Time Pipeline · Unreal Engine 5 · Houdini · Blender

A documentary production pipeline built from scratch in 9 months with a team of 4 — case study of nine interconnected R&D systems.

---

## Overview

TRE is a documentary production depicting the geological evolution of Earth across deep time — from primordial landscapes to contemporary biomes. Scientific plausibility was a hard requirement: environments needed to hold up under expert review without claiming photorealism. The real challenge was building a real-time pipeline that could deliver this level of credibility across radically different geological eras, with a small team, in nine months.

The full pipeline was built around Unreal Engine 5 rather than traditional offline rendering. This decision shaped every technical choice downstream: shader complexity, asset density, memory budgets, and transition systems all had to perform at runtime — no render farm to hide behind.

The R&D work documented here covers nine interconnected systems developed over the course of production.

## Production context

- **Duration:** 9 months, end to end
- **Team:** 4 people — 2 generalist artists, 1 developer, 1 CG Supervisor / TD (myself)
- **My role:** pipeline architecture, R&D lead, base scene authoring, team supervision
- **Constraint:** small team, real-time output, integration with live-action footage
- **Outcome:** the systems below went into final production use — they shipped, they held up, and they were maintainable by the rest of the team

Every decision documented in this repo was made under production constraints, not as pure research. The trade-offs reflect that.

---