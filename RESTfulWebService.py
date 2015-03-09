from flask import Flask
from flask import render_template
from Fibonacci import Fibonacci
import  os


app = Flask(__name__)
heading_path = os.path.join(os.getcwd(),'static')

# Hello menu
@app.route("/")
def hello():
    return render_template('hello.html')

# Error when input wrong address
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# receive information from clients and return fibonacci string
@app.route("/fibonacci/<numberInput>")
def getFibonacciString(numberInput):
    fibonacci = Fibonacci()
    try:
        num = int(numberInput)
        if  0 < num <= 1000:
            fibonacciString = fibonacci.responseFibonacci(num)
            print(fibonacciString)
        else:
            return render_template('input_error.html')
    except:
        return render_template('input_error.html')
    return render_template('fibonacciString.html', fibonacciString=fibonacciString)

fibonacci = Fibonacci()
fibonacci.calculateFibonacci()

if __name__ == '__main__':
    app.run()
