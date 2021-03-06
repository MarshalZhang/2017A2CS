class Assessment:
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
    def OutputAssessmentDetails(self):
        print(self.__AssessmentTitle, " Marks: ",self.__MaxMarks)

class Course:
    def __init__ (self, t, m): 
        self.CourseTitle = t
        self.MaxStudents = m
        self.NumberOfLessons = 0
        self.CourseLesson = []
        self.CourseAssessment = Assessment

    def AddLesson(self,t,d,r):
        self.NumberOfLessons = self.NumberOfLessons + 1
        self.CourseLesson .append(Lesson (t,d,r))

    def AddAssessment(self,t,m):
        self. CourseAssessment = Assessment(t,m)
        
    def OutputCourseDetails (self):
        print(self.CourseTitle, "Maximum number: " ,self.MaxStudents)
        for i in range(self.NumberOfLessons):
            print(self.CourseLesson[i].OutputLessonDetails ())

class Lesson:
    def __init__(self, t, d, r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__requiresLab = r
    def OutputLessonDetails(self):
        print(self.__LessonTitle, self.__DurationMinutes)
        
def Main():
    MyCourse= Course("Computing", 10) 
    MyCourse.AddAssessment("Programming", 100) 
    MyCourse.AddLesson("Problem Solving", 60, False)
    MyCourse.AddLesson("Programming", 120, True)
    MyCourse.AddLesson("Theory", 60, False)
    MyCourse.OutputCourseDetails()

Main()
