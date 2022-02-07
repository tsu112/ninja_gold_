
from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def index():
    if 'total_gold' and 'activities' not in session:
        session['total_gold'] = 0
        session['activities'] = ""
    return render_template('index.html', messages=session['activities'])


@app.route('/process_money', methods=['POST'])
def process_gold():
    location = request.form['building']
    current_time = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    if location == "farm":
        gold_this_turn = random.randint(10, 20)
    elif location == "cave":
        gold_this_turn = random.randint(5, 10)
    elif location == "house":
        gold_this_turn = random.randint(5, 10)
    else:
        gold_this_turn = random.randint(-50, 50)
    session['total_gold'] += gold_this_turn
    if gold_this_turn >= 0:
        new_message = f"<p class='text-success'>Yay you won {gold_this_turn} gold from {location} {current_time}</p>"
        session['activities'] += new_message
    elif gold_this_turn < 0:
        new_message = f"<p class='text-danger'>Oh no! You lost {gold_this_turn} gold from {location} {current_time}</p>"
        session['activities'] += new_message
    return redirect('/')


@app.route('/reset')
def reset_gold():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
