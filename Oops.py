Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    def _init_(self):
        self.brand="Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=Car()
car
<__main__.Car object at 0x000002EEA0D1C710>
car.brand
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    car.brand
AttributeError: 'Car' object has no attribute 'brand'
car.brand
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    car.brand
AttributeError: 'Car' object has no attribute 'brand'
Car.brand
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Car.brand
AttributeError: type object 'Car' has no attribute 'brand'
class Car:
    def __init__(self):
        self.brand="Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=Car()
SyntaxError: invalid syntax
class Car:
    def __init__(self):
        self.brand="Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=Car()
car.brand
'Suzuki'
car.color
'Blue'
car.top_speed
200


class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts

        
car=Car("Maruti","Black",150)
car.brand
'Maruti'
car=Car("Tata","Grey",225)
car.brand
'Tata'

class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate():
        print("Your car top speed is:",self.top_speed)

        
car=Car("Tata","Grey",225)
car
<__main__.Car object at 0x000002EEA08276E0>

'

class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate(self):
        print("Your car top speed is:",self.top_speed)
        
SyntaxError: unterminated string literal (detected at line 1)

class Car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate(self):
        print("Your car top speed is:",self.top_speed)
        

car=Car("Tata","Grey",225)
car.accelerate()
Your car top speed is: 225

class Dog:
    def __init__(self,n,a,ts)
    
SyntaxError: expected ':'



class Dog:
    def __init__(self,n,a,ts):
        self.name=n
        self.age=a
        self.top_speed=ts
    def accelerate(self):
        print("Your Dog top speed is:",self.top_speed)

        
dog=Dog("Popy","Tomy",120)
dog.accelerate()
Your Dog top speed is: 120

class watch:
    def __init__(self,b,c,p):
        self.brand=b
        self.color=c
        self.price=p
    def accelerate(self):
        print("Price of Watch is:",self.price)

        
watch=Watch("Sonata","Black",1450)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    watch=Watch("Sonata","Black",1450)
NameError: name 'Watch' is not defined. Did you mean: 'watch'?

class Watch:
    def __init__(self,b,c,p):
        self.brand=b
        self.color=c
        self.price=p
    def accelerate(self):
        print("Price of Watch is:",self.price)

        
watch=Watch("Sonata","Black",1450)
watch.accelerate()
Price of Watch is: 1450

class College:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self)
...     
SyntaxError: expected ':'
>>> 
>>> KeyboardInterrupt
>>> 
>>> 
... 
... class College:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self):
...         print(self.name+ "is present at "+self.loc)
... 
...         
>>> class Department(College):
...     def __init__(self,name,ids):
...         sself.id=ids
... 
...         
>>> college=College("GEC Vaishali","Vaishali")
>>> college.departmnet
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    college.departmnet
AttributeError: 'College' object has no attribute 'departmnet'
>>> 
>>> class College:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self):
...         print(self.name+ "is present at "+self.loc)
... 
...         
>>> class Department(College):
...     def __init__(self,name,ids):
