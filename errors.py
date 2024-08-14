class Garage():
  def __init__(self):
    self.cars=[]

  def __len__(self):
    return len(self.cars)

  def add_car(self,car):
    if not isinstance(car,Car):
      raise TypeError (f'found {car.__class__.__name__} instead of Car')
    self.cars.append(car)

class Car():
  def __init__(self,make,model):
    self.make=make
    self.model=model

ford=Garage()
car=Car('Ford','Fiesta')
ford.add_car(cars)
print(len(ford))

class UncountableError(Exception):
  def __init__(self, number):
      super().__init__(f'Invalid value of n, {number}. n must be greater than 0.')
    #super().__init__(f"Invalid value for n, {wrong_value}. n must be greater than 0.")


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
  if n < 1:
      raise UncountableError(n)
  for x in range(0, n + 1):
      print(x)

#count_from_zero_to_n(-100)

class InvalidNumber(Exception):
  def __init__(self):
    super().__init__('Invalid Number')

raise InvalidNumber