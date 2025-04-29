#include <iostream>
#include <vector>

using namespace std;

class Item {
protected:
    static int count;
    const int id;

public:
};

class Zid : public Item {
private:
    double inaltime;
    double lungime;
    double grosime;

public:
    Zid();
};

class Turn : public Item {
private:
    double powlaser;

public:
    Turn();
};

class Robot : public Item {
private:
    int damage;
    int nivel;
    int viata;

public:
    Robot();
};

class RobotTerestru : public Robot {
    bool scut;
    int nrgloante;

public:
    RobotTerestru();
};

class RobotAerian : public Robot {
    double autonomie;

public:
    RobotAerian();
};

class Inventar {
    vector<Item> items;
};

int main() {
    return 0;
}
