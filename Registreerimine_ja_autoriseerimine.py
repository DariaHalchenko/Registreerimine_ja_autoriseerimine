from MyModule import *
kasutajanimi=["Daria", "User342", "Valeria443", "Darja6666"]
parool=["Jess333", "12333Valeria", "44556vkd", "jfhbdsf"] 
while True:
    print("0-registreerimine\n1-logi sisse\n2-nime või parooli muutmine\n3-unustatud salasõna taastamine\n") 
    valik=int(input())
    if valik==0:
        register(kasutajanimi,parool)
        uus_kasutaja(kasutajanimi, parool)
    if valik==1:
        autoriseerimine(kasutajanimi,parool) 
        loe_failist(kasutajanimi,parool)
        kirjuta_failisse(kasutajanimi,parool)
    if valik==2:
        print(kasutajanimi,parool)
        muuta_kasautajanime_või_parooli(kasutajanimi,parool) 
        loe_failist(kasutajanimi,parool)
        kirjuta_failisse(kasutajanimi,parool)
    if valik==3:
        nimi=input("Sisesta teie kasutajanimi: ")
        if nimi in kasutajanimi:
            email=input("Sisesta teie posiadress: ")
            parooli_taastamine(nimi,email,parool[kasutajanimi.index(nimi)])
            loe_failist(kasutajanimi,parool)
            kirjuta_failisse(kasutajanimi,parool)
        else: print("Nimi ei leidnud")
