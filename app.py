from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vulnerable')
def vulnerable():
    # Introducing a vulnerability by using eval with user input
    user_input = request.args.get('input', '')
    result = eval(user_input)  # This is insecure and should trigger a CodeQL alert
    return f'Result: {result}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
