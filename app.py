from flask import Flask, request, render_template, flash, jsonify, redirect, session
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.config["SECRET_KEY"] = 'no secret'

answer_key = 'answer'

@app.route('/')
def homepage():
    return render_template('homepage.html', survey = survey)

@app.route('/question/1', methods=['POST', 'GET'])
def show_first_question():
    session[answer_key] = []
    return render_template('question1.html', survey = survey)

@app.route('/question/2', methods=['POST', 'GET'])
def show_second_question():
    answers = session[answer_key]
    answers.append(request.form.get('answer'))
    session[answer_key] = answers  
    if (request.form.get('answer') is None):
        return redirect('/question/1')
    return render_template('question2.html', survey = survey)

@app.route('/question/3', methods=['POST', 'GET'])
def show_third_question():
    answers = session[answer_key]
    answers.append(request.form.get('answer'))
    session[answer_key] = answers
    if (request.form.get('answer') is None):
        return redirect('/question/2')
    return render_template('question3.html', survey = survey)

@app.route('/question/4', methods=['POST', 'GET'])
def show_fourth_question():
    answers = session[answer_key]
    answers.append(request.form.get('answer'))
    session[answer_key] = answers
    if (request.form.get('answer') is None):
        return redirect('/question/3')
    return render_template('question4.html', survey = survey)


@app.route('/thanks', methods=['POST', 'GET'])
def thank_user():
    answers = session[answer_key]
    answers.append(request.form.get('answer'))
    session[answer_key] = answers
    if (request.form.get('answer') is None):
        return redirect('/question/4')
    print(session[answer_key])
    flash('survey sucessfully submitted! ')
    return render_template('thanks.html', survey = survey)