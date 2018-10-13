from app import scraper
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/hha-grades/app/static")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sc = scraper.Scraper(username, password)
        courseData = sc.get()

        mainHTML = u"<section id='main'>"

        for c in courseData:
            grid = courseData[c]['grid'].decode()
            average = courseData[c]['average']

            if average < 60:
                grade = u'F'
            elif average < 70:
                grade = u'D'
            elif average < 80:
                grade = u'C'
            elif average < 90:
                grade = u'B'
            else:
                grade = u'A'

            courseHTML = u"<p class='name'>{}</p>".format(c) + \
                         u"<p class='score'>{}%</p>".format(average) + \
                         u"<p class='grade'>{}</p>".format(grade) + \
                         u"<progress class='{}' value='{}' max='100'></progress>".format(grade, average) + \
                         u"<button class='details'>Details</button>" + \
                         u"<div class='modal'><button class='modal-close'>x</button><div class='content'>{}</div></div>".format(grid)

            mainHTML += u"<div class='course'>{}</div>".format(courseHTML)

        mainHTML += u"</section>"

        return render_template('index.html', main=mainHTML)
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)
