import random
#4 4 andra gång 3 3 
ditt_slag = random.randint(1, 6)
datorns_slag = "6"
summa = ditt_slag + datorns_slag

print("Alea iacta est!")
print(f"Du: {ditt_slag}, datorn: {datorns_slag}, totalt: {summa}")
# programmet kraschar på rad nummer 5 pga datorns slag var en int