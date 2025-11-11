[[]]*bsp*: 

Structure: 

**class Robot**
- name: 
- color: 
- weight
	 class Robot defines the abstract attributes name, color and weight, but does not assign any concrete values
- birthdate
- +introduceSelf()

**object R1**
- name: "Tom"
- color: "red"
- weight: 30
- birthdate: 2006
	- instances of a class have concrete valuess for the attributes of the class
- +introduceSelf()

**object R2**


bsp: 

		class Robot: 
				def introduce_self(self):
					print("my name is ", self.name)

				def age(self)
					return 2025 - self.birthdate

the argument self has to be included in every function defined in a class
the argument "self" of the defined function gives the function all attributes that are defined later on:  (attributes have to be defined, otherwise calling the function will return an AttributeError)

		r1 = Robot()
		r1.name = "Tom"
		r1.birthdate = 2006


		r1.introduce_self()
		print(r1.age())



Constructors can be used to define these attributes directly when creating an instance and thereby avoiding Attribute Errors: 
# Constructor

		class Robot;
			def __init__(self, name, color, weight, birthdate)
				self.name = name
				self.color = color
				self.weight = weight
				self.birthdate = birthdate
			
			def introduce_self(self):
				print("my name is ", self.name)

			def age(self)
				return 2025 - self.birthdate
				
The functions can now be called directly after creating an object, with the attributes defined in the creation: 

		r1 = Robot("Tom", "red", 68, 2006)

			print(r1.age())

The attributes of the instance can also be retrieved without calling a function: 

		r1 = Robot("Tom", "red", 68, 2006)
		print(r1.name)



