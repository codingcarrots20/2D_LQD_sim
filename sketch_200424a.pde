import java.io.FileWriter;
import java.io.*;


import java.util.Random;

final int N = 16;
final int iter = 16;
final int SCALE = 1;
float t = 0;
float dt = 0.2;
int c=N/2;

Fluid fluid;

 

 



void settings() {
  size(N*SCALE, N*SCALE);
  fluid = new Fluid(dt, 0, 0.0000001);

  
}

void setup() {
  String[] lines = loadStrings("demofile.txt");
  for (int i=0; i<lines.length; i+=4)
  {
    int x = Integer.parseInt(lines[i]);
    int y = Integer.parseInt(lines[i+1]);
    fluid.addDensity(x, y, 10000.0);

    fluid.addVelocity(x, y, Float.parseFloat(lines[i+2]),Float.parseFloat(lines[i+3]) );
  }
  
}
 
  


int x=0;
void draw() {
  background(0);



  if (x < 30) {
    fluid.step();



    fluid.renderV0();

    x = x + 1;
  } else {
    noLoop();
  }
  saveFrame();





  //fluid.renderV();
  //fluid.fadeD();
}
