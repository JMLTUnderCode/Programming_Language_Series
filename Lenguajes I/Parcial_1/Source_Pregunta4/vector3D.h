
/*
    Definicion principal de HEADER "vector3D.h" para la creacion de librerias 
    en C++. Una vez definido la clase V_3D con cada una de predefiniciones
    de las sobrecargas a los operadores se debe tener un archivo adicional
    "vector3D.cpp" que tendra el Body de cada sobrecarga.
*/
#ifndef _VECTOR3D
    #define _VECTOR3D
        #include <iostream>
        class V_3D{
        public:
            double x, y, z;

            // Constructor vacio.
            V_3D(){
                this->x = 0; this->y = 0; this->z = 0;
            }
            // Contructor completo.
            V_3D(double _x, double _y, double _z){
                this->x = _x; this->y = _y; this->z = _z;
            }

            // Definicion de sobrecarga para operadores vector con vector.
            V_3D operator + (V_3D v);
            V_3D operator - (V_3D v);
            V_3D operator * (V_3D v);
            double operator % (V_3D v);
            double operator & ();

            // Definicion de sobrecarga para operaciones vector con numero.
            V_3D operator + (double number);
            V_3D operator - (double number);
            V_3D operator * (double number);

            // Definicion de sobrecarga para stdout, lograr mostrar por pantalla
            // el tipo de dato de manera elegante.
            friend std::ostream& operator << (std::ostream &console, V_3D v);
        };
#endif