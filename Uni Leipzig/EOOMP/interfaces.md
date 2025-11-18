# Grammatik
```
public abstract interface Name {

}
```
- implizit immer `abstract`.

## Grammatik innerhalb interface
### Konstante
`public static final int  KONSTANTE=2;`

- implizit immer `public static final`

### Methode

`public abstract double  getRadius();`

- implizit immer `public abstract`

## bsp: 

```
package eoomp;

public interface Statistik{
	public double getFlaecheninhalt();
	public double getUmfang();
}
```
# Implementierung 

```
public interface Statistik {
	public double getFlaecheninhalt();
	public double getUmfang();
}

public class Kreis implements Statistik {
	private double radius;
	
	public Kreis(final double radius) {
	setRadius(radius)
	}
	...
	
	@Override
	public double getFlaecheninhalt(){
	return ...;
	}
	
	@Override
	public double getUmfang(){
	return ...;
	}
}

```
- Die funktionen aus dem interface müssen in den einzelnen Klassen, die das interface implementieren trotztdem noch definiert werden

`@Override` ist optional