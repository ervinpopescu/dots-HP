/* center radius (pixels) */
#define C_RADIUS 200
/* center line thickness (pixels) */
#define C_LINE 2.5
/* outline color */
#define OUTLINE #81a1c1
/* Amplify magnitude of the results each bar displays */
#define AMPLIFY 400
/* Angle (in radians) for how much to rotate the visualizer */
#define ROTATE (PI / 2)
/* Whether to switch left/right audio buffers */
#define INVERT 0
/* Whether to fill in the space between the line and inner circle */
#define C_FILL 0
/* Whether to apply a post-processing image smoothing effect
   1 to enable, 0 to disable. Only works with `xroot` transparency,
   and improves performance if disabled. */
#define C_SMOOTH 1

/* Gravity step, overrude frin `smooth_parameters.glsl` */
#request setgravitystep 6.0

/* Smoothing factor, override from `smooth_parameters.glsl` */
#request setsmoothfactor 0.05
