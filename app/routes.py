from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.scrape import scrape


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            courses = scrape(username, password)
        except Exception as e:
            app.logger.warning("HHA Grades: {}".format(e))
            return render_template('login.html', message="A problem has occurred. Please try again later.")

        if courses is False:
            return render_template('login.html', message="Invalid username or password.")

        return render_template('index.html', courses=courses)
    else:
        return render_template('login.html')

