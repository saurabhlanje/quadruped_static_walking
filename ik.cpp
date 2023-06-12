/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <math.h>

using namespace std;

float
calculateAngle (float a, float b, float c)
{
  // Calculating cosine of angle O1 using the cosine rule
  double cosPhi1 = (a * a + b * b - c * c) / (2 * a * b);

  // Calculating angle O1 in radians using the inverse cosine function (acos)
  float phi1 = acos (cosPhi1);

  // Converting angle from radians to degrees
  phi1 = phi1;

  return phi1;
}

void
printangle (float angle)
{

}

int
main ()
{
  float l1, l2, l3;
  float q1, q2, q3;
  float x, y, z;
  float x1, y1, z1;
  float r1, r2;
  float phi1, phi2;
  l1 = 27.47093226;
  l2 = 55.00450438;
  l3 = 80;
  cout << "Enter X Y Z" << endl;
  cin >> x;
  cin >> y;
  cin >> z;
  cout << x << " " << y << " " << z << " " << endl;
  q1 = atan (y / x);
  cout << "q1 is " << q1 * 180 / M_PI << endl;
  x1 = l1 * sin (q1);
  y1 = l1 * cos (q1);
  cout << "x1=" << x1 << " y1= " << y1 << endl;
  float dx = x - x1;
  float dy = y - y1;
  float dz = z - z1;
  r1 = sqrt (dx * dx + dy * dy + dz * dz);
  cout << "r1 is " << r1 << endl;


  phi1 = calculateAngle (l2, r1, l3);
  cout << phi1 * 180 / M_PI << endl;

  phi2 = asin (z / r1);
  cout << phi2 * 180 / M_PI << endl;

  q2 = phi1 + phi2;
  cout << "q2=  " << q2 * 180 / M_PI << endl;

  q3 = calculateAngle (l3, l2, r1) - M_PI * 0.5;
  cout << "q3= " << q3 * 180 / M_PI << endl;
  
  cout<<"qs are "<<q1* 180 / M_PI<<" "<<q2* 180 / M_PI<<" "<<q3* 180 / M_PI<<endl;





  return 0;
}
