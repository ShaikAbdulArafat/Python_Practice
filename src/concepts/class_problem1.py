class Student:
    def __init__(self,name,overall_score):
        self.__name = name
        self.__overall_score = overall_score
        self.__clubs = set()
        self.__is_honors_student = False

    def set_stduent_name (self,name):
        self.__name = name

    def set_student_overall_score(self,overall_score):
        self.__overall_score = overall_score
    
    def add_clubs(self,club):
        self.__clubs.add(club)
    
    def set_is_honors_student(self,Is_honor):
        self.__is_honors_student = Is_honor
    
    def print_all(self):
        print(self.__name,self.__overall_score,self.__clubs,self.__is_honors_student)

class College:

    s = Student('Arafat',10)
    s.add_clubs('Yoga')
    s.print_all()
    

