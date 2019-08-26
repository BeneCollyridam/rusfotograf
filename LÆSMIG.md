# Generer rusbilleder med en fin ramme

## Rammen
Rammen skal være ca. 2480px bredt og 3508px højt og placeres i `ramme.png`.

Den standard ramme er fra: [NeedPix](https://www.needpix.com/photo/download/1539177/frame-square-empty-golden-baroque-gold-nobody-white-background)

## Billeder af rus
Billederne af rus placeres f.eks. i en mappe (eller i roden)

## Generer billeder
`generer_rus.py` læser en liste af rus fra stdin. F.eks. kan du bruge følgende
kommando til at genrere for alle `.jpg|.JPG` billeder:
`find -iname "*.jpg" | ./generer_rus.py`.

En ny fil kaldet `samlet.pdf` vil nu ligge i roden, som indeholder alle dine rus
med billeder og rammen.

Hvis ikke rammen er placeret korrekt prøv da at ændre værdierne på linje 29 i
`generer_rus.py` og hvis billedet af rus ikke er placeret korrekt prøv da med
linje 36-37.
