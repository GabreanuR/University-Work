#include <iostream>
using namespace std;

class Cont {
private:
    double sold;
public:
    Cont(double s) : sold(s) {}
    friend void depune(Cont& c, double suma);
    friend class Auditor;
};

void depune(Cont& c, double suma) {
    c.sold += suma;
}

class Auditor {
public:
    void audit(const Cont& c) {
        cout << "Audit sold: " << c.sold << endl;
    }
};

int main() {
    Cont c(100.0);
    depune(c, 50.0);
    Auditor a;
    a.audit(c);
    return 0;
}
