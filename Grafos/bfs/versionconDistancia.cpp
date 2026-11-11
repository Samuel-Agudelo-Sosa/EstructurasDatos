#include <bits/stdc++.h>
using namespace std;

void solve() {
     
   /*
   1: [2,4]
   2 [3,1]
   3 [2,4]
   4 [1,3]
   */
   int n = 4;
   int start =1;
   vector<vector<int>> dct = {
    {0,0}, {2,4}, {3,1}, {2,4}, {1,3}};

   queue<int> cola;
   cola.push(start);


   vector<int> distancias(n+1, 1e7); // se inicializan las distancias como infinito
   distancias[start] = 0;

   while(!cola.empty()){
    int node = cola.front();
    cola.pop();
    cout << node << ' ';
    for(int new_node : dct[node]){
        if (distancias[new_node] == 1e7){ // si es infinito no está visitado
            cola.push(new_node);
            distancias[new_node] = distancias[node] + 1;
        }

    }
   }

   cout << "\n";
   for(int i = 1; i < distancias.size(); i++) cout << distancias[i] << " ";
}

int main() {
    // Optimización de entrada/salida para CP
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin >> t; // Descomentar si hay múltiples casos de prueba
    while(t--) {
        solve();
    }
    return 0;
}