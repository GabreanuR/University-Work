#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Artefact {
protected:
    static int counterIdArtefact;
    const int id;
    // false = scazut, true = ridicat
    bool colectibil;

public:
    Artefact(): id(counterIdArtefact++) {
    }
};

class Istoric : public Artefact {
    string nume;
};

class Artistic : public Artefact {
    // tip = 1 corespunde sculptura
    // tip = 2 corespunde pictura
    int tip;
    //material = 1 acrilic
    //material = 2 ulei
    //material = 3 lemn
    //material = 4 piatra
    //material = 5 marmura
    int material;
};

class Pretios : public Artefact {
    string nume;
    int greutate;

public:
};

int Artefact::counterIdArtefact = 1;

class Participant {
protected:
    static int counterIdParticipant;
    const int id;
    int buget;
    // 1 = istoric, 2 = artistic, 3 = pretios
    int tipPreferat;
    int tipIgnorat;
    int pas;
    int vConfort;

public:
    Participant(): id(counterIdParticipant) {
    }

    virtual void read(istream &in) {
    }

    friend istream &operator >>(istream &in, Participant &participant) {
        participant.read(in);
        return in;
    }
};


class Fizic : public Participant {
    string nume;

public:
    void read(istream &in) override {
        cout << "Selecteaza nume:\n";
        cin >> nume;
        cout << "Tipuri: 1 = istoric, 2 = artistic, 3 = pretios\n";
        cout << "Selecteaza un tip preferat:\n";
        cin >> tipPreferat;
        cout << "Selecteaza un tip ignorat:\n";
        cin >> tipIgnorat;
        cout << "Selecteaza numarul de pasi:\n";
        cin >> pas;
        cout << "Selecteaza valoarea de confort\n";
        cin >> vConfort;
    }
};

class Juridic : public Participant {
    string nume;
    string numeReprezentant;

public:
    void read(istream &in) override {
        cout << "Selecteaza nume organizatie:\n";
        cin >> nume;
        cout << "Selecteza nume reprezentant:\n";
        cout << "Tipuri: 1 = istoric, 2 = artistic, 3 = pretios\n";
        cout << "Selecteaza un tip preferat:\n";
        cin >> tipPreferat;
        cout << "Selecteaza un tip ignorat:\n";
        cin >> tipIgnorat;
        cout << "Selecteaza numarul de pasi:\n";
        cin >> pas;
        cout << "Selecteaza valoarea de confort\n";
        cin >> vConfort;
    }
};

int Participant::counterIdParticipant = 1;

class Licitatie {
protected:
    std::vector<Participant *> participanti;

public:
    Licitatie();
    ~Licitatie() {
        for (auto p : participanti)
            delete p;
    }
    void displayMenu();

    void adaugaParticpant();
};

Licitatie::Licitatie() = default;

void Licitatie::displayMenu() {
    while (true) {
        cout << "---MENU---\n";
        cout << "1. Adauga Participant\n";
        cout << "2. \n";
        cout << "3. \n";
        cout << "4. \n";
        cout << "5. \n";
        cout << "6. \n";
        cout << "7. \n";
        cout << "8. \n";
        cout << "9. EXIT\n";
        cout << "Alege o optiune:";
        int choice;
        cin >> choice;
        switch (choice) {
            case 1:
                adaugaParticpant();
                break;
            //
            case 9:
                return;
            default:
                break;
        }
    }
}

void Licitatie::adaugaParticpant() {
    cout << "1 = fizic\n2 = juridic\n";
    cout << "Alege tip de persoana:";
    int type;
    cin >> type;
    Participant *participant = nullptr;
    switch (type) {
        case 1:
            participant = new Fizic();
            cin >> *participant;
            break;
        case 2:
            participant = new Juridic();
            cin >> *participant;
            break;
        default:
            delete participant;
            cout << "Nu este un tip de persoana!\n";
            break;
    }
    if (participant)participanti.push_back(participant);
}


int main() {
    Licitatie licitatie;
    licitatie.displayMenu();
    return 0;
}
