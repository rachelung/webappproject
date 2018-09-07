
from flask import Flask, render_template, request
app = Flask(__name__)

ansA = 0
ansB = 0
ansC = 0

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/q1')
def render_q1():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
        print (ansA) 
    if 'B' in request.args:
        ansB += 1
        print(ansB)
    if 'C' in request.args:
        ansC += 1
        print(ansC)
    return render_template('q1.html')

@app.route('/q2')
def render_q2():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
        print(ansA)
    if 'B' in request.args:
        ansB += 1
        print(ansB)
    if 'C' in request.args:
        ansC += 1
        print(ansC)
    return render_template('q2.html')

@app.route('/q3')
def render_q3():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q3.html')

@app.route('/q4')
def render_q4():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q4.html')

@app.route('/q5')
def render_q5():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q5.html')

@app.route('/q6')
def render_q6():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q6.html')

@app.route('/q7')
def render_q7():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q7.html')

@app.route('/q8')
def render_q8():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q8.html')

@app.route('/q9')
def render_q9():
    global ansA, ansB, ansC
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q9.html')

@app.route('/q10')
def render_q10():
    global ansA, ansB, ansC

    print(ansA)
    print(ansB)
    print(ansC)
    
    if 'A' in request.args:
        ansA += 1
    if 'B' in request.args:
        ansB += 1
    if 'C' in request.args:
        ansC += 1
    return render_template('q10.html')

@app.route("/result")
def result():
    global ansA, ansB, ansC
    print(ansA)
    print(ansB)
    print(ansC)
    if ansA > ansB and ansA > ansC:
        return render_template('resultA.html')
    if ansB > ansA and ansB > ansC:
        return render_template('resultB.html')
    if ansC > ansB and ansC > ansA:
        return render_template('resultC.html')


if __name__ == "__main__":
    app.run(debug = True)
