#include <iostream>

using namespace std;

template<class T>
class Baza
{
public:
    void afis(){cout<<"T\n";}
};

class Derivata1 : public Baza<float> /// derivata nontemplate dintr-o clasa instantiata dintr-un template
{
public:
 ///   void afis(){cout<<"D1 - Float\n";}
};

class Test_nontemplate
{
public:
    void afis(){cout<<"baza non-template\n";}
};

template<class T>
class Derivata2 : public Test_nontemplate
{
public:
    void afis(){cout<<"deriv template din non-template\n";}
};

/*
template<>
class Derivata2<int> : public Test_nontemplate
*/

/// merge si fara :
template<>
class Derivata2<int>
{
    public:
    void afis(){cout<<"deriv 2 int\n";}
};

int main()
{
    /// Derivata1<float> ob; /// pt ca non-template
    Derivata1 ob;
    ob.afis();

    Derivata2<int> ob2;
    ob2.afis();
    return 0;
}
