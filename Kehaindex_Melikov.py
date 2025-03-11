try:
    print("Tere! Olen sinu uus sõber - Python!")
    nimi = input("Mis sinu nimi on? ")
    print(f"{nimi}, oi kui ilus nimi!")
    küsimus = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if küsimus == 1:
        pikkus = float(input("Kirjuta oma pikkus sentimeetrides: "))
        mass = float(input("kirjuta oma kehakaalu kilogrammides: "))
        if pikkus >0 and mass >0:
            KMI= mass/(0.01 * pikkus)**2
            print(f"{nimi}! Sinu keha indeks on: {round(KMI,1)}")
            KMI=int(KMI)
            if KMI <16:
                print("Tervisele ohtlik alakaal")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI in range(16,20):
                print("Alakaal")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI in range(20,26):
                print("Normalkaal")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI in range(26,31):
                print("Ülekaal")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI in range(31,36):
                print("Rasvumine")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI in range(36,41):
                print("Tugev rasvumine")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
            elif KMI>40:
                print("Tervisele ohtlik rasvumine")
                print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")

        else:
            print("Kuidas sa elus oled?")
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print(f"Kohtumiseni, {nimi}!Igavesti Sinu, Python!")
except Exception as e:
    print ("Viga:",e)
    ##
