# Glitter & Flake Rendering — Reference Notes

## Weta Digital Research

The glitter shader implemented in TRE draws from published research on stochastic specular rendering for natural surfaces, notably techniques developed at Weta Digital for snow and sand in feature film production.

### Key reference

**"Rendering Glints on High-Resolution Normal-Mapped Specular Surfaces"**  
Chermain et al. — also informed by Weta's practical implementations for Hero snow/sand surfaces.

The core insight: standard microfacet BRDF models integrate over normal distributions and produce smooth specular lobes. At grain scale (sand, snow, glitter), individual facet reflections are visible and produce discrete highlights. Modeling this requires per-pixel stochastic sampling of the normal distribution rather than integrating over it.

### Weta practical approach (as referenced)
- Screen-space stochastic normal perturbation
- Multi-sample specular evaluation per pixel
- View-dependent behavior — highlights shift with camera angle
- Designed to be performant at film resolution; adapted here for real-time UE5 constraints

### TRE adaptation notes
- LOD fade replaced by TSR + DLAA pipeline configuration (see README section 5)
- Separate parameterization for sand vs snow to account for grain size and reflectance differences
- Implemented as a UE5 Material Function for pipeline-wide reuse

### Further reading
- Yan et al., "Rendering Glints on High-Resolution Normal-Mapped Specular Surfaces", SIGGRAPH 2014
- Jakob et al., "A Comprehensive Framework for Rendering Layered Materials", SIGGRAPH 2014
- UE5 Material documentation — Custom node / stochastic sampling patterns
