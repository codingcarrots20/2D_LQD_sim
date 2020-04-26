int IX(int x, int y) {
  x = constrain(x, 0, N-1);
  y = constrain(y, 0, N-1);
  return x + (y * N);
}
import java.io.BufferedWriter;
import java.io.FileWriter;

void appendTextToFile(String filename, String text){
   FileWriter fileWriter;
    BufferedWriter bufferedWriter;
    try {
      fileWriter = new FileWriter(filename, true); // true to append
      bufferedWriter = new BufferedWriter(fileWriter);
      bufferedWriter.write(text);
      bufferedWriter.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
}
  

class Fluid {
  int size;
  float dt;
  float diff;
  float visc;

  float[] s;
  float[] density;

  float[] Vx;
  float[] Vy;

  float[] Vx0;
  float[] Vy0;

  Fluid(float dt, float diffusion, float viscosity) {

    this.size = N;
    this.dt = dt;
    this.diff = diffusion;
    this.visc = viscosity;

    this.s = new float[N*N];
    this.density = new float[N*N];

    this.Vx = new float[N*N];
    this.Vy = new float[N*N];

    this.Vx0 = new float[N*N];
    this.Vy0 = new float[N*N];
  }

  void step() {
    int N          = this.size;
    float visc     = this.visc;
    float diff     = this.diff;
    float dt       = this.dt;
    float[] Vx      = this.Vx;
    float[] Vy      = this.Vy;
    float[] Vx0     = this.Vx0;
    float[] Vy0     = this.Vy0;
    float[] s       = this.s;
    float[] density = this.density;

    diffuse(1, Vx0, Vx, visc, dt);
    diffuse(2, Vy0, Vy, visc, dt);

    project(Vx0, Vy0, Vx, Vy);

    advect(1, Vx, Vx0, Vx0, Vy0, dt);
    advect(2, Vy, Vy0, Vx0, Vy0, dt);

    project(Vx, Vy, Vx0, Vy0);

    diffuse(0, s, density, diff, dt);
    advect(0, density, s, Vx, Vy, dt);
  }

  void addDensity(int x, int y, float amount) {
    int index = IX(x, y);
    this.density[index] += amount;
  }

  void addVelocity(int x, int y, float amountX, float amountY) {
    int index = IX(x, y);
    this.Vx[index] += amountX;
    this.Vy[index] += amountY;
  }
  
  void Write(int choice) { 
  //  0 input 1 output
  String fname1="/input.txt";
  String fname2="/output.txt";
  
  if (choice == 0)
  {
   for( int i=0;i<N;i++ ){
     for( int j=0;j<N;j++ ){
       
       appendTextToFile(fname1,Float.toString(this.density[ IX(i,j) ])+" ,");
       appendTextToFile(fname1,Float.toString(this.s[ IX(i,j) ])+" ,");
       appendTextToFile(fname1,Float.toString(this.Vx[ IX(i,j) ])+" ,");
       appendTextToFile(fname1,Float.toString(this.Vy[ IX(i,j) ])+" ,");
       appendTextToFile(fname1,Float.toString(this.Vx0[ IX(i,j) ])+" ,");
       appendTextToFile(fname1,Float.toString(this.Vy0[ IX(i,j) ])+" ,");
         
     }
   }
   appendTextToFile("/input.txt","end\n");
  }  
  else{
    for( int i=0;i<N;i++ ){
     for( int j=0;j<N;j++ ){
       
       appendTextToFile(fname2,Float.toString(this.density[ IX(i,j) ])+" ,");
       appendTextToFile(fname2,Float.toString(this.s[ IX(i,j) ])+" ,");
       appendTextToFile(fname2,Float.toString(this.Vx[ IX(i,j) ])+" ,");
       appendTextToFile(fname2,Float.toString(this.Vy[ IX(i,j) ])+" ,");
       appendTextToFile(fname2,Float.toString(this.Vx0[ IX(i,j) ])+" ,");
       appendTextToFile(fname2,Float.toString(this.Vy0[ IX(i,j) ])+" ,");
         
     }
   }
   appendTextToFile("/output.txt","end\n");
  }
      
    
    
 
  }

  void renderD() {


    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        float x = i * SCALE;
        float y = j * SCALE;
        float d = this.density[IX(i, j)];
        float ss = this.s[IX(i, j)];
        fill(d,ss,0.0);
        noStroke();
        square(x, y, SCALE);
      }
    }
  }

  void renderV() {

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        float x = i * SCALE;
        float y = j * SCALE;
        float vx = this.Vx[IX(i, j)];
        float vy = this.Vy[IX(i, j)];
        stroke(255);

        fill(0.0,vx*5000,vy*5000);
        noStroke();
        square(x, y, SCALE);
      }
    }
  }
  void renderV0() {

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        float x = i * SCALE;
        float y = j * SCALE;
        float vx0 = this.Vx0[IX(i, j)];
        float vy0 = this.Vy0[IX(i, j)];
        stroke(255);

        fill(vx0*1000000,0.0,vy0*1000000);
        noStroke();
        square(x, y, SCALE);
      }
    }
  }

  
}
