#include <iostream>
#include <vector>

using namespace std;

struct Enemigo {
    int vida;
};

int main() {
    vector<Enemigo*> listaEnemigos; // Creación del vector de punteros a Enemigo

    //Asignación de memoria dinámica en el heap:
    listaEnemigos.push_back(new Enemigo{100}); //new reserva memoria en el heap y ejecuta el constructor para asignar el objeto.
    listaEnemigos.push_back(new Enemigo{250});

    //modificar la vida del primer enemigo
    listaEnemigos[0]->vida = 80;
    //Eso es azucar sintáctico y equivalente de:
    //(*listaEnemigos[0]).vida = 80
    cout << "Vida enemigo" << listaEnemigos[0]->vida << "\n";
    //memory leak: ocurre cuando se reserva memoria, pero se pierde el puntero antes de liberarla con delete consumiendo memoria mientras el programa corra
    
    for (Enemigo*& e : listaEnemigos) { 
        // Enemigo*  -> El tipo de elemento almacenado (un puntero a Enemigo).
        // &         -> Paso por referencia: 'e' es un alias del puntero real dentro de 'listaEnemigos',
        //              lo que nos permite asignarle 'nullptr' al elemento original y no a una copia local.
        delete e; //libera la memoria reservada en el heap 
        e = nullptr; // evita Dangling Pointer
        //Dangling Pointer ocurre porque aunque delete libere la memoria, el puntero sigue guardando la dirección de memoria antigua
        //si se intenta acceder a es adirección el programa intenta leer una memoria que no le pertenece cayendo en segmen fault
    }

    //implementar structs así no es practico, los punteros en lista enemigo están contiguos, pero los objetos están dispersos en el heap bajando la eficiencia por saltos constantes de la memoriaCache
    //aunque se copian solo direcciones de memoria que es muy barato para objetos grandes


    return 0;
}