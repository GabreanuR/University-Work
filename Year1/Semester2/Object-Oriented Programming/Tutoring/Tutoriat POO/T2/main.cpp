#include <iostream>
#include <string>
using namespace std;

class Calculator {
    const int id;
    static int counter_id;

    string procesor;
    bool placa_video;
    int ram;

public:
    // Constructori
    Calculator();

    Calculator(string procesor, bool placa_video, int ram);

    Calculator(string procesor);

    Calculator(const Calculator &obj);

    Calculator& operator=(const Calculator &obj);
    // Methods

    static void functie() {
        counter_id = 10;
        cout<<counter_id;
    }

    // static void functie(){
    //     this->counter_id = 0;        NU MERGE
    //     cout<<counter_id;
    // }

    ~Calculator() {
        cout << "Destructor called" << endl;
    }

    int getId() const {
        return this->id;
    }
};

int Calculator::counter_id = 1;

Calculator::Calculator(): id(counter_id++) {
    this->procesor = "unknown";
    this->placa_video = true;
    this->ram = 8;
}

Calculator::Calculator(string procesor, bool placa_video, int ram): id(counter_id++) {
    this->procesor = procesor;
    this->placa_video = placa_video;
    this->ram = ram;
}

Calculator::Calculator(const Calculator &obj): id(counter_id++) {
    this->procesor = obj.procesor;
    this->placa_video = obj.placa_video;
    this->ram = obj.ram;
}

Calculator::Calculator(string procesor): id(counter_id++) {
    this->procesor = procesor;
    this->placa_video = 0;
    this->ram = 0;
};

// void f(float a) {
//     cout << "no";
// };
//
// void f(double a) {
//     cout << "yes";
// };

Calculator& Calculator::operator=(const Calculator &obj) {
    this->procesor = obj.procesor;
    this->placa_video = obj.placa_video;
    this->ram = obj.ram;
    return *this;
}

int main() {
    Calculator a;
    // Calculator b("pentium", 0, 10000);
    // cout<< Calculator::counter_id << endl; MERGE DACA E PUBLIC DAR NU AVEM VOIE SA ACCESAM MEMBRII STATICI DIN INSTANTE
    // float x = 3.14;
    // f(3.14);
    cout << a.getId();
}
