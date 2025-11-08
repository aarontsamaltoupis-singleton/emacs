#Javaspezifisch 
# Methoden
int i = Integer.max(int a, int b);
- max ist dabei eine [[Modifikatoren|static]] methode der Klasse Integer und kann deshalb ohne Instanz der klasse integer verwendet werden
int i = Integer.min(int a, int b);
# Klassen
# java.lang.Math
- komplexere mathematische Funktionen

import java.lang.Math;

public final class Math
	public static final double PI = 3.1415926535;

PI: name der variable
final: PI ist konstante, wert kann nicht verändert werden
static: die funktion braucht keine INstanz, durch Klassenname kann darauf zugegriffen werden: 
	Math.PI
double: es gibt wort in speicher, das genau wert von PI speichert


