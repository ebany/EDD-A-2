#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int suma(int numero1, int numero2);
int sumaConParamReferencia(int *numero1, int *numero2);
void readCsv();

int main() {
    //imprimir en consola
    cout << "Hola mundo" << endl;

    //leer numero de consola
    int numero;
    cout << "Ingrese un numero: ";
    cin >> numero;
    cout << "El numero ingresado es: " << numero << endl;

    //otra forma de imprimir en consola
    printf("El numero ingresado es: %d\n", numero);

    //imprimir string
    string ejemplo1 = "String imprimiendo pasando apuntador";
    printf("%s\n", ejemplo1.c_str());

    //leer string desde consola, con espacios incluidos
    string nombreAlumno1;
    cout << "Ingrese su nombre: ";
    cin.ignore();
    getline(cin, nombreAlumno1);
    cout << "Bienvenido alumno1: " << nombreAlumno1 << endl;

    //leer string desde consola, sin espacios incluidos
    char temporal[100];
    printf("Ingrese su nombre: ");
    scanf("%100s", temporal);
    string nombreAlumno2 = temporal;
    printf("Bienvenido alumno2: %s\n", nombreAlumno2.c_str());

    //uso de funciones y punteros
    int numero1 = 1;
    int numero2 = 2;
    cout << "Variables sin modificar ---------------" << endl;
    cout << "Resultado:" << suma(numero1, numero2) << endl;
    cout << numero1 << endl;
    cout << numero2 << endl;
    cout << "Variables modificadas ------------------" << endl;
    cout << "Resultado:" << sumaConParamReferencia(&numero1, &numero2) << endl;
    cout << numero1 << endl;
    cout << numero2 << endl;

    //uso de punteros
    int numero3 = 10;
    int *punteroInt;
    punteroInt = &numero3;
    cout << "Dirección de memoria de numero3: " << &numero3 << endl;
    cout << "Dirección de memoria de punteroInt: " << punteroInt << endl;
    cout << "Valor de punteroInt: " << *punteroInt << endl;
    cout << "Dirección de memoria de punteroInt: " << &punteroInt << endl;

    //leer csv
    readCsv();

    return 0;
}

int suma(int numero1, int numero2) {
    numero1++;
    return numero1 + numero2;
}

int sumaConParamReferencia(int *numero1, int *numero2) {
    *numero1 = *numero1 + 1;
    return *numero1 + *numero2;
}

void readCsv() {
    //read csv
    ifstream file("file.csv");
    string line;
    while (getline(file, line))
    {
        stringstream ss(line);
        string data;
        while (getline(ss, data, ','))
        {
            cout << data << "\n";
        }
    }
}