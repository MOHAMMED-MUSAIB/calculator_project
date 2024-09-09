from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Extract input from the form
    num1 = float(request.form.get('num1', 0))
    operation = request.form.get('operation', '')
    
    # Perform the selected operation
    result = None
    if operation == 'add':
        num2 = float(request.form.get('num2', 0))
        result = num1 + num2
    elif operation == 'subtract':
        num2 = float(request.form.get('num2', 0))
        result = num1 - num2
    elif operation == 'multiply':
        num2 = float(request.form.get('num2', 0))
        result = num1 * num2
    elif operation == 'divide':
        num2 = float(request.form.get('num2', 0))
        result = num1 / num2 if num2 != 0 else 'Undefined'
    elif operation == 'sin':
        result = math.sin(math.radians(num1))
    elif operation == 'cos':
        result = math.cos(math.radians(num1))
    elif operation == 'tan':
        result = math.tan(math.radians(num1))
    elif operation == 'log':
        result = math.log(num1)
    elif operation == 'exp':
        result = math.exp(num1)
    elif operation == 'sqrt':
        result = math.sqrt(num1)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)