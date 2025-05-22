#include <iostream>
#include <vector>
#include <typeinfo>

using namespace std;

class Baza
{
    protected:
    int x;
public:
    Baza(int _x = 0) : x(_x){}
    virtual void afis() const {cout<<"x = "<<x<<" ";}
//    friend istream& operator>>(istream& in, Baza& ob){return in>>ob.x;}
    void f(){}

    virtual void citire(){cout<<"x = "; cin>>x;}
    friend istream& operator>>(istream& in, Baza& ob)
    {
        ob.citire();
       /// return in;
    }
};

class Derivata1 : public Baza
{
    int y;
public:
    Derivata1(int _x = 0, int _y = 0) : Baza(_x),y(_y){}
    void afis()const{Baza::afis(); cout<<"y = "<<y<<endl;}
    friend istream& operator>>(istream& in, Derivata1& ob){return in>>ob.x>>ob.y;}
    void citire(){Baza::citire(); cout<<"y = "; cin>>y;}
};

class Derivata2 : public Baza
{
    int z;
public:
    Derivata2(int _x = 0, int _z = 0) : Baza(_x),z(_z){}
    void afis()const{Baza::afis(); cout<<"z = "<<z<<endl;}
    /*
    friend istream& operator>>(istream& in, Derivata2& ob)
    {
        in>>dynamic_cast<Baza&>(ob);
        in>>ob.z;
        return in;
    }*/

    void citire(){Baza::citire(); cout<<"z = "; cin>>z;}
};

int main()
{
    vector<Baza*> v;
    v.push_back(new Baza());
    cin>>*v.back();
    v.push_back(new Derivata1());
    cin>>*v.back();
    v.push_back(new Derivata2());
    cin>>*v.back()>>*v.back();
    cin>>*v.back();

    for(auto& x : v)
        x->afis();

    /*
    vector<Baza*> v;
//    v.push_back(new Baza());
//    cin>>*v.back();

//    v.push_back(new Derivata1());
//    cin>>*dynamic_cast<Derivata1 *>(v.back());

     v.push_back(new Derivata2());
//     cin>>*v.back();
    cin>>*dynamic_cast<Derivata2 *>(v.back());

    for(auto& x : v)
        x->afis();

    //v.push_back(new Derivata2());

    /*
    vector<Baza*> v;
    v.push_back(new Baza(1));
    v.push_back(new Derivata1(2,3));
    v.push_back(new Derivata2(4,5));

    for(auto& x : v)
        if (typeid(*x) == typeid(Derivata1))
            x->afis();
        else cout<<typeid(*x).name()<<endl;
    cout<<"********"<<endl;

    for(auto& x : v)
        if (dynamic_cast<Derivata1 *>(x) != NULL)
            x->afis();
        else cout<<"NULL";
    */

 /*
          B
        /   \
        D1  D2
        |
        D3
        |
        D4

        D3 ob;
        Baza *p; p = &ob;
        D1* q;
        q = dynamic_cast<D1 *>(p); /// q retine adresa &ob
        D4* r;
        r = dynamic_cast<D4*> (p); /// r retine NULL
    */
    /*
    for(auto& x : v)
        x->afis();///(*x).afis();
*/

    /*
    const Baza ob;
    ob.afis();
///    ob.f(); /// obiect const nu poate folosi functie membra neconst

    Baza ob1;
    ob1.afis();
    ob1.f();
    */
    return 0;
}
