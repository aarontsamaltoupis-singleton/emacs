#Javaspezifisch

| Source Code                 | Aktion                                       | Bezeichnung |
| --------------------------- | -------------------------------------------- | ----------- |
| Integer i =5;               | Integer i = new Integer(5);                  | autoboxing  |
| int j = i;                  | int j = i.intValue();                        | unboxing    |
| double d =j;                | double d = (double) j;                       | typecast    |
| System.out.println(radius); | System.out.println(Double.toString(radius)); |             |

Zu 2): 
i.intValue() ist eine Methode der Integer Klasse, die den Value des Integers ausgibt. j wird diesm Wert gleichgesetzt.

