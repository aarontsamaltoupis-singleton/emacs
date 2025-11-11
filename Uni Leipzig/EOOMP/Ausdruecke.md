Vorlesung 29.10.25

`+,-,*,/,%`


# Arithemetische Operatoren

## Kurzschreibweisen
	a=a+b --> a+=b

	a=a+1; <--> a+=1; <--> ++a; <--> a++;
	a=a-1; <--> a-=1; <--> --a; <--> a--;


arithmetische operatoren : 
long: analog int
float: analog double

bspw: 
	int i = 7+5%4;


	long 1 = 5L * 7L +4L;

Nach Arithmetischen Operationen auf dem Typ byte, muss ergebnis zunächst noch wieder in byte umgeandelt werden, da die bytes für arithmetische oPeratoren in Integers umgewandelt werden.

wenn double ausgegeben werden soll, sollte in arithmetischer operation auch doubles benutzt werden, bzw integers durch bspw:  
	(double) 7
in doubles umgewandelt werden
ansonsten wird der Wert 0 ausgegeben


# Vergleiche
`==,!=, <, >, <=, >=`
``


- Zwei komplett unterschiedliche Instanzen sind nicht gleich, auch wenn sie die gleichen Werte haben: 
	Integer wert1 = new Integer(1);
	Integer wert2 = new Integer(10);

- Es gilt:  wert1!=wert2

Die Variablen müssen tatsächlich auf die gleiche Instanz verweisen, bspw:
	Integer wert = new Integer(1)
	Integer kopie = wert;
	kopie == wert --> true

# logische operatoren
&&: logisches und
||: logisches oder
!: logisches nciht