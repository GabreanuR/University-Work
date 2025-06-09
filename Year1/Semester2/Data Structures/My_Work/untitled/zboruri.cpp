#include <string>
#include <iostream>
#include <vector>

class Zbor {
    std::string zborId;
    std::string zborName;
    int ziPlecare = 0;
    int lunaPlecare = 0;
    int anPlecare = 0;
    std::string orasPlecare;
    std::string orasDestinatie;
    int durataZile = 0;

public:
    Zbor();

    Zbor(const std::string &zborId, const std::string &zborName, int ziPlecare,
         int lunaPlecare, int anPlecare, const std::string &orasPlecare,
         const std::string &orasDestinatie, int durataZile) {
        this->zborId = zborId;
        this->zborName = zborName;
        this->ziPlecare = ziPlecare;
        this->lunaPlecare = lunaPlecare;
        this->anPlecare = anPlecare;
        this->orasPlecare = orasPlecare;
        this->orasDestinatie = orasDestinatie;
        this->durataZile = durataZile;
    }

    ~Zbor();

    Zbor &operator=(const Zbor &obj) {
        if (this == &obj)
            return *this;

        this->zborId = obj.zborId;
        this->zborName = obj.zborName;
        this->ziPlecare = obj.ziPlecare;
        this->lunaPlecare = obj.lunaPlecare;
        this->anPlecare = obj.anPlecare;
        this->orasPlecare = obj.orasPlecare;
        this->orasDestinatie = obj.orasDestinatie;
        this->durataZile = obj.durataZile;

        return *this;
    };

    friend std::ostream &operator<<(std::ostream &out, const Zbor &obj) {
        return out;
    };

    friend std::istream &operator>>(std::istream &in, Zbor &obj) {
        std::cout << "";
        return in;
    };
};

class Container {
    int numarCurse = 0;
    int pretBilet = 0;
    Zbor ruta;

public:
    Container(const int numarCurse, const int pretBilet) {
        Zbor tempZbor;
        std::cin >> tempZbor;
        this->ruta = tempZbor;
        this->numarCurse = numarCurse;
        this->pretBilet = pretBilet;
    }
};
