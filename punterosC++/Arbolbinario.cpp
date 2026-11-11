#include <iostream>

using namespace std;

struct Nodo {
    int valor;
    Nodo* izq;
    Nodo* der;
    

    //constructor 
    Nodo(int v) {
        valor = v;
        izq = nullptr;
        der = nullptr;
    }
};
//se podrían meter los métodos dentro de una clase contenedora BST, así como se hará en el ejemplo de lista enlazada

void insertar(Nodo*& raiz, int valor) { //la referencia del puntero raíz, permite modificar a donde apuntara
    if (raiz == nullptr){
        raiz  = new Nodo(valor);
        return;
    }

    if (valor < raiz -> valor)  insertar(raiz -> izq, valor);
    else if (valor > raiz -> valor) insertar(raiz -> der, valor);
    
    else {
        cout << "No se admiten elementos iguales";
        return;
    }
}

Nodo* buscar(Nodo* raiz, int valor){
    if (raiz == nullptr || raiz -> valor == valor) return raiz;
    if (valor < raiz -> valor) return buscar(raiz -> izq, valor);
    return buscar(raiz -> der, valor);
    
}

void recorridoInOrden(Nodo* raiz) {
    if (raiz == nullptr) return;
    recorridoInOrden(raiz -> izq);
    cout << raiz -> valor << " ";
    recorridoInOrden(raiz -> der);
}

void liberarMemoria(Nodo*& raiz){
    if (raiz == nullptr) return;
    liberarMemoria(raiz -> izq);
    liberarMemoria(raiz -> der);
    delete raiz;
    raiz = nullptr;
}

int main() {
    Nodo* raiz = nullptr; // Apuntador inicial en el Stack apuntando a nulo

    // Inserción de datos
    insertar(raiz, 10);
    insertar(raiz, 5);
    insertar(raiz, 15);
    insertar(raiz, 2);
    insertar(raiz, 7);

    // Impresión del árbol
    cout << "Recorrido In-Orden: ";
    recorridoInOrden(raiz);
    cout << endl;

    // Búsqueda
    int clave = 7;
    Nodo* buscado = buscar(raiz, clave);

    if (buscado != nullptr) {
        cout << "El valor " << buscado -> valor << " fue encontrado en la dirección: " << buscado << endl;
    } else {
        cout << "El valor " << clave << " no existe en el árbol." << endl;
    }

    // Limpieza de memoria manual debido a esta implementación
    liberarMemoria(raiz);

    return 0;
}