

pajamos = []
islaidos = []



while True:
    print("1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "q - Išeiti\n")

    pasirinkimas = input("Pasrinkite norimą opciją > ")

    if pasirinkimas == "q":
        break

    elif pasirinkimas == "1":
        try:
            pajamu_suma = float(input("Įveskite norimas pajamas > "))
            pajamu_rusis = input("Įveskite pajamų rūšį > ")
            pajamos.append((pajamu_suma, pajamu_rusis))
            print("Pajamos įvestos!\n")
        except ValueError:
            print("Klaida, įveskite teisingą sumą. \n")






