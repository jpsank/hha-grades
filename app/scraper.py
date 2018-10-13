import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, username, password):
        self.database = 1160
        self.username = username
        self.password = password

        self.session = requests.session()

    def get(self):
        data = {
            "Database": self.database,
            "LogOnDetails.UserName": self.username,
            "LogOnDetails.Password": self.password
        }
        post = self.session.post("https://hac40.esp.k12.ar.us/HomeAccess40/Account/LogOn", data=data)
        r = self.session.get("https://hac40.esp.k12.ar.us/HomeAccess40/Content/Student/Assignments.aspx")

        soup = BeautifulSoup(r.content, "html.parser")

        courseData = {}
        courses = soup.select(".AssignmentClass")
        for course in courses:
            header = course.select_one(".sg-header")
            name, average = header.select(".sg-header-heading")

            grid = course.select_one(".sg-content-grid")

            courseData[name.text.strip().split('    ')[-1]] = {'average': float(average.text[15:-1]),
                                                               'grid': grid}

        return courseData


