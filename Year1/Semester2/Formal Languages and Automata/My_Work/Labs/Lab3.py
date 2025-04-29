#GABREANU RAZVAN-GEORGE
#%%
class RegEx:
    def __init__(self):
        # Date initiale

        # EXEMPLU LABORATOR 2

        # self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
        # self.alphabet = ['f', 'd', 'p', 'r', 'v', 'e']
        # self.initial_state = 'q0'
        # self.final_states = ['q6']
        # self.transitions = {
        #     'q0': {'lambda': ['q2', 'q3'], 'f': ['q1'], 'd': [], 'p': [], 'r': [], 'v': [], 'e': []},
        #     'q1': {'lambda': ['q4'], 'f': ['q2'], 'd': ['q3'], 'p': [], 'r': [], 'v': [], 'e': []},
        #     'q2': {'lambda': [], 'f': ['q3', 'q5'], 'd': [], 'p': ['q4'], 'r': [], 'v': [], 'e': []},
        #     'q3': {'lambda': [], 'f': ['q2', 'q4'], 'd': ['q5'], 'p': [], 'r': [], 'v': [], 'e': []},
        #     'q4': {'lambda': [], 'f': ['q5'], 'd': [], 'p': ['q6'], 'r': ['q0'], 'v': [], 'e': []},
        #     'q5': {'lambda': [], 'f': [], 'd': [], 'p': [], 'r': [], 'v': ['q6'], 'e': ['q3', 'q1']},
        #     'q6': {'lambda': ['q0'], 'f': [], 'd': [], 'p': [], 'r': [], 'v': ['q4'], 'e': []}
        # }

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

        # EXEMPLU LABORATOR 3

        self.states = ['q0', 'q1', 'q2', 'q3', 'q4']
        self.alphabet = ['a', 'b', 'c']
        self.initial_state = 'q0'
        self.final_states = ['q3','q4']
        self.transitions = {
            'q0': {'lambda': [], 'a' : ['q1'], 'b' : ['q0'], 'c' : ['q2']},
            'q1': {'lambda': [], 'a' : ['q3'], 'b' : ['q1'], 'c' : ['q1']},
            'q2': {'lambda': [], 'a' : ['q4'], 'b' : ['q4'], 'c' : []},
            'q3': {'lambda': [], 'a' : [], 'b' : [], 'c' : []},
            'q4': {'lambda': [], 'a' : [], 'b' : [], 'c' : []}
        }

        # Date calculate

        self.new_init_state = 'qP'
        self.new_final_state = 'qF'
        self.transition_regex = {}

        # Functii pentru calculare

        self.prepare_transitions()

    def prepare_transitions(self):
        for state in self.states:
            self.transition_regex[state] = {}

            for symbol, destinations in self.transitions[state].items():
                regex_symbol = "L" if symbol == 'lambda' else symbol
                for dest in destinations:
                    if dest not in self.transition_regex[state]:
                        self.transition_regex[state][dest] = regex_symbol
                    else:
                        self.transition_regex[state][dest] += "|" + regex_symbol

        self.transition_regex[self.new_init_state] = {self.initial_state: "L"}
        for final_state in self.final_states:
            if final_state in self.transition_regex:
                self.transition_regex[final_state][self.new_final_state] = "L"
            else:
                self.transition_regex[final_state] = {self.new_final_state: "L"}

    def eliminate_state(self, state):
        if state in [self.new_init_state, self.new_final_state]:
            return

        loop_regex = f"({self.transition_regex[state].pop(state)})*" if state in self.transition_regex[state] else ""

        incoming = []
        for src in self.transition_regex:
            if state in self.transition_regex[src]:
                incoming.append((src,self.transition_regex[src][state]))
        outgoing = [(symbol, dst) for dst, symbol in self.transition_regex[state].items()]

        for i in range(len(outgoing)):
            if '(' not in outgoing[i][0] and '|' in outgoing[i][0]:
                outgoing[i] = ('(' + outgoing[i][0] + ')', outgoing[i][1])

        del self.transition_regex[state]

        for (src, in_symbol) in incoming:
            self.transition_regex[src].pop(state)
            for (out_symbol, dst) in outgoing:
                new_regex = f"{in_symbol}{loop_regex}{out_symbol}"

                if dst in self.transition_regex[src]:
                    self.transition_regex[src][dst] += "|(" + new_regex + ")"
                else:
                    self.transition_regex[src][dst] = "(" + new_regex + ")"

    def post_processing(self, string):
        cnt = string.count("L")
        while cnt:
            string = string.replace("L", "")
            cnt -= 1

        i = 1
        while i < len(string):
            if string[i] == "|" and string[i - 1] == "(":
                string = string[:i] + string[i + 1:]
                i = i - 1
            i = i + 1

        while "(())" in string:
            string = string.replace("(())", "")
        while "()" in string:
            string = string.replace("()", "")

        i = len(string) - 1
        while i > 1:
            if string[i] == ')' and string[i - 2] == '(':
                if i + 1 < len(string):
                    string = string[:i] + string[i + 1:]
                else:
                    string = string[:i]
                string = string[: i - 2] + string[i - 1:]
                i -= 2
            i -= 1

        i = 0
        while i < len(string) - 2:
            if string[i] != ")" and string[i] != "(" and string[i] == string[i + 2] and string[i + 1] == '*':
                string = string[: i + 1] + '+' + string[i + 3:]
                i = 0
            else:
                i += 1

        i = len(string) - 1
        while i > 3:
            if string[i] == ")" and string[i - 1] == ")" and string[i - 3] == "(" and string[i - 4] == "(":
                if i + 1 < len(string):
                    string = string[:i - 1] + string[i + 1:]
                else:
                    string = string[:i - 1] + ""
                string = string[:i - 4] + string[i - 2:]
                i = i - 4
            i -= 1

        i = len(string) - 1
        while i > 4:
            if string[i] == ")" and string[i - 1] == ")" and string[i - 4] == "(" and string[i - 5] == "(":
                if i + 1 < len(string):
                    string = string[:i] + string[i + 1:]
                else:
                    string = string[:i] + ""
                string = string[:i - 5] + string[i - 4:]
                i = i - 3
            i -= 1

        i = len(string) - 2
        while i > 3:
            if string[i] == ")" and string[i - 2] in "+*" and string[i - 4] == "(" and string[i + 1] not in "*+":
                if i + 1 < len(string):
                    string = string[:i] + string[i + 1:]
                else:
                    string = string[:i] + ""
                string = string[:i - 4] + string[i - 3:]
                i = i - 2
            i -= 1

        i = 1
        while i < len(string):
            if string[i] == "|" and string[i - 1] == "(":
                string = string[:i] + string[i + 1:]
                i = i - 1
            i = i + 1

        return string

    def transformation(self):
        for state in list(self.states):
            self.eliminate_state(state)

        mid_regex = self.transition_regex[self.new_init_state][self.new_final_state]
        print("\nFunctional Regular Expression:", mid_regex)

        final_regex = self.post_processing(mid_regex)

        return final_regex

