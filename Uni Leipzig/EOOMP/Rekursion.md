- langsamer als Iterativ, ist aber möglichkeit bestimmte Funktionen, wie Ackermann- Funktion zu berechnen

Beispiel Fakultät:
```
public static final fakultaetRecursive(final long n){
	if (n>1){
		// rekursiver Aufruf
		return n*fakultaetRecursive(n-1);
	}
	else{
		//Basisfall
		return 1;
	}
}
```
- Basisfall im else
	- Werte kleiner 1 springen somit auch in den Basisfall


Beispiel odd even
$odd(n)=\begin{cases} true: n=1 \\even(n-1): n>1 \\ \end{cases}$

$even(n)=\begin{cases} false: n=1 \\odd(n-1): n>1 \\ \end{cases}$

```
public static boolean odd(final int n){
	if (n>1){
		return even(n-1);
	}
	else{
		return true
	}
}

public static boolean even(final int n){
	if (n>1){
		return odd(n-1);
	}
	else{
		return false
	}
}
```
