class Animal():
  def __init__(self):
    print('Animal has been created')


class Dog(Animal):
  def __init__(self,name,age):
    Animal.__init__(self)
    #super().__init__()
    print('Dog has been created')
    self.name=name
    self.age=age

  #def age_months(self):
    #return self.age*12
#transforming this into a property as decorator

  @property
  def age_months(self):
    return self.age*12

b=Dog('Bruno',23)
print(b.name)
print(b.age)
#print(b.age_months())
print(b.age_months)
print(b.__class__.__name__)


