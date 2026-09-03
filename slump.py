import random

ditt_nummer = random.randint (1, 10)
läskigaAI_nummer = random.randint (1, 10)

name = input ("skriv ditt namn:")
bett_summa = input("Hur mycket vill du betta?:")
bett = int(bett_summa)

print (f"du fick: {ditt_nummer}")
print (f"Läskiga AI fick: {läskigaAI_nummer}")

if ditt_nummer > läskigaAI_nummer:
    print("Grattis " +  name  + "!" + " du vann") 
    print(bett + 100)
if läskigaAI_nummer > ditt_nummer:
    print(f"Läskiga AI vann :(, nu har du {bett-bett}kr") 
     

