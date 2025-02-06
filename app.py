from isArmstrong import isArmstrong,power
from isPrime import isPrime
from isPerfect import isPerfect
from flask import Flask, jsonify, Response
import requests


app = Flask(__name__)


def armstrong(arm):
    if arm is True:
        return ['armstrong']
    return []

def check(number):
    return (number % 2 == 0)

def odd_even(b):
    if check(b) == True:
        return 'even'
    return 'odd'

@app.route('/api/<number>')
def task(number):
    if number.isdigit() is not True:
        r = jsonify({'number':'alphabet', 'error':'true'})
        r.status_code = 400
        return r
    url = "http://numbersapi.com/"+number+"/math"
    t = requests.get(url).text
    number = int(number)
    prop,  d_sum = isArmstrong(number)
    prop = armstrong(prop)
    prop.append(odd_even(number))
    data = {
            'number': number,
            'is_prime': isPrime(number),
            'properties':prop,
            'fun_fact': t, 
            'digit_sum': d_sum,
            'is_perfect': isPerfect(number)
            }
    return jsonify(data)




if __name__ == '__main__':
   app.run(debug = True)
