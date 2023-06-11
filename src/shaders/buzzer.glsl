#ifdef GL_ES
precision highp float;
#endif

uniform float     u_time;
uniform vec2      u_resolution;
uniform vec2      u_mouse;
uniform vec3      u_camera;

#define PI          3.141592653589
#define TAU         2.0 * PI
#define MAX_STEPS   100 // Mar Raymarching steps
#define MAX_DIST    100. // Max Raymarching distance
#define SURF_DIST   .01 // Surface Distance

mat2 rot(float theta) {
	float s = sin(theta);
	float c = cos(theta);
	return mat2(c, -s, s, c);
}

float opSmoothUnion(float d1, float d2, float k) 
{
	float h = clamp( 0.5 + 0.5*(d2-d1)/k, 0.0, 1.0 );
	return mix( d2,  d1,  h ) - k*h*(1.0-h); 
}

float opSmoothSubtraction(float d1, float d2, float k) 
{
	float h = clamp( 0.5 - 0.5*(d2+d1)/k, 0.0, 1.0 );
	return mix( d2, -d1, h ) + k*h*(1.0-h); }

float opSmoothIntersection(float d1, float d2, float k) 
{
	float h = clamp( 0.5 - 0.5*(d2-d1)/k, 0.0, 1.0 );
	return mix( d2, d1, h ) + k*h*(1.0-h); 
}

float sdSphere(vec3 p, float s)
{
	return length(p) - s;
}

float sdBox(vec3 p, vec3 b)
{
	vec3 q = abs(p) - b;
  	return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0);
}

float sdRoundBox(vec3 p, vec3 b, float r)
{
  	vec3 q = abs(p) - b;
  	return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0) - r;
}

float sdCappedCylinder(vec3 p, float h, float r)
{
  	vec2 d = abs(vec2(length(p.xz), p.y)) - vec2(r, h);
  	return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

float sdTorus(vec3 p, vec2 t)
{
  	vec2 q = vec2(length(p.xz) - t.x, p.y);
  	return length(q) - t.y;
}

float sdVerticalCapsule(vec3 p, float h, float r)
{
  	p.y -= clamp(p.y, 0.0, h);
	return length(p) - r;
}

float drawBuzzerButton(vec3 p, out vec3 col)
{
  	float buzzerRing = sdTorus(p - vec3(0, 0.0, 0), vec2(0.63, 0.10));
  	float buttonDivet = sdSphere(p - vec3(0., 2.5, 0.), 0.87);
	float buzzerButton = sdCappedCylinder(p - vec3(0., 1.5, 0.0), .250, 0.53);	
	// buzz function : + 0.1 * abs(sin(u_time * TAU))
	float d = buzzerButton;
	d = min(d, buzzerButton);
	d = max(d, -buttonDivet);

	col =vec3(0.8, 0.1, 0.1) ;

	return d;
}

float drawBuzzer(vec3 p, bool isRedLed, out vec3 col)
{
  	float buzzerBox =  sdRoundBox(p / vec3(3.118, 1.13, 1.9818), vec3(1, 1, 1), 0.30);
  	float ledHole = sdCappedCylinder(p - vec3(0., 1.5, 1.2), .20, 0.25);
  	float led = sdVerticalCapsule(p - vec3(0., 1.2, 1.2), 0.28, 0.21);
	float buzzerHole = sdCappedCylinder(p - vec3(0., 1.5, 0.0), .67, 0.67);

	float d = buzzerBox;
	d = max(d, -buzzerHole);
  	d = max(d, -ledHole);

	float boxD = d;

  	d = min(d, led);

	vec3 buttonCol;
	float buttonD = min(d, drawBuzzerButton(p + vec3(0., 0.2 * abs(sin(u_time * TAU)), 0.), buttonCol));
	
	d = min(boxD, buttonD);
	d = min(d, led);

	float colD = boxD;
	vec3 finalCol = vec3(0.15);
	if (buttonD < colD) {
		colD = buttonD;
		finalCol = buttonCol;
	}
	if (led <= colD) {
		colD = led;
		float dominant = 0.75 * abs(sin(u_time * PI * 1.5)) + 0.20;
		finalCol = (isRedLed) ? vec3(dominant, 0.10, 0.15) : vec3(0.15, dominant, .1);
	}
	col = finalCol;

  	return d;
}

float getDist(vec3 p, out vec3 col) 
{
	vec4 s = vec4(0, 1, 6, 1); //Sphere xyz is position w is radius
	float sphereDist = length(p - s.xyz) - s.w;
	float planeDist  = p.y;
	float buzzerBox = sdRoundBox(p, vec3(2, 3.2, 1.6), 2.15);
	vec3 buzzerCol = vec3(0);
	vec3 buzPos = p - vec3(0, -5.8 + 0.2 * sin(u_time * 0.2 * TAU), 25);
	buzPos.xz *= rot(0.25 * cos(u_time) * u_time);
	float d = drawBuzzer(buzPos, false, buzzerCol);
	col = buzzerCol;
	return d;
}
 
float rayMarch(vec3 ro, vec3 rd, out vec3 col) 
{
	float dO = 0.; //Distane Origin
	vec3 outCol;
	for(int i = 0; i < MAX_STEPS; i++)
	{
		vec3 p = ro + rd * dO;
		vec3 iterCol;
		float ds = getDist(p, outCol); // ds is Distance Scene
		dO += ds;
		if(dO > MAX_DIST || ds < SURF_DIST) 
		break;
	}
	col = outCol;
	return dO;
}
 
vec3 getNormal(vec3 p)
{ 
	vec3 _ = vec3(0);
	float d = getDist(p, _); // Distance
	vec2 e = vec2(.01, 0); // Epsilon
	vec3 n = d - vec3(
	getDist(p - e.xyy, _),
	getDist(p - e.yxy, _),
	getDist(p - e.yyx, _));
 
	return normalize(n);
}

float getLight(vec3 p)
{ 
	// Directional light
	vec3 lightPos = vec3(5.0, 5.0, 5.0); // Light Position
	vec3 l = normalize(lightPos - p); // Light Vector
	vec3 n = getNormal(p); // Normal Vector
   
	float dif = dot(n, l); // Diffuse light
	dif = clamp(dif, 0., 1.); // Clamp so it doesnt go below 0
   
	// Shadows
	vec3 _ = vec3(0);
	float d = rayMarch(p + n * SURF_DIST * 2., l, _); 
	 
	if(d < length(lightPos - p)) dif *= .1;
 
	return dif;
}
 
void main()
{
	vec2 uv = (gl_FragCoord.xy - .5 * u_resolution.xy) / u_resolution.y;
	 
	vec3 ro = vec3(0, 1, 0); // Ray Origin/Camera
	vec3 rd = normalize(vec3(uv.x, uv.y, 1)); // Ray Direction
   
	vec3 surfCol = vec3(0);
	float d = rayMarch(ro, rd, surfCol); // Distance
   
	vec3 p = ro + rd * d;
	float dif = getLight(p); // Diffuse lighting
	d *= .2;
	vec3 color = vec3(dif) * surfCol;
	// color = surfCol;
	//color += getNormal(p);
	//float color = getLight(p);
 
	// Set the output color
	if (color.rgb == vec3(0)) {
		color = vec3(0, 0, 1);
	}
	gl_FragColor = vec4(color,1.0);
}