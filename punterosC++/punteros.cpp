#include <iostream>

using namespace std;

//las variables se guardan en la ram
//La ram se puede imaginar como una tira de celdas donde cada celda tiene un id que es dirección de memoria

//la memoria se almacena en el stack donde hay variables locales y llamados a funciones todo con liberación automática
//el heap es una zona de memoria dinámica de gran capacidad gestionada manualmente por el programador, donde los datos persisten hasta que se liberen


int main() {
    int numero = 42;
    cout << "Valor almacenado: " << numero << "\n";
    cout << "Dirección de memoria: " << &numero << "\n"; //se escribe la dirección de memoria en hexadecimal (Ej: ox7ffd56a8)
   

    //un puntero es una variable cuyo valor es la direccion de memoria de otra variable
    int x = 10;
    int* prt = &x; //prt contiene la direccion ede x
    cout << "Dirección guardada en prt: " << prt << "\n";
    cout << "Valor al que apunta: " << *prt << "\n";

    *prt = 20; // actualiza la variable a la que apunta es decir x
    cout << "nuevo valor en x: " << x << "\n";
    cout << "prt sigue aputando a x: " << prt << "\n";
    cout << "prt tiene su propia dirección de memoria también es variable: " << &prt << "\n"; //un puntero es una variable común y corriente tambiént iene su propia dirección de memoria en el stack
    
    // a los punteros solo se les asigna direcciones de memoria
    int* prt2 = prt; // copia a donde apunta prt
    int* prt3 = nullptr; // puntero nulo, significa no apunta a nada.


     return 0;

}