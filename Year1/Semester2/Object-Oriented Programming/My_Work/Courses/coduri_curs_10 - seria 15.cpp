#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class elev
{
    string nume;
public:
    elev(string s=""){nume = s;}
    void afis()const{cout<<nume<<endl;}
///    bool operator<(const elev ob){return this->nume < ob.nume;}
    friend bool operator<(const elev ob1, const elev ob2){return ob1.nume < ob2.nume;}
};

int main()
{
    vector<elev> v;
    v.push_back(elev("ion"));
    v.push_back(elev("ana"));
    v.push_back(elev("george"));
    v.push_back(elev("mircea"));
    v.push_back(elev("lili"));

    for(auto& x : v)
        x.afis();

    cout<<endl<<v.size()<<" "<<v.capacity()<<endl;
    v.shrink_to_fit();
    cout<<endl<<v.size()<<" "<<v.capacity()<<endl;

    v.clear();
    cout<<endl<<v.size()<<" "<<v.capacity()<<endl;


    priority_queue<elev> p;
    p.push(elev("ion"));
    p.push(elev("ana"));
    p.push(elev("george"));
    p.push(elev("mircea"));
    p.push(elev("lili"));

    cout<<endl<<p.size()<<endl;

    while(!p.empty())
    {
        (p.top()).afis();
        p.pop();
    }
    cout<<endl<<p.size()<<endl;

    return 0;
}
/*****************************************************************/
/*
template<class T>
class Test;

template<class T>
istream& operator>>(istream& in, Test<T>& ob){return in>>ob.x;}

template<class T>
class Test
{
    T x;
public:
    void citire(){cin>>x;}
    void afis();
    friend ostream& operator<<(ostream& out, const Test& ob){return out<<ob.x<<endl;}
///    template<class T1> friend istream& operator>>(istream& in, Test<T1>& ob);
    friend istream& operator>> <>(istream& in, Test& ob);
};

template<class T>
void Test<T>::afis(){cout<<x<<endl;}

///template<class T>
///istream& operator>>(istream& in, Test<T>& ob){return in>>ob.x;}

int main()
{
    Test<int> ob1;
///    ob1.citire();
    cin>>ob1;
    cout<<ob1;

    Test<float> ob2;
///    ob2.citire();
    cin>>ob2;
    cout<<ob2;
    return 0;
}
*/
