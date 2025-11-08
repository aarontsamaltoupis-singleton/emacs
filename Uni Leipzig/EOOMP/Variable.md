- ein Ort im Speicher
- variablen können werte zugewiesen werden, gespeicherten Werte gelesen werden
- eindeutige **Bezeichner**

Variablen haben meist [[Modifikatoren]], sowie einen [[java primitive datentypen|typ]].


# Variablen in Java
## Deklaration
- Variablen müssen deklariert (engeführt) werden vor der Nutzung: 

 int wert = n



## Initialisation
		double nameDerVariable;
- Variablen können initialisiert werden (Wertzuweisung)

		double nameDerVariable = 1;


## locale Variable: 
variable in methode deklariert, sobald methode abgeschlossen ist, gibt es variable nciht mehr
Lokale Variablen existieren nur in der Methode, in der sie deklariert wurden
Auch methoden innerhalb einer methode haben keinen Zugriff auf lokale Variblen dieser Methode (es sei denn ,sie wird als parameter übergeben)

# Arrays

Arrays:
 `int [] werte = new int [4];`
 `werte [0] = 1;`
 `werte [1] = 2;`
 `werte [2] = 3;`
 `werte [3] = 4;`



werte.length : Länge des Arrays




# Kopieren von Instanzen
`Integer wert = New Integer(70);`
`Integer kopie = wert;`

- kopie und wert bezeichnen dasselbe Objekt


# Konstanten
[[Konstanten]]


# Attribute
- "irgendwo muss "=" stehen", entweder bei der Deklaration, oder in einem Konstruktor
- Namen in einer Klasse

# Parameter
- Namen in einer Methode
- Wert wird festgelegt, wenn [[Methode]] aufgerufen wird
