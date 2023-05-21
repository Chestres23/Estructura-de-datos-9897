#include <iostream>
#include <vector>
using namespace std;

vector<int> decimalaBinario(int decimal) {
    vector<int> binario;

    while (decimal > 0) {
        int remainder = decimal % 2;
        binario.push_back(remainder);
        decimal /= 2;
    }

    return binario;
}

int main() {
    int decimal;
    cout << "Ingrese un número decimal: ";
    cin >> decimal;

    vector<int> binary = decimalaBinario(decimal);

    cout << "El número binario es: ";
    for (int i = binary.size() - 1; i >= 0; i--) {
        cout << binary[i];
    }
    cout << endl;

    return 0;
}