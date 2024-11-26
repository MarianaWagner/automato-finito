from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class TurnstileAutomaton:
    def __init__(self):
        self.states = ['Travada', 'Destravada', 'Alerta']
        self.initial_state = 'Travada'
        self.current_state = self.initial_state
        self.transitions = {
            'Travada': {
                'Pagamento': 'Destravada',
                'Passar': 'Alerta'
            },
            'Destravada': {
                'Passar': 'Travada',
                'Pagamento': 'Destravada'  # Permanece destravada
            },
            'Alerta': {
                'Reset': 'Travada',
                'Pagamento': 'Alerta',
                'Passar': 'Alerta'
            }
        }

    def process_input(self, input_symbol):
        if input_symbol in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][input_symbol]
            return {'state': self.current_state, 'message': self.get_message(input_symbol)}
        else:
            return {'state': self.current_state, 'message': f"Ação '{input_symbol}' não é válida no estado '{self.current_state}'."}

    def get_message(self, action):
        if self.current_state == 'Alerta':
            return "Tentativa inválida detectada! Catraca em estado de alerta."
        elif action == 'Passar' and self.current_state == 'Travada':
            return "A catraca está travada. Efetue o pagamento."
        elif action == 'Pagamento' and self.current_state == 'Destravada':
            return "Pagamento recebido. Você já pode passar."
        else:
            return f"Ação '{action}' realizada com sucesso."

# Instanciando o autômato
automaton = TurnstileAutomaton()

@app.route('/')
def index():
    return render_template('index.html', state=automaton.current_state)

@app.route('/action', methods=['POST'])
def action():
    data = request.get_json()
    input_symbol = data.get('action')
    result = automaton.process_input(input_symbol)
    return jsonify(result)

@app.route('/simulate', methods=['POST'])
def simulate():
    possible_actions = ['Pagamento', 'Passar', 'Passar', 'Pagamento']
    action = random.choice(possible_actions)
    result = automaton.process_input(action)
    result['action'] = action
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
