from flask import Flask, render_template, request, session, redirect, url_for
import datetime
import json
from qclass import Question
from config import Config

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

def get_today_question():
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    with open('questions.json') as f:
        questions = json.load(f)

    for q in questions:
        if q['date'] != today: 
            continue
        return Question(q['question'], q['answer'])

@app.route('/', methods=['GET', 'POST'])
def math_question():
    if 'tries_left' not in session:
        session['tries_left'] = 2 
    
    quesiton = get_today_question()

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        quesiton.check_answer(user_answer)
        return redirect(url_for('math_question'))

    return render_template('question.html', exercise=quesiton)

@app.route('/clear')
def clear_session():
    session.clear()
    return "Session has been cleared!"

@app.route('/session')
def show_session():
    print(session.items())
    return "showing session items!"

if __name__ == '__main__':
    app.run(debug=True)


