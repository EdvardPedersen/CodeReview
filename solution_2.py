import num2words

# Algoritmen min:
# Jeg bruker en while-løkke for å sjekke om jeg har kommet til 99
# For hver runde i while-løkken bruker jeg num2words for å lage et tekst-tall
# Jeg lagrer dette tekst-tallet i en variabel, og skriver ut resultatet
# Til slutt i løkken øker jeg tallet

# Variabelen som inneholder resultatet
result = ""
# Variabelen som inneholder tallet som skal sees på
num = 1
while result != "ninety-nine": # En løkke som sjekker om jeg har kommet til 99
    result = num2words.num2words(num) # Lager ord-versjonen av tallet
    print(num, result, len(result)) # Skriver ut tallet, ord-versjonen, og lengden på tallet
    num += 1 # Øker tallet jeg ser på
