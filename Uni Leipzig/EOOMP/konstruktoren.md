- spezielle Methoden
- Signatur: umfasst die selben Elemente wie eine Methode

- konstruktoren haben keinen Rückgabetyp, denn er gibt eine Instanz der Klasse selbst heraus

- anders als in Python notwendig, um Instanzen der Klasse zu kreieren

spezielle [[Methode]] zum erstellen einer Instanz einer [[Klassen und Instanzen|Klasse]]


	public Kreis(double radius) {
		this.radius = radius;
	}


	public class Auto {
		private int anzahlPlaetze;
		private double leistung	
		
		public Auto(int anzahlPlaetze double leistung){
			this.anzahlPlaetze = anzahl	
		}
	}



notwendig, sodass in anderen funktionen auf die variablen anzahl eines Autos zugegriffen werden kann: auf leistung kann nicht zugegriffen werden


 

# Verhindern vom Erzeugen von Instanzen
private Math(){}
- Konstruktor ist gebaut, auf ihn kann aber nicht zugegriffen werden
- somit können keine Instanzen der Klase Math() erzeugt werden