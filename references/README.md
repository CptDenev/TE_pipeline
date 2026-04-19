# References

Documentation sources, research material, and third-party tools used across the pipeline. Includes both retained approaches and evaluated alternatives — the distinction is noted where relevant.

---

## Plugins (patched & extended)

### Errant Landscape — Dynamic Brush Projection
[errantphoton.com](https://www.errantphoton.com/)

Base plugin for landscape brush projection. Patched to support runtime-dynamic brushes and animated geological transitions — the original handles static projection only, with no runtime evaluation or movement support. See system 02 in the main README for implementation details.

### Sky Creator — Sky & Atmosphere System
[dmkarpukhin.com/sky-creator](https://dmkarpukhin.com/sky-creator/)

Base plugin for sky and atmosphere management. Extended to support multi-sky preset sequencing and era transitions — the original does not handle ordered sky state lists or per-transition interpolation curves out of the box. Semi source-open plugin, modifications made within the existing architecture. See system 03 in the main README.

---

## Shading Research

### Glitter Shader — Weta Digital / Meerkat (retained)
[Meerkat Sample Project — Epic Games Dev Portal](https://dev.epicgames.com/documentation/unreal-engine/meerkat-sample-project-for-unreal-engine)

Reference implementation for the glitter shader approach used in production. Technique developed by Weta Digital for sand surfaces. Retained for its performance profile — compatible with Nanite and TSR/DLAA pipeline-level anti-aliasing without requiring per-shader LOD logic.

### Glitter Shader — Pixar / Piper (evaluated, not retained)
[The Tech of Pixar Part 1: Piper — FXGuide](https://www.fxguide.com/fxfeatured/the-tech-of-pixar-part-1-piper-daring-to-be-different/)

Alternative glitter approach evaluated during R&D. Not retained due to computational cost — too expensive at production scale even with Nanite, and the Weta approach delivered validated visual results at a fraction of the runtime budget.

---

## Color Pipeline

### ACES — Reference Documentation
[CG Cinematography — Chris Brejon](https://chrisbrejon.com/cg-cinematography/chapter-1-5-academy-color-encoding-system-aces/)

Authoritative reference for ACES implementation in CG production. Used as the conceptual foundation for the project-wide color pipeline. Covers tone mapping behavior, dynamic range handling, and practical implementation considerations. See system 09 in the main README.

### OpenColorIO in Unreal Engine
[Color Management with OpenColorIO — Epic Games Dev Portal](https://dev.epicgames.com/documentation/unreal-engine/color-management-with-opencolorio?application_version=4.27)

Official Epic documentation for OCIO integration. Note: documentation targets UE 4.27 — implementation in UE5 follows the same principles with updated interface. Reference for color space configuration and pipeline standardization.

### OCIO Setup in Virtual Production — Disguise
[Unreal OCIO Setup — Disguise](https://help.disguise.one/workflows/renderstream/unreal-engine/unreal-ocio-setup)

Practical OCIO configuration reference from a virtual production context. Used as a cross-reference for real/CG integration calibration, particularly relevant given the production's live-action footage compositing requirements.

---

*All third-party tools and references are cited for documentation purposes. No proprietary code is reproduced in this repository.*
