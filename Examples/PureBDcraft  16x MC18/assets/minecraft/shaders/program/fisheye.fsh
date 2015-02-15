#version 120

// Fisheye

uniform sampler2D DiffuseSampler;

varying vec2 texCoord;

// 150 degrees (set fov in options.txt to 2.0)
const float C1 = 1.8;//2.617993877991494; // fov in radians
const float C2 = 0.4;//0.133974596215561; // 0.5/tan(C1*0.5)
const float Rlim = 0.6;//0.565685424949238; // sqrt(0.4*0.4 + 0.4*0.4)


void main() {
	float X = texCoord.x - 0.5;
	float Y = texCoord.y - 0.5;
	
	// Distance from centre of screen
    float R = sqrt(X*X + Y*Y);
	
	// Discard pixels for which the tangent wraps around
	//if(R > Rlim) discard;
	
	float T = tan(C1*R)*C2;
	float C = T/R;
	
	X = X*C + 0.5;
	Y = Y*C + 0.5;
	
	if(X < 0.0 || Y < 0.0 || X > 1.0 || Y > 1.0) discard;

	gl_FragColor = texture2D(DiffuseSampler, vec2(X, Y));
}
