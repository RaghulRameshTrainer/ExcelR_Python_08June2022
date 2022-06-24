from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def tyres(self):
        pass
    def price(self):
        return "{}".format(1600000)

class EcoSport(Car):
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def breaks(self):
        self.break_applied="Yes"
    def seats(self):
        self.count="10 seater"
    def engine(self):
        self.engine_type="Petrol engine"
    def tyres(self):
        self.tire="fitted"
    def order(self,cust_name,deposit):
        self.cust_name=cust_name
        self.deposit=deposit
        self.delivery_date="25-08-2022"
c1=EcoSport(2022,"Ford")

print(c1.price())
c1.order('Raghul Ramesh',20000)
print(c1.delivery_date)