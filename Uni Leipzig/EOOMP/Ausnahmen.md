---
aliases:
  - Throwable
  - Exceptions
  - Error
---
- trennt Ausnahmesituationen von gewöhnlichen Situationen, lässt unterschiedliche Behandlung zu
- 

- es sollte von dem spezifisschten Fehler zu den allgemeinsten Fehler in ein
- pro Fehler-Art gibt es einen catch-block
- es macht also sinn viele throwables zu erstellen, damit zwischen vielen verschiedenen Fehler unterschieden werden kann


# Unchecked Exceptions
- Instanzen von RuntimeException
- brauchen keine throws-Klasel, müssen nicht in Methode deklariert werden
- können leicht umgangen werden



# Checked Exceptions
Instanzen von Exception aber nicht von RuntimeException
- "erwartete Fehler"
- müssen in der throws Klausel einer Methode deklariert werden:
	`public Weihnachtsmann throws Exception{}`

```
public Kugel(double radius)throws Exception{
	if(radius<0){
		throw new Exception();	
	}	
}
```

- getMessage() ist eine Methode der Klasse Exception, die geerbt wird


# Error
- Programm hat keinen Einfluss
- sollten weder geworfen, noch gefangen werden
- bsp: zu wenig speicher



# Eigene Throwables


# Eigene Exceptions erstellen
