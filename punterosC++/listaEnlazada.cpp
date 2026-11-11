#include <iostream>

using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;

    Nodo(int v, Nodo* sig = nullptr){
        dato = v;
        siguiente = sig;
    }
};


class ListaEnlazada {
    private:
        Nodo* cabeza;
    
    public:
        ListaEnlazada(){
            cabeza = nullptr;
        }

        void insertar(int valor){
            Nodo* nuevo = new Nodo{valor, cabeza};
            cabeza = nuevo;
        }

        void imprimir() {
            Nodo* actual = cabeza;
            while (actual != nullptr){
                cout << actual -> dato << " -> ";
                actual = actual -> siguiente;

            }
            cout << "nullptr\n";
        
        }

        ~ListaEnlazada() {
            Nodo* actual = cabeza;
            while (actual != nullptr) {
                Nodo* temp = actual;
                actual = actual -> siguiente;
                delete temp; // Limpieza manual del Heap
            }
        }
};


int main() {
    ListaEnlazada lista;

    cout << "--- Insertando elementos ---" << endl;
    lista.insertar(10);
    lista.insertar(20);
    lista.insertar(30);

    cout << "Contenido de la lista:" << endl;
    lista.imprimir(); 
    // Salida esperada: 30 -> 20 -> 10 -> nullptr

    return 0; // Al salir del scope de main, el destructor ~ListaEnlazada() se ejecuta automáticamente.
}