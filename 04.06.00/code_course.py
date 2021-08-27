from code_student import *

class Course:
    def __init__(self, cn, cid, sl):
        self.cname = cn
        self.cid = cid
        self.slist = sl
    def getCName (self):
        return self.cname
    def getCid(self):
        return self.cid
    def prinALllStudents(self):
        for i in self.slist:
            print(i.getSName(), i.getSid(), i.getSYear())
    def addStudent(self, st):
        if type(st) is Student:
            for i in self.slist:
                if i is st:
                    print('....')
                    return 
            self.slist.append(st)
        else:   
            print('Sorry, this is not a student!')
