class student:
    def __init__(self, Name, major, gpa):
        self.Name = Name
        self.major = major
        self.gpa = gpa


    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
