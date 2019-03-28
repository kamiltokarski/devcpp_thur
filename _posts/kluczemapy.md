# Iteracja po elementach mapy

---
~~~~{.cpp}
#include <iostream>
#include <map>
using namespace std;


map<int, int> M;


int main() {
    int N;
    int a, x;
    cin >> N;

    for(int i = 0; i < N; ++i) {
        cin >> a >> x;
        M[a] += x; // wrzucamy jakies wartosci na mape
    }

    for(auto v : M) {
        int a = v.first; // klucz
        int x = v.second; // wartosc
        cout << a << " " << x << endl;
    }

    return 0;
}
~~~~