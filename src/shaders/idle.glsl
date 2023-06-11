#ifdef GL_ES
precision highp float;
#endif

uniform float    u_time;
uniform vec2     u_resolution;
uniform vec2     u_mouse;
uniform vec3     u_camera;

/**
uniform vec3 a;
uniform vec3 b;
uniform vec3 c;
uniform vec3 d;
**/

#define PI  3.141592653589
#define TAU 2.0 * PI

vec3 gradientCol(float t, vec3 a, vec3 b, vec3 c, vec3 d)
{
    return a + b * cos(TAU * (c*t + d));
}

void drawBuzzer()
{
    return;
}

void main()
{
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / u_resolution.y;
    vec2 uv0 = uv;
    uv = fract(uv * 2.0) - 0.5;
    vec3 result = vec3(0.);

    for (float i = 0.0; i < 1.0; i++) 
    {
        float r = length(uv);

        vec3 col = gradientCol (
            length(uv0) + u_time * 0.25,
            vec3(0.5633, 0.7853, 0.2765),
            vec3(0.7853, 0.2765, 0.5623),
            vec3(0.9933, 0.7853, 0.2765),
            vec3(0.1233, 0.7853, 0.9865)
        );

        r = sin(r * 8. + u_time) / 8.;
        r = abs(r);

        r = 0.035 / r;
        result += r * col;

    }
    
    gl_FragColor = vec4(result, 1.0);
}