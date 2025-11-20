```
public class Position {
	protected double x;
	protected double y;
	
	public Position(final double x, final double y){
		this.x = x;
		this.y = y;	
	}
}



public class Kreis extends Position{
	private double radius;
	
	public Kreis(final double x, final double y, final double radius){
		super(x,y)
		this.radius = radius	
	}	
}
```


# Kreieren von Instanzen: 

class Mensch{}

class Seefahrer extends Mensch{}


Mensch tom = new Seefahrer
- kann nur Funktionen verwenden, die aus Mensch geerbt sind, keine die spezifisch neu für Seefahrer kreiert wurden
- verwendet aber trotzdem die überschriebene Version von Funktionen, die Seefahrer von Mensch geerbt hat

Seefahrer tom = new Seefahrer
- kann geerbte Funktionen aus Mensch und spziefische Funktionen verwenden


