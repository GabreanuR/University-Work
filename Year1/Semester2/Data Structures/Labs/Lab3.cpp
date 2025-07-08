#include <iostream>
#include <vector>

using namespace std;

const int MAX_SIZE = 10;

struct nod{
    int key, value;
    nod *next;
    nod(int key, int value){
        this->key = key;
        this->value = value;
        this->next = NULL;
    }
};

vector<nod*>table(MAX_SIZE, NULL);

int hashK(int key){
    return key % MAX_SIZE;
}
nod* accesare(int key){
    int hashedKey = hashK(key);
    for(nod* it = table[hashedKey]; it != NULL; it=it->next){
        if(it->key == key)
            return it;
    }
    return NULL;
}

void inserare(int key, int value){
    if(accesare(key) != NULL)
        return;
    int hashedKey = hashK(key);
    nod *ins = new nod(key, value);
    ins->next = table[hashedKey];
    table[hashedKey] = ins;
}

void afisare(){
    for(int i = 0; i < MAX_SIZE; i++){
        cout << i << ": ";
        for(nod* it=table[i]; it != NULL; it=it->next){
            cout << "(" << it->key << ", " << it->value << ") ";
        }
        cout << '\n';
    }
}

void stergere(int key){
    if(accesare(key) == NULL)
        return;
    int hashedKey = hashK(key);
    if(table[hashedKey]->key == key){
        nod* cop_next = table[hashedKey]->next;
        delete table[hashedKey];
        table[hashedKey] = cop_next;
        return;
    }
    for(nod* it = table[hashedKey]; it->next != NULL; it=it->next){
        if(it->next->key == key){
            nod* cop_next = it->next;
            it->next= it->next->next;
            delete cop_next;
            return;
        }
    }
}

int main(){
    inserare(2, 7);
    inserare(12, 9);
    inserare(32, 8);
    inserare(22, 10);
    inserare(2147483647, 107);
    afisare();
    stergere(2147483647);
    cout << "dupa stergere: \n\n";
    afisare();
}