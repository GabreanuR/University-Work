#include <iostream>
#include <vector>
#include <typeinfo>

using namespace std;


class Elev
{
    string nume;
    public:
        Elev(string s = "") {nume = s;}
        friend ostream& operator<< (ostream& out, Elev& e){ return out<<e.nume<<endl;}
};


/********** template-uri **************/
/*
class Elev
{
    string nume;
    public:
        Elev(string s = "") {nume = s;}
        friend ostream& operator<< (ostream& out, Elev& e){ return out<<e.nume<<endl;}
};

class Masina
{
    int an;
public:
    Masina(int a = 0){an = a;}
///    friend ostream& operator<< (ostream& out, Masina& m){ return out<<m.an<<endl;}
};

/*
void afis(int x){cout<<x<<endl;}
void afis(char x){cout<<x<<endl;}
void afis(float x){cout<<x<<endl;}
*/

template<class T>
void afis(T x){cout<<x<<endl;}

template<>
void afis(float x){cout<<"specializare pe float "<<x<<endl;}

void afis(float x){cout<<"netemplate "<<x<<endl;}

template<class T>
void afis(T x, T y){cout<<"afis cu 2 param "<<x<<" "<<y<<endl;}

template<>
void afis(int x, int y){cout<<"specializare pe int "<<x<<" "<<y<<endl;}

///void afis(int x, int y){cout<<"nontemplate pe int "<<x<<" "<<y<<endl;}

/**** prioritate varianta nontemplate, apoi specializare de template, apoi template ****/
int main()
{
    afis((float)34.56, 89.56);

///    afis(123, 45);
/*    afis(1);
    afis('B');
    afis((float)45.67);
    afis<>((float)89.76);
    afis<float>((float)12.34);
    Elev e("Ana");
    afis(e);
*/
    return 0;
}


/************* typeid si static_cast vs dynamic_cast ***********/
/*
class Baza{public: virtual ~Baza(){}};
class Elev : public Baza
{
    string nume;
    public:
        Elev(string s = "") {nume = s;}
        friend ostream& operator<< (ostream& out, Elev& e){ return out<<e.nume<<endl;}
};

class Masina : public Baza
{
    int an;
public:
    Masina(int a = 0){an = a;}
    friend ostream& operator<< (ostream& out, Masina& m){ return out<<m.an<<endl;}
};

int main()
{
    vector<Baza*> v;
    v.push_back(new Masina(2000));
    v.push_back(new Elev("Ana"));
    v.push_back(new Masina(2025));
    v.push_back(new Elev("Bob"));
    v.push_back(new Masina(2020));

//    for(auto x : v)
//        if (typeid(*x) == typeid(Elev)) cout<<*static_cast<Elev*>(x);

    for(auto x : v)
        if (auto p = dynamic_cast<Elev*>(x)) cout<<*p;

return 0;
}
*/
/*********** recapitulare tratarea exceptiilor, ca la subiecte de examen **************************/
/*
class Baza{ public: virtual ~Baza(){}};
class D1 : virtual public Baza{};
class D2 : public D1{};
class D3 : virtual public Baza{};
class D4 : public D1, public D3{}; /// nu conteaza ordinea mostenirii ci conteaza ordinea catch-urilor

int main()
{
    D4 ob;
    Baza& re = ob;
    try{
        throw re;
    }
    catch(D4& o){cout<<"D4\n";}
    catch(Baza& o){cout<<"Baza\n";} /// atentie, catch-ul acesta prinde ref din Baza catre ob, indiferent de ierarhie polimorfica sau nu
    catch(D2& o){cout<<"D2\n";}
    catch(D3& o){cout<<"D3\n";}
    catch(D1& o){cout<<"D1\n";}
}
*/
/*
class Baza{};
class D1 : virtual public Baza{};
class D2 : public D1{};
class D3 : virtual public Baza{};
class D4 : public D1, public D3{}; /// nu conteaza ordinea mostenirii ci conteaza ordinea catch-urilor

int main()
{
    D4 ob;
    try{
        throw ob;
    }
    catch(D2 o){cout<<"D2\n";}
    catch(D3 o){cout<<"D3\n";}
    catch(D1 o){cout<<"D1\n";}
    catch(Baza o){cout<<"Baza\n";}
}
*/

/*
class Test
{
    int x;
public:
    Test(int a = 0) : x(a){}
///    operator int(){return x;}
};

int main()
{
    Test A = 123;
    int y = A; /// nu merge daca nu exista operator de cast catre int; apoi se arunca exceptie int
    try{
///        throw A;
    throw y;
    }
    catch(int a){cout<<"int\n";}
    catch(Test a){cout<<"Test\n";} /// se afiseaza "Test" daca e throw A;
}
*/

/*
class Baza{};
class D1 : public Baza{};
class D2 : public D1{};
class D3 : public Baza{};

int main()
{
    D3 ob;
    try{
///        throw ob;
///        throw static_cast<D1>(ob);
        D1 ob1;
        ob1 = static_cast<D1>(ob); /// nu poate fi facut cast
        throw ob1;
    }
    catch(D1 o){cout<<"D1\n";}
    catch(D2 o){cout<<"D2\n";}
    catch(Baza o){cout<<"Baza\n";}
    catch (D3 o){cout<<"D3\n";}
    return 0;
}
*/

/*
int main()
{
    D2 ob;
    try{
        throw ob;
    }
///    catch(...){cout<<"multiplu\n";} /// catch multiplu e "ultima sansa"
    catch(D1 o){cout<<"D1\n";}
    catch(D2 o){cout<<"D2\n";}
///    catch(...){cout<<"multiplu\n";} /// catch multiplu e "ultima sansa"
///    catch(Baza o){cout<<"Baza\n";}
///    catch(...){cout<<"multiplu1\n";} /// catch multiplu e "o singura data"
///    catch(...){cout<<"multiplu2\n";} /// catch multiplu e "ultima sansa"

    return 0;
}
*/
