# Captures — System Breakdowns

Visual documentation of the nine pipeline systems. Annotations are embedded directly in-engine or in-DCC — no external post-processing. Code is visible where readable; complex graphs are documented at block level with logic annotations rather than exposed in detail.

---

## 01 — GPS & Terrain (Houdini)

| File | Description |
|------|-------------|
| `01_gps_houdini_mapboxpatchpipeline` | Base pipeline for Mapbox data retrieval — intentionally stripped down for reuse |
| `01_gps_houdini_erosionmix` | Blending two heightfields with independent multi-erosion passes per source |
| `01_gps_houdini_terrace` | Procedural terrace generation on mountain slopes driven by slope angle |
| `01_gps_houdini_cityreproduction` | OpenStreetMap data ingestion — building footprints and road paths from real-world data |
| `01_gps_houdini_buildingprojection` | Building geometry reprojection onto terrain with height delta compensation |

---

## 02 — Dynamic Landscape Brush Projection (UE5)

Plugin used: **Errant** (patched — see [references](../references/README.md))

| File | Description |
|------|-------------|
| `02_brush_projection_errantmove` | Modified plugin internals exposing fixed vs dynamic brush differentiation |
| `02_brush_projection_sequencercall` | Example of a runtime dynamic brush call driven from Sequencer |

---

## 03 — Sky & Atmosphere Preset System (UE5)

Plugin used: **Sky Creator** (patched — see [references](../references/README.md))

| File | Description |
|------|-------------|
| `03_sky_system_cinematiccontroler` | BP_SkyCinematic Blueprint — preset list sequencing and interpolation logic |
| `03_sky_system_customsequencercontrol` | Sequencer-driven sky parameter example: era time variable, custom cloud shadow simulation |

---

## 04 — Auto-Landscape Material Layer System (UE5)

Base shader: **M4 Landscape** (extended — custom logic layered on top, no M4 source exposed)

| File | Description |
|------|-------------|
| `04_autolandscape_masterblend` | Master material overview — M4 base with custom blend logic, no internal M4 nodes visible |
| `04_autolandscape_layersstructure` | Material instance structure showing editable parameter blocks |
| `04_autolandscape_layerblender` | Material function: layer blending logic between two landscape layers |
| `04_autolandscape_noiseblend` | Noise function driving layer boundary variation and dithering |

---

## 05 — Glitter Shader — Sand & Snow (UE5)

| File | Description |
|------|-------------|
| `05_glitter_shader_materialfunction` | Glitter material function — block-level logic annotated, screen-space normal perturbation approach |

---

## 06 — PCG Vegetation & Rock Population (UE5)

| File | Description |
|------|-------------|
| `06_pcg_structure` | PCG graph — block-annotated logic: sampler → exclusion → Z filter → slope check → 3D spatial noise → projection → bounding box update → density → output |

---

## 07 — PBR Pipeline Standardization (UE5)

| File | Description |
|------|-------------|
| `07_pbr_standardization_PBRmaster` | Master PBR shader — global structure overview |
| `07_pbr_standardization_PBRroughnessmicrodetails` | Double roughness layer for specular micro-detail at close range |
| `07_pbr_standardization_colorvariationinjection` | World-scale noise injection for color variation — breaks repetition in forested areas |
| `07_pbr_standardization_windijection` | Wind parameter injection into PBR master for vegetation animation |

---

## 08 — Forest Biome Material Function (UE5)

| File | Description |
|------|-------------|
| `08_biome_function_mainfunction` | Material function overview — biome ID blend system, full graph |
| `08_biome_function_noisescaleopacity` | Localized view: 3D noise driving mesh opacity for biome death simulation |
| `08_biome_function_temporalditherpng` | Localized view: custom temporal dither logic for smooth era transitions |

---

## 09 — Color Pipeline & Real/CG Integration

No captures for this system. The color pipeline spans multiple UE5 subsystems (ACES tone mapping, Color Calibrator, Pixel Inspector, per-scene exposure compensation) and does not produce a single readable graph view. The full approach is documented in the [main README](../README.md#9-color-pipeline--realcg-integration).
