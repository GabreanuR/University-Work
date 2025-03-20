#GABREANU RAZVAN-GEORGE
#%%
class DFA:
    def __init__(self):
        # Definim starile
        self.states = ['q1','q2','q3','q4']
        self.alphabet = ['0','1']
        self.initial_state = 'q1'
        self.final_states = ['q3']
        self.transitions = {
            'q1':{'0':'q2','1':'q3'},
            'q2':{'0':'q1','1':'q4'},
            'q3':{'0':'q4','1':'q1'},
            'q4':{'0':'q3','1':'q2'},
        }
    def process_string(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states
if __name__ == '__main__':
    dfa = DFA()
    test_strings = ["0","1","01","10","101","010","1010","0101"]
    for string in test_strings:
        result = dfa.process_string(string)
        print(f"String {string} is accepted: {result}")
#%%
class NFA:
    def __init__(self):
        # Definim starile
        self.states = ['q1', 'q2', 'q3', 'q4']
        self.alphabet = ['0', '1']
        self.initial_state = 'q1'
        self.final_states = ['q4']
        self.transitions = {
            'q1': {'0': ['q1', 'q2'], '1': ['q1', 'q3']},
            'q2': {'0': [], '1': ['q4']},
            'q3': {'0': ['q4'], '1': []},
            'q4': {'0': [], '1': []},
        }
    def process_string(self, input_string):
        current_state = {self.initial_state}
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            next_states = set()
            for state in current_state:
                if state in self.transitions and symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_state = next_states
            if not current_state:
                return False
        return any(state in self.final_states for state in current_state)

if __name__ == '__main__':
    nfa = NFA()
    test_strings = ["0","1","01","10","101","010","1010","0101"]
    for string in test_strings:
        result = nfa.process_string(string)
        print(f"String {string} is accepted: {result}")