from flask import Flask, request, jsonify
app = Flask(__name__)


history_file = "history.txt"

def save_history(entry):
    with open(history_file, 'a') as file:
        file.write(entry + '\n')

def load_history():
    history = []
    with open(history_file, 'r') as file:
        for line in file:
            history.append(line.rstrip('\n'))
    return history

@app.route('/')
def index():
    return app.send_static_file('calculator.html')



@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']

    try:
        result = eval(expression)
        entry = f"Expression: {expression}, Result: {result}"
        save_history(entry)
        response = {'status': 'success', 'result': str(result)}
    except Exception as e:
        result = eval(expression)
        entry = f"Expression: {expression}, Result: {result}"
        save_history(entry)
        response = {'status': 'error', 'message': str(e)}

    return jsonify(response)
@app.route('/history', methods=['GET'])
def get_history():
    history = load_history()
    return jsonify(history)

def evaluate_expression(expression):
    # 替换函数名为对应的数学运算函数
    expression = expression.replace('log', 'math.log')
    expression = expression.replace('ln', 'math.log')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')

    # 使用 eval 函数计算表达式结果
    result = eval(expression)

    return result

if __name__ == '__main__':
    app.run()