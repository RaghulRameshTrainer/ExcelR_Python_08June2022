class Employee():
    #hike=1.1
    def __init__(self,fname,lname,pay):     #constructor
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gmail.com'

    def fullname(self):
        return "{}.{}".format(self.fname,self.lname)

    def appraisal(self):
        self.hike=2
        #print("Hike for the year is : ", self.hike)
        self.salary = int(self.salary*self.hike)

    @classmethod
    def emp_object(cls,emp_str):
        fn,ln,sal=emp_str.split('-')
        return cls(fn,ln,int(sal))            #Employee(fn,ln,sal)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "Holiday!"
        else:
            return "Working Day!"
class Manager():
    def info(self):
        print("Data Analytics - Python - MySQL")

    def appraisal(self):
        self.hike=3
        #print("Hike for the year is : ", self.hike)
        self.salary = int(self.salary*self.hike)

class Developer(Employee,Manager):
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

    def add_nums(self,*args):
        return sum(args)

    def fullname(self,title):
        return "{}.{} {}".format(title,self.fname,self.lname)

    def appraisal(self):
        super(Employee,self).appraisal()
        #Manager().appraisal(self)

dev_1=Developer('Siva','Murugan',100000,'Python')
dev_2=Developer('Ramya','Karthick',150000,'AIML')
print(dev_1.email)
print(dev_1.add_nums(1,2,3,4,5,6,7,8,9,10))
print(dev_1.fullname('Mr'))
print(dev_2.fullname('Mrs'))
dev_1.info()

print(dev_1.salary)
dev_1.appraisal()
print(dev_1.salary)

#print(help(dev_1))
# Method Overloading is not needed in python
#overriding
#Overloading : two method in the same name in a class is called overloading. both method varies in
#number of arguments or type of the arguments

#overriding : in a parent-child classes, if we redefine the method in child class which exists in
#parent class is called overriding