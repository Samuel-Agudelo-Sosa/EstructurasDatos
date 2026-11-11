#include <bits/stdc++.h>
using namespace std;

void solve() {
     
   /*
   1: [2,4]
   2 [3,1]
   3 [2,4]
   4 [1,3]
   */

   int start =1;
   vector<vector<int>> dct = {
    {0,0}, {2,4}, {3,1}, {2,4}, {1,3}};

   queue<int> cola;
   cola.push(start);
   unordered_set<int> visited {1};

   while(!cola.empty()){
    int node = cola.front();
    cola.pop();
    cout << node << ' ';
    for(int new_node : dct[node]){
        if (! visited.count(new_node)){
            cola.push(new_node);
            visited.insert(new_node);
        }

    }
   }
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