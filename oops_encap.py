class Account():
    def __init__(self,fname,lname,deposit):
        self.fname=fname
        self.lname=lname
        self.__amount=deposit   #protected(_) private(__) public
        self.username="{}{}".format(self.fname,123)
        self.password="{}{}".format(self.fname.title(),'#100')

    def setAmount(self,amt):
        self.__amount=self.__amount+amt

    def getAmount(self):
        return self.__amount
