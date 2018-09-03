from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/q1')
def render_q1():
    return render_template('q1.html')

@app.route('/q2')
def render_q2():
    return render_template('q2.html')

@app.route('/q3')
def render_q3():
    return render_template('q3.html')

@app.route('/q4')
def render_q4():
    return render_template('q4.html')

@app.route('/q5')
def render_q5():
    return render_template('q5.html')

@app.route('/q6')
def render_q6():
    return render_template('q6.html')

@app.route('/q7')
def render_q7():
    return render_template('q7.html')

@app.route('/q8')
def render_q8():
    return render_template('q8.html')

@app.route('/q9')
def render_q9():
    return render_template('q9.html')

@app.route('/q10')
def render_q10():
    return render_template('q10.html')


if __name__ == "__main__":
    app.run(debug = True)
