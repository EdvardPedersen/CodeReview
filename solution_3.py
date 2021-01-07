## Her har jeg prøvd å lage en algoritme for å gjøre dette
## Men det fungerer ikke helt, og jeg skjønner ikke hva jeg har gjort feil


## Lager en klasse
class TextNumber:
    def __init__(self,x):
        self.number = x
        self.convert_to_text()

## Konverterer til tekst
    def convert_to_text(self):
        # Har fått disse listene fra Navn Navnesen
        bigs = ["tjue", "tretti", "førti", "femti", "seksti", "søtti", "åtti", "nitti"]
        smalls = ["en", "to", "tre", "fire", "fem", "seks", "syv", "åtte", "ni", "ti", "elleve", "tolv", "tretten", "fjorten", "femten", "seksten", "søtten", "atten", "nitten"]
        if self.number < 1 or self.number > 99:
            self.text = "Unsupported"
        elif self.number >= 20:
            text = str(self.number)
            first = bigs[int(text[0])]
            second = smalls[int(text[1])]
            self.text = first + second
        # Kan bare bruke direkte hvis det er under 20
        elif self.number < 20:
            self.text = smalls[self.number]

    def pretty_print(self):
        print(f"The number is {self.number}, which is written \"{self.text}\", which has a length of {len(self.text)}")

## Lager tallene
for i in range(100):
    TextNumber(i).pretty_print()
