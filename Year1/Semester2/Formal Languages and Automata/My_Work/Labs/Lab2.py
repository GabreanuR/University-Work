#GABREANU RAZVAN-GEORGE
#%%
class lambdaNFAtoDFAdict:
    def __init__(self):
        # Definim starile
        self.states = ['q1', 'q2', 'q3', 'q4','q5','q6']
        self.alphabet = ['f', 'd','p','r','v','e']
        self.initial_state = 'q1'
        self.final_states = ['q6']
        self.transitions = {
            'q0': {'lambda':['q1','q2','q3'],'f':[], 'd':[],'p':[],'r':[],'v':[],'e':[]},
            'q1': {'lambda':['q4'],'f':['q2'], 'd':['q3'],'p':[],'r':[],'v':[],'e':[]},
            'q2': {'lambda':[],'f':['q3','q5'], 'd':[],'p':['q4'],'r':[],'v':[],'e':[]},
            'q3': {'lambda':[],'f':['q2','q4'], 'd':['q5'],'p':[],'r':[],'v':[],'e':[]},
            'q4': {'lambda':[],'f':['q5'], 'd':[],'p':['q6'],'r':['q0'],'v':[],'e':[]},
            'q5': {'lambda':[],'f':[], 'd':[],'p':[],'r':[],'v':[],'e':['q3','q1']},
            'q6': {'lambda':['q0'],'f':[], 'd':[],'p':[],'r':[],'v':['q4'],'e':[]}
        }
        self.lambdaNFAtoNFAdict = {}
        self.NFAtoDFAdict = {}
    def lambdaNFAtoNFA(self):
        return
    def NFAtoDFA(self):
        resultat_partial = proc.lambdaNFAtoNFA()
        return resultat_partial

if __name__ == '__main__':
    proc = lambdaNFAtoDFAdict()     # Clasa
    print(proc.NFAtoDFA())          # Procesul efectiv