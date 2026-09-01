name = input("name")
ålder_text = input("Hur gammal är du?")
ålder = int(ålder_text)
print(ålder)
aktuellt_år = 2026
ålder = aktuellt_år-ålder_text
print(f"hej {name} du är ungefär {ålder} år gammal")