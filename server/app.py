from flask import Flask

app = Flask(__name__)

# Index Route: /
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string in the console and display it in the browser
# URL format: /print/<parameter>
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string to the console
    return parameter  # Return the string without HTML tags

# Route to display all numbers in the range of the parameter
# URL format: /count/<parameter>
@app.route('/count/<int:parameter>')
def count(parameter):
    # Adjust range to start from 0 and include numbers up to parameter-1
    numbers = [str(i) for i in range(parameter)]
    return '\n'.join(numbers) + '\n'  # Add a trailing newline

# Route to perform basic mathematical operations
# URL format: /math/<num1>/<operation>/<num2>
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Unsupported operation!'
    
    return str(result)  # Return only the result as a string

if __name__ == '__main__':
    app.run(debug=True)
