#include <iostream>
#include<vector>

using namespace std;


int main(){
    int arr[5] = {10, 20, 30, 40, 50};
    int* p = arr; // el nombre de un arreglo en c++ colapsa a un puntero al primer elemento
    //si le sumamos 1 a un puntero int*, el compilador no le suma 1 byte físico, sino que suma el sizeof(int) que son 4 bytes

    cout << "p: " << p << " " << *p << "\n";
    //p +1 se mueve al segundo elemento, pero esos son 4 bytes, (EJ se mueve de 0x1000 a 0x1004)
     cout << "p + 1: " << p + 1 << " " << *(p + 1) << "\n";
     // p +3 se mueve al cuarto elemento
     cout << "p + 3: " << p + 3 <<  " " << *(p + 3) << "\n"; 

     // estas sumas de punteros funcionan para estructuras nativas como arreglos
     // un iterador es una clase que imita la sintaxis de un puntero para navegar por cualquier estructura de datos tenga o no tenga memoria contigua
     //la sintaxis del iterador es la misma *it, it->metodo() it->atributo, it++, it +2, etc

    //en vectores v.begin() devuelve iterador (conceptualmente igual a un puntero) que apunta al primer elemento
    //v.end() devuelve un iterador que aputna a la posición justo depués del último elemento, 
    //de hecho por eso no se puede desreferenciar genera comportamiento indefinido, se debe es desreferenciar el v.end() -1
    vector<int> v = { 1, 2, 3};
    cout << "v.begin(): " << &(*(v.begin())) << " " << *(v.begin()) << "\n"; // un iterador no deja de ser un objeto de una clase da error imprimirlo
    //pero entonces más fácil se obtiene la dirección de memoria al objeto que apunta el iterador, ¿cómo se guardan los int en un vector?
    cout << "v.end() - 1: " << &(*(v.end() - 1)) << " " << *(v.end() - 1) << "\n";


    

    return 0;
}