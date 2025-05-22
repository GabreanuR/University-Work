#include <iostream>
#include <exception>
#include <vector>

using namespace std;

/******* sabloane ******/


class Test{
    int x;
public:
    friend ostream& operator<<(ostream& out, Test& ob){return out<<ob.x;}
};

template<class T>
void afis(T v[10], int n)
{
    for(int i = 0; i<n; i++)
        cout<<v[i]<<" ";
    cout<<endl;
}

void afis(int v[10], int n)
{
    cout<<"nontemplate int\n";
    for(int i = 0; i<n; i++)
        cout<<v[i]<<" ";
    cout<<endl;
}

template<>
void afis(float v[10], int n)
{
    cout<<"specializare de functie template; T = float";
    for(int i = 0; i<n; i++)
        cout<<v[i]<<" ";
    cout<<endl;
}

template<>
void afis(int v[10], int n)
{
    cout<<"specializare de functie template; T = int";
    for(int i = 0; i<n; i++)
        cout<<v[i]<<" ";
    cout<<endl;
}


int main()
{
    int v[] = {3,6,7,8};
    float w[] = {(float)1.2, (float)3.67};
    ///afis(v,4);
    afis<>(v,4);
    afis(w,2);
    Test a[3];
    afis(a,3);
    return 0;
}


/*******************************/

/*
class Negativ : public exception
{
public:
    const char* what() const throw()
    {
        return "grupa nu poate avea nr negativ de studenti\n";
    }
};

class Peste : public exception
{
public:
    const char* what() const throw()
    {
        return "grupa nu poate avea >= 40 studenti\n";
    }
};

class grupa
{
    int x;
public:
    grupa(int _x = 0) : x(_x)
    {
        if (x < 0) throw Negativ();
        if (x >= 40) throw Peste();
    }
    void afis()
    {
        cout<<x<<endl;
    }
};

class Meniu
{
    vector<grupa> v;

    Meniu(){}
    Meniu(const Meniu& ob){}
    ~Meniu(){}

    static Meniu* instanta;

public:

    static Meniu* get_instanta()
    {
        if (instanta == NULL) instanta = new Meniu();
        return instanta;
    }
    void citire()
    {
        for(int i = 0; i < 3; i++)
        {
            try
            {
                cout<<"dati nr de studenti: ";
                int a;
                cin>>a;
                v.push_back(grupa(a));
            }
            catch(exception& ob)
            {
                cout<<ob.what();
            }
        }
    }
    void afis()
    {
        for(auto& x : v)
            x.afis();
    }
};
    Meniu* Meniu::instanta = NULL;

int main()
{
    Meniu* m = Meniu::get_instanta();
    m->citire();
    m->afis();
    Meniu* m2 = Meniu::get_instanta();
    m2->afis();
    /*
    Meniu m;
    m.citire();
    m.afis();
    */

    /*
    vector<grupa> v;
    for(int i = 0; i < 3; i++)
    {
        try
        {
            cout<<"dati nr de studenti: ";
            int a;
            cin>>a;
            v.push_back(grupa(a));
        }
        catch(exception& ob)
        {
            cout<<ob.what();
        }
    }

    //    for(vector<grupa>::iterator x = v.begin(); x != v.end(); x++)
    //        x->afis();
    /// iterator asemanator cu pointer, deci, trebuie dereferentiere (*x).afis();

    for(auto& x : v)
        x.afis();
    */
    /*
    try{
    cout<<"dati nr de studenti: ";
    int a; cin>>a;
        grupa Ob(a);
        Ob.afis();
    }
    /*    catch(Negativ& ob)
    {
        cout<< ob.what();
    }
    catch(Peste& ob)
    {
        cout<<ob.what();
    }
    */ /*   catch(exception& ob)
{
cout<<ob.what();
}
*/
/*
    return 0;
}
*/

