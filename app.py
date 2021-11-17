from flask import Flask, request, render_template, flash, jsonify, redirect
from surveys import surveys


app = Flask(__name__)
app.config["SECRET_KEY"] = 'no secret'

responses = []


@app.route('/')
def homepage():
    survey_title = surveys['satisfaction'].title
    survey_instruction = surveys['satisfaction'].instructions
    for val in request.args:
        responses.append(val)
    print(responses)    

    return render_template('homepage.html', title = survey_title, instruction = survey_instruction, redirect = redirect)

@app.route('/question/1')
def show_first_question():
    question1 = surveys['satisfaction'].questions[0].question
    answer = surveys['satisfaction'].questions[0].choices
    yes, no = answer
    return render_template('question1.html', question1 = question1, yes = yes, no = no)

@app.route('/question/2')
def show_second_question():
    question2 = surveys['satisfaction'].questions[1].question
    answer = surveys['satisfaction'].questions[1].choices
    yes, no = answer
    for val in request.args:
        responses.append(val)
    return render_template('question2.html', question2 = question2, yes = yes, no = no)

@app.route('/question/3')
def show_third_question():
    question3 = surveys['satisfaction'].questions[2].question
    answer = surveys['satisfaction'].questions[2].choices
    yes, no = answer
    for val in request.args:
        responses.append(val)
    return render_template('question3.html', question3 = question3, yes = yes, no = no)

@app.route('/question/4')
def show_fourth_question():
    question4 = surveys['satisfaction'].questions[3].question
    answer = surveys['satisfaction'].questions[3].choices
    yes, no = answer
    for val in request.args:
        responses.append(val)
    flash('Thanks for taking the survey with us')
    return render_template('question4.html', question4 = question4, yes = yes, no = no)


