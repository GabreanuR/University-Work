#GABREANU RAZVAN-GEORGE
#%%
class lambdaNFAtoDFAdict:
    def __init__(self):
        # Date initiale

        # EXEMPLU LABORATOR

        self.states = ['q0','q1', 'q2', 'q3', 'q4','q5','q6']
        self.alphabet = ['f', 'd','p','r','v','e']
        self.initial_state = 'q0'
        self.final_states = ['q6']
        self.transitions = {
            'q0': {'lambda':['q2','q3'],'f':['q1'], 'd':[],'p':[],'r':[],'v':[],'e':[]},
            'q1': {'lambda':['q4'],'f':['q2'], 'd':['q3'],'p':[],'r':[],'v':[],'e':[]},
            'q2': {'lambda':[],'f':['q3','q5'], 'd':[],'p':['q4'],'r':[],'v':[],'e':[]},
            'q3': {'lambda':[],'f':['q2','q4'], 'd':['q5'],'p':[],'r':[],'v':[],'e':[]},
            'q4': {'lambda':[],'f':['q5'], 'd':[],'p':['q6'],'r':['q0'],'v':[],'e':[]},
            'q5': {'lambda':[],'f':[], 'd':[],'p':[],'r':[],'v':['q6'],'e':['q3','q1']},
            'q6': {'lambda':['q0'],'f':[], 'd':[],'p':[],'r':[],'v':['q4'],'e':[]}
        }

        # EXEMPLU SEMINAR

        # self.states = ['q0','q1', 'q2', 'q3', 'q4','q5','q6']
        # self.alphabet = ['a','b']
        # self.initial_state = 'q0'
        # self.final_states = ['q2','q6']
        # self.transitions = {
        #     'q0': {'lambda':['q2','q3'],'a':['q0','q1'], 'b':['q2']},
        #     'q1': {'lambda':['q2'],'a':[], 'b':[]},
        #     'q2': {'lambda':['q4'],'a':['q3'], 'b':[]},
        #     'q3': {'lambda':['q5'],'a':['q6'], 'b':['q3','q6']},
        #     'q4': {'lambda':['q6'],'a':['q6'], 'b':['q5']},
        #     'q5': {'lambda':['q2','q6'],'a':['q6'], 'b':['q2']},
        #     'q6': {'lambda':[],'a':[], 'b':['q6']},
        # }

        # Date calculate

        self.lambda_closure_dict = {}
        self.nfa_transitions = {}
        self.dfa_transitions = {}

        # Functii pentru calculare

        self.compute_lambda_closures()
        self.convert_lambda_nfa_to_nfa()
        self.convert_nfa_to_dfa()
        self.print_NFA()
        self.print_DFA()

    def lambda_closure(self, state):
        closure = {state}
        stack = [state]

        while stack:
            current = stack.pop()
            if 'lambda' in self.transitions[current]:
                for next_state in self.transitions[current]['lambda']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)

        return closure

    def compute_lambda_closures(self):
        for state in self.states:
            self.lambda_closure_dict[state] = self.lambda_closure(state)

    def convert_lambda_nfa_to_nfa(self):
        for state in self.states:
            self.nfa_transitions[state] = {symbol : set() for symbol in self.alphabet}

            for symbol in self.alphabet:
                reachable_states = set()

                for lambda_state in self.lambda_closure_dict[state]:
                    for next_state in self.transitions[lambda_state][symbol]:
                        reachable_states.update(self.lambda_closure_dict[next_state])

                self.nfa_transitions[state][symbol] = reachable_states

    def convert_nfa_to_dfa(self):
        new_initial_state = frozenset(self.lambda_closure_dict[self.initial_state])
        new_initial_name = "q" + "".join(sorted(state[1:] for state in new_initial_state))
        stack = [new_initial_state]

        dfa_states = {new_initial_state: new_initial_name}
        self.dfa_transitions[new_initial_name] = {symbol: [] for symbol in self.alphabet}

        while stack:
            current_dfa_state = stack.pop()
            current_dfa_name = dfa_states[current_dfa_state]

            self.dfa_transitions[current_dfa_name] = {symbol: [] for symbol in self.alphabet}

            for symbol in self.alphabet:
                new_state = set()
                for nfa_state in current_dfa_state:
                    new_state.update(self.nfa_transitions[nfa_state][symbol])

                new_state = frozenset(new_state)

                if new_state:
                    new_dfa_name = "q" + "".join(sorted(state[1:] for state in new_state))

                    if new_state not in dfa_states:
                        dfa_states[new_state] = new_dfa_name
                        stack.append(new_state)
                        self.dfa_transitions[new_dfa_name] = {symbol: [] for symbol in self.alphabet}

                    self.dfa_transitions[current_dfa_name][symbol] = new_dfa_name

        self.dfa_final_states = {dfa_name for nfa_set, dfa_name in dfa_states.items()
                                 if any(state in self.final_states for state in nfa_set)}

    def print_NFA(self):
        print(f"\nTabela de tranzitie de la Lambda-NFA la NFA:\n")

        aux_stare = 0
        for state in self.states:
            if len(state) > aux_stare:
                aux_stare = len(state)
        aux_stare += 2

        aux_alphabet = len(self.states) * aux_stare

        # Tavanul tabelului
        print("#"*(aux_stare+2),end="")
        for i in range(len(self.alphabet)):
            print("#"*(aux_alphabet-6),end="")
            print("#",end="")
        print()

        print("#",end="")
        print(" "*aux_stare,end="")
        print("#",end="")
        for symbol in self.alphabet:
            print(symbol.center(aux_alphabet-6),end="")
            print("#",end="")
        print()

        print("#" * (aux_stare + 2), end="")
        for i in range(len(self.alphabet)):
            print("#" * (aux_alphabet-6), end="")
            print("#", end="")
        print()

        # Tabel Propriu-zis

        for state in self.nfa_transitions:

            print("#", end="")
            print(state.center(aux_stare), end="")
            print("#", end="")

            for symbol in self.nfa_transitions[state]:
                L = list(self.nfa_transitions[state][symbol])
                L.sort()
                print("|".join(L).center(aux_alphabet-6), end="")
                print("#",end="")
            print()

            print("#" * (aux_stare + 2), end="")
            for i in range(len(self.alphabet)):
                print("#" * (aux_alphabet-6), end="")
                print("#", end="")
            print()
        return

    def print_DFA(self):
        print(f"\nTabela de tranzitie de la NFA la DFA:\n")

        aux_stare = len(self.states) + 3

        aux_alphabet = aux_stare * 2

        # Tavanul tabelului
        print("#"*(aux_stare+2),end="")
        for i in range(len(self.alphabet)):
            print("#"*(aux_alphabet-6),end="")
            print("#",end="")
        print()

        print("#",end="")
        print(" "*aux_stare,end="")
        print("#",end="")
        for symbol in self.alphabet:
            print(symbol.center(aux_alphabet-6),end="")
            print("#",end="")
        print()

        print("#" * (aux_stare + 2), end="")
        for i in range(len(self.alphabet)):
            print("#" * (aux_alphabet-6), end="")
            print("#", end="")
        print()

        # Tabel Propriu-zis

        for state in self.dfa_transitions:

            print("#", end="")
            print(state.center(aux_stare), end="")
            print("#", end="")

            for symbol in self.dfa_transitions[state]:
                if self.dfa_transitions[state][symbol]:
                    print(self.dfa_transitions[state][symbol].center(aux_alphabet - 6), end="")

                else:
                    print(" ".center(aux_alphabet - 6), end="")
                print("#",end="")
            print()

            print("#" * (aux_stare + 2), end="")
            for i in range(len(self.alphabet)):
                print("#" * (aux_alphabet-6), end="")
                print("#", end="")
            print()

