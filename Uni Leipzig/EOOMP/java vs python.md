python: 
- **whitespace significant language**
- everything is public
- 


java: 
- compiled language: 
	designed for larger scaled programms: more structure
- everything is in classes: all funcitionality designed in classes
- whitespace insignificant
- visibility control

- design for large scale applications: 

# methods
class HelloApp {
	public static void main (String[] args)
		System.out.println("hello World")
}

- public: visibility control, default in python
- static: function belongs to class itself (as opposed to an instance method): objects of the class HelloApp wouldnt necessarily use this function
- void: like none in python. method doesn't return any value
- main: name of method
- String[] args: method is passed an array of strings named args
- System.out: special method of the system class: holds reference to outputstream, **gives us access to the terminal**
- println: print line

