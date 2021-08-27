
class Student:
    def __init__(self, sn, sid, sy):
        self.sname = sn
        self.sid = sid
        self.syear = sy
        
    def getSName(self):
        return self.sname
    
    def getSid(self):
        return self.sid
    
    def getSYear(self):
        return self.syear
               
    def get_all(self):
        return self.sname, self.sid, self.syear

    def getSYear(self):
        return self.syear
    def setSYear(self, sy):
        
        if type(sy) is str and (sy.lower()=='freshman' or 
                                sy.lower()=='sophomore' or 
                                sy.lower()=='junior' or sy.lower()=='senior'):

                                self.syear = sy
        else:
           print('You have input an invalid value!')
    
        
            
            
 