#%%
#LEMA DE POMPARE
class LP:
    def __init__(self):
        # Date initiale

        self.test = "aaabbb"
        self.p = 3

        # Date calculate

        self.pumped_strings = []

        # Functii pentru calculare

        self.pumped_strings = self.PumpingLemmaRegular(self.test,self.p)
        self.print_result(self.pumped_strings)

    def PumpingLemmaRegular(self, test, p):
        if len(test) < p:
            return [self.test]

        results = []

        for i in range(1,p+1):
            xy = test[:i]
            z = test[i:]
            for j in range(len(xy)):
                x = xy[:j]
                y = xy[j:]
                for k in range(5):
                    xyz = x + y * k + z
                    results.append((x,y,z,k,xyz))

        return results

    def IsAnBn(self, string):
        ok = -1
        aux = 0
        i = 0
        for i in range(len(string)):
            if string[i] != 'a':
                aux = i
                break
            else:
                ok = 0
        aux2 = -1
        for j in range(i, len(string)):
            if string[j] != 'b':
                aux2 = j
                break
        else:
            if aux2 == -1 and ok != -1 and aux == len(string)/2 :
                return True
        return False

    def print_result(self, pumped_strings):
        for x, y, z, k, pumped in pumped_strings:
            print(f"x = {x}, y = {y}, z = {z}, k = {k}")
            print(f"Pumped strings: {pumped}")
            print(f"Is in language: {self.IsAnBn(pumped)}\n")


if __name__ == "__main__":
    print("\nEX 1: ")
    proc = lambdaNFAtoDFAdict()
    print("\nEX 2: \n")
    process = LP()