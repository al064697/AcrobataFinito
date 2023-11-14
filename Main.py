import matplotlib.pyplot as plt
import networkx as nx

class AutomataPrintfV3:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'}
        self.alphabet = {'p', 'r', 'i', 'n', 't', 'f', '(', ')', ';'}
        self.transitions = {
            'q0': {'p': 'q1'},
            'q1': {'r': 'q2'},
            'q2': {'i': 'q3'},
            'q3': {'n': 'q4'},
            'q4': {'t': 'q5'},
            'q5': {'f': 'q6'},
            'q6': {'(': 'q7'},
            'q7': {')': 'q8'},
            'q8': {';': 'q9'},
            'q9': {},  # Estado de aceptación
        }
        self.current_state = 'q0'

    def process_input(self, input_str):
        for symbol in input_str:
            if symbol in self.alphabet:
                if symbol in self.transitions[self.current_state]:
                    self.current_state = self.transitions[self.current_state][symbol]
                else:
                    # Estado de reinicio en caso de símbolo no permitido
                    self.current_state = 'q0'
                    break
            else:
                # Estado de reinicio en caso de símbolo no perteneciente al alfabeto
                self.current_state = 'q0'
                break
        return self.current_state == 'q9'


def draw_automaton_v3():
    automata = AutomataPrintfV3()

    G = nx.DiGraph()
    G.add_nodes_from(automata.states)

    for from_state, transitions in automata.transitions.items():
        for symbol, to_state in transitions.items():
            G.add_edge(from_state, to_state, label=symbol)

    pos = nx.spring_layout(G)
    labels = {state: state for state in automata.states}
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos, labels)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title('Automata for printf(); (V3)')
    plt.show()

# Generar la ilustración del tercer autómata
draw_automaton_v3()
