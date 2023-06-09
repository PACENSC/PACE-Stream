#ifdef GL_ES
precision highp float;
#endif

uniform float    u_time;
uniform vec2     u_resolution;
uniform vec2     u_mouse;
uniform vec3     u_camera;

#define PI          3.141592653589
#define TAU         2.0 * PI
#define MAX_STEPS   100 // Mar Raymarching steps
#define MAX_DIST    100. // Max Raymarching distance
#define SURF_DIST   .01 // Surface Distance
 
float GetDist(vec3 p) 
{
  vec4 s = vec4(0, 1, 6, 1); //Sphere xyz is position w is radius
  float sphereDist = length(p - s.xyz) - s.w;
  float planeDist  = p.y;
  float d = min(sphereDist,planeDist);
  return d;
}
 
float RayMarch(vec3 ro, vec3 rd) 
{
  float dO = 0.; //Distane Origin
  for(int i = 0; i < MAX_STEPS; i++)
  {
    vec3 p = ro + rd * dO;
    float ds = GetDist(p); // ds is Distance Scene
    dO += ds;
    if(dO > MAX_DIST || ds < SURF_DIST) 
      break;
  }
  return dO;
}
 
vec3 GetNormal(vec3 p)
{ 
    float d = GetDist(p); // Distance
    vec2 e = vec2(.01, 0); // Epsilon
    vec3 n = d - vec3(
    GetDist(p - e.xyy),
    GetDist(p - e.yxy),
    GetDist(p - e.yyx));
 
    return normalize(n);
}

float GetLight(vec3 p)
{ 
    // Directional light
    vec3 lightPos = vec3(5. * sin(u_time), 5., 5.0 * cos(u_time)); // Light Position
    vec3 l = normalize(lightPos - p); // Light Vector
    vec3 n = GetNormal(p); // Normal Vector
   
    float dif = dot(n, l); // Diffuse light
    dif = clamp(dif, 0., 1.); // Clamp so it doesnt go below 0
   
    // Shadows
    float d = RayMarch(p + n * SURF_DIST * 2., l); 
     
    if(d < length(lightPos - p)) dif *= .1;
 
    return dif;
}
 
void main()
{
    vec2 uv = (gl_FragCoord.xy - .5 * u_resolution.xy) / u_resolution.y;
     
    vec3 ro = vec3(0, 1, 0); // Ray Origin/Camera
    vec3 rd = normalize(vec3(uv.x, uv.y, 1)); // Ray Direction
   
    float d = RayMarch(ro, rd); // Distance
   
    vec3 p = ro + rd * d;
    float dif = GetLight(p); // Diffuse lighting
    d *= .2;
    vec3 color = vec3(dif);
    //color += GetNormal(p);
    //float color = GetLight(p);
 
    // Set the output color
    gl_FragColor = vec4(color,1.0);
}