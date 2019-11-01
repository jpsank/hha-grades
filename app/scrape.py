from app import app
import requests
from bs4 import BeautifulSoup
from app.models import Course

session = requests.session()


def scrape(username, password):
    form_data = {
        "Database": app.config["HHA_DB_NUMBER"],
        "LogOnDetails.UserName": username,
        "LogOnDetails.Password": password
    }
    post = session.post("https://hac40.esp.k12.ar.us/HomeAccess40/Account/LogOn", data=form_data)
    r = session.get("https://hac40.esp.k12.ar.us/HomeAccess40/Content/Student/Assignments.aspx")

    soup = BeautifulSoup(r.content, "html.parser")

    course_divs = soup.select(".AssignmentClass")
    if len(course_divs) == 0:
        return False

    courses = []
    for course_div in course_divs:
        courses.append(Course(course_div))

    return courses


