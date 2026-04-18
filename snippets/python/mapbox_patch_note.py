# ─────────────────────────────────────────────────────────────
# TRE — Mapbox Lab Node Compatibility Patch
# Houdini 19 → 21
# ─────────────────────────────────────────────────────────────
#
# The Mapbox terrain data node (SideFX Labs) used for GPS
# heightmap ingestion was originally built for Houdini 19.
# Two breaking changes prevented it from running in H21:
#
#   1. API renaming — several internal hou.* calls had been
#      renamed or deprecated between H19 and H21, causing
#      AttributeError on node cook.
#
#   2. Mapbox authentication — the API key system had evolved
#      and the node's request format no longer matched
#      Mapbox's current endpoint authentication scheme,
#      returning 401 errors silently handled as empty geometry.
#
# Rather than switching data source or waiting for an official
# Labs update, the node source was patched directly.
#
# ─── Fixes applied ───────────────────────────────────────────
#
# 1. API renaming
#    Identified deprecated calls by running the node in H21
#    and tracing AttributeError stack — replaced with current
#    H21 equivalents. No logic changes, rename only.
#
# 2. Mapbox authentication
#    Updated request construction to match current Mapbox
#    Raster Tiles API v4 format — moved API key from legacy
#    query param to the current access_token scheme.
#    Validated against Mapbox API docs (2023).
#
# ─── Outcome ─────────────────────────────────────────────────
#
# Patched node runs cleanly in H21, preserves full original
# functionality: coordinate input, zoom level control,
# tile stitching, and height field output.
#
# Patch kept minimal and surgical — only the two breaking
# points were modified to reduce surface area for future
# engine update regressions.
#
# ─── Note ────────────────────────────────────────────────────
#
# Full patched source not published here (SideFX Labs license).
# This file documents the nature and scope of the fix.
# ─────────────────────────────────────────────────────────────