class Automata:
    def __init__(self):
        # Date initiale

        self.RegEx = "((b*a(b|c)*a))|((b*c(a|b)))"
        self.state_counter = 0
        self.operators = {'|', '*', '.'}
        self.precedence = {'*': 3, '.': 2, '|': 1}
        self.step = 1

        # Date calculate

        self.RegEx_standardized = ""
        self.Postfix = ""
        self.state_ids = {}  # Maps state objects to IDs

        # Functii pentru calculare

        self.add_concatenation_operators(self.RegEx)
        self.regex_to_postfix(self.RegEx_standardized)
        self.nfa = self.build_nfa()
        self.print_final_nfa()

    class State:
        def __init__(self):
            self.transitions = {}
            self.L = []

    class NFA:
        def __init__(self, start, accept):
            self.start = start
            self.accept = accept

    def new_state(self):
        state = self.State()
        self.state_ids[state] = self.state_counter
        self.state_counter += 1
        return state

    def get_id(self, state):
        return self.state_ids[state]

    def print_final_nfa(self):
        print("\n=== FINAL NFA ===")
        print("All Transitions:")

        for state in sorted(self.state_ids.keys(), key=lambda s: self.get_id(s)):

            for char, targets in state.transitions.items():
                for target in targets:
                    print(f"q{self.get_id(state)} --{char}--> q{self.get_id(target)}")

            for target in state.L:
                print(f"q{self.get_id(state)} --L--> q{self.get_id(target)}")

        print(f"\nStart state: q{self.get_id(self.nfa.start)}")
        print(f"Accept state: q{self.get_id(self.nfa.accept)}")

    def add_concatenation_operators(self, regex):
        new_regex = ""
        prev = None

        for curr in regex:
            if (prev and
                    ((prev.isalnum() and (curr.isalnum() or curr == '(')) or
                     (prev == ')' and (curr.isalnum() or curr == '(')) or
                     (prev == '*' and (curr.isalnum() or curr == '(')))):
                new_regex += '.'
            new_regex += curr
            prev = curr

        self.RegEx_standardized = new_regex
        print("Standardized regex:", new_regex)
        return new_regex

    def regex_to_postfix(self, regex):
        precedence = {'*': 4, '.': 3, '|': 2}
        output = []
        operators = []

        i = 0
        while i < len(regex):
            c = regex[i]

            if c.isalnum():
                output.append(c)
            elif c == '(':
                operators.append(c)
            elif c == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '('
            elif c in precedence:
                while (operators and operators[-1] != '(' and
                       precedence[operators[-1]] >= precedence[c]):
                    output.append(operators.pop())
                operators.append(c)
            i += 1

        while operators:
            output.append(operators.pop())

        self.Postfix = ''.join(output)
        print("Postfix notation:", self.Postfix)

    def basic_nfa(self, char):
        s1 = self.new_state()
        s2 = self.new_state()
        s1.transitions[char] = [s2]
        return self.NFA(s1, s2)

    def concat_nfas(self, a, b):
        a.accept.L.append(b.start)
        return self.NFA(a.start, b.accept)

    def union_nfas(self, a, b):
        s = self.new_state()
        e = self.new_state()
        s.L = [a.start, b.start]
        a.accept.L.append(e)
        b.accept.L.append(e)
        return self.NFA(s, e)

    def star_nfa(self, nfa):
        new_start = self.new_state()
        new_accept = self.new_state()
        new_start.L.extend([nfa.start, new_accept])
        nfa.accept.L.extend([nfa.start, new_accept])
        return self.NFA(new_start, new_accept)

    def build_nfa(self):
        postfix = self.Postfix

        stack = []
        for c in postfix:
            if c.isalnum():
                stack.append(self.basic_nfa(c))
            elif c == '.':
                right = stack.pop()
                left = stack.pop()
                stack.append(self.concat_nfas(left, right))
            elif c == '|':
                right = stack.pop()
                left = stack.pop()
                stack.append(self.union_nfas(left, right))
            elif c == '*':
                nfa = stack.pop()
                stack.append(self.star_nfa(nfa))

        return stack.pop()

if __name__ == "__main__":
    print("EX 1: ")
    proc = RegEx()
    RegEx = proc.transformation()
    print("\nFinal Regular Expression:", RegEx)
    print("\nEX 2: \n")
    automata = Automata()
