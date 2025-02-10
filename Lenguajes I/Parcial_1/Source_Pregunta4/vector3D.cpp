#include "vector3D.h"
#include <math.h>

// Suma de vectores.
V_3D V_3D::operator + (V_3D v){
    return V_3D(x + v.x, y + v.y, z + v.z);
}
// Recta de vectores.
V_3D V_3D::operator - (V_3D v){
    return V_3D(x - v.x, y - v.y, z - v.z);
}

// Producto cruz de vectores.
V_3D V_3D::operator * (V_3D v){
    return V_3D(y*v.z - z*v.y, z*v.x - x*v.z, x*v.y - y*v.x);
}

// Produnto punto de vectores.
double V_3D::operator % (V_3D v){
    return x*v.x + y*v.y + z*v.z;
}

// Norma de vectores.
double V_3D::operator & (){
    return sqrt(x*x + y*y + z*z);
}

// Operador Suma con argumento V_3D y numeros.
V_3D V_3D::operator + (double number){
    return V_3D(x+number, y+number, z+number);
}

// Operador Resta con argumento V_3D y numeros.
V_3D V_3D::operator - (double number){
    return V_3D(x-number, y-number, z-number);
}

// Operador Multiplicar con argumento V_3D y numeros.
V_3D V_3D::operator * (double number){
    return V_3D(x*number, y*number, z*number);
}

// Impresion por consola un vector 3D.
std::ostream& operator << (std::ostream &console, V_3D v){
    console << "[" << v.x << ", " << v.y << ", " << v.z << "]";
    return console;
}