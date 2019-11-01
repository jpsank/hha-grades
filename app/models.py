

class Course:
    def __init__(self, div):
        header = div.select_one(".sg-header")
        name, average = header.select(".sg-header-heading")

        self.grid = div.select_one(".sg-content-grid")

        self.name = name.text.strip().split('    ')[-1]
        if average.text == '':
            self.average = None
            self.grade = None
        else:
            self.average = float(average.text[15:-1])
            self.grade = 'F' if self.average < 60 \
                else 'D' if self.average < 70 \
                else 'C' if self.average < 80 \
                else 'B' if self.average < 90 \
                else 'A'

    @property
    def has_grade(self):
        return self.average is not None

    def __repr__(self):
        return "<Course {} {} {}>".format(self.name, self.average, self.grade)
