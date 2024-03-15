import smtplib,ssl
from email.message import EmailMessage
import random 
import re

def register(k,p):
    """Funktsioon kasutaja ja parooli registreerimiseks #Функция регистрации пользователя и пароля
    param kasutajanimi: kasutajanime sisestamine
    param parool: sisestage parool
    """
    while True:
        kasutajanimi=input("Sisesta kasutajanimi: ")
        if kasutajanimi not in k:
             k.append(kasutajanimi)
             break
        else: 
            print("Selle kasutajanimi on juba hõivatud")
            continue
    while True:
        valik=input("Kas ma peaksin parooli looma automaatselt või mitte? 1/0: ") 
        if valik=="1":
            pw=auto_pass()
            p.append(pw)
            print("Registreeritud")
            print("Teie parool on: ",pw) 
            print("Kasutajanimi: "+str(kasutajanimi), "ja parool: " +str(pw))
            break
        if valik=="0":
            pw=my_pass()
            p.append(pw)
            print("Olete edukalt registreerunud!")
            print("Kasutajanimi: "+str(kasutajanimi), "ja parool: " +str(pw))
            break
        else:
            print("Error")
            continue

def autoriseerimine(k,p):
    """Funktsioon kontrollib parooli ja kasutajanime, #Функция проверяет пароль и имя пользователя есть ли
    kas need on nimekirjas ja väljastab sõnumi           они в списке и выдает сообщение
    param kasutajanimi: kasutajanime sisestamine
    param parool: sisestage parool
    """
    print(k,p)
    kasutajanimi=input("Sisesta kasutajanimi: ")  
    if kasutajanimi in k:
        print("Kasutajanimi on õige!") 
    else:
        print("Kasutajanimi on vale!") 
    parool=input("Sisestage parool: ") 
    if parool in p:
        print("Parool on õige!") 
    else:
        print("Vale parool!") 
        return k, p 
    print("Olete edukalt sisse loginud!") 


def muuta_kasautajanime_või_parooli(k,p):
    """Funktsioon muudab parooli või kasutajanime uueks #Функция изменяет  пароль или имя пользователя на новое
    param kasutajanimi: kasutajanime sisestamine
    param parool: sisestage parool
    """
    kasutajanimi=input("Sisestage oma praegune kasutajanimi: ")
    if kasutajanimi in k:
        indeks=k.index(kasutajanimi)
        asendamine=input("Mida soovite asendada? (kasutajanimi/parool):  ") 
        if asendamine=="kasutajanimi":
            uus_kasutajanimi=input("Sisesta uus kasutajanimi: ")
            k[indeks]=uus_kasutajanimi
            print("Kasutajanime muutmine õnnestus!") 
            print("Uus kasutajanimi: "+str(uus_kasutajanimi))
            print("Vana kasutajanimi: "+str(kasutajanimi), ".Uus kasutajanimi: "+str(uus_kasutajanimi))
            print(k,p)
        elif asendamine=="parool":
            parool=input("Sisestage oma praegune parool: ") 
            if parool==p[indeks]:
                uus_parool=input("Sisestage uus parool: ") 
                p[indeks]=uus_parool
                print("Parooli muutmine õnnestus!") 
                print( "Uus parool: "+str(uus_parool))
                print("Vana parool: "+str(parool), ".Uus parool: "+str(uus_parool))
                print(k,p)
            else:
                print("Viga")
        else:
            print("Viga")
    else:
        print("Viga")
    return k,p

def parooli_taastamine(k,email,p)->any:
    """Funktsioon küsib kasutajanime ja saadab meilile parooli, #Функция спрашивает имя пользователя и отправляет  на почту пароль,
     et taastada unustatud parool                                          чтобы восстановить забытый пароль
     param kasutajanimi: kasutajanime sisestamine
    param parool: sisestage parool
    """
    smtp_server="smtp.gmail.com"
    port = 587 #for starttls
    sender_email = "daragalcenko3@gmail.com"
    password = input("Type ur password and press enter: ")
    context=ssl.create_default_context()
    #msg
    msg = EmailMessage()
    msg.set_content ("Tere tulemast! "+str(p)) 
    msg['Subject']="Parooli taastamine!"
    msg['From']=sender_email="daragalcenko3@gmail.com"
    msg['To']=email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        print("Teie parool oli saadetud emailile")
        server.quit()
        return True


def auto_pass():
    """
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    parool = ''.join([random.choice(ls) for x in range(12)])
    return parool

def my_pass():
    """
    """
    print("Parool peab koosnema numbritest, väiketähtedest, suurtähtedest ja eritähtedest sümboleid.") 
    while True:
        parool=input("Sisestage parool: ")
        if len(parool)<8:
            print("Parool peab koosnema vähemalt 8 tähemärgist")
            continue
        elif re.search("[0-9]", parool) is None:
            print("Numbreid pole")
            continue
        elif re.search("[a-z]", parool) is None:
            print("Paroolis ei ole väiketähti") 
            continue
        elif re.search("[A-Z]", parool) is None:
            print("Paroolis pole suuri tähti")
            continue
        elif re.search("[$@^=.,:;!_*-+()/#¤%&]", parool) is None:
            print("Paroolis pole erimärke")
            continue
        else:
            print("Teie parool on turvaline!")
            return parool 

def loe_failist(k,p)->any:
    """Loeme failist ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    failname="andmeid.txt"
    kasutajanimi=parooli=[]
    try:
        f=open(failname,'r')
        for rida in f:
            kasutajanimi.append(rida.split()[0])
            parooli.append(rida.split()[1])
        f.close()
        return kasutajanimi,parooli
    except Exception as e:
        print(e)

def kirjuta_failisse(kasutajanimi,parool):
    """Функция открывает файл в режиме записи
    """
    failname="andmeid.txt"
    try:
        f=open(failname,'w',encoding="utf-8")
        for i in range(len(kasutajanimi)):
            k=kasutajanimi[i]
            p=parool[i]
            f.write(f"{k}  {p}"+"\n")
    except: 
        print("Viga")


def uus_kasutaja(kasutajanimi, parool):
    """
    Funktsioon uue kasutaja lisamiseks faili
    """
    failname = "andmeid.txt"
    try:
        f=open(failname, 'a', encoding="utf-8")
        f.write(f"{kasutajanimi} {parool}\n")
        print("Kasutaja oli lisatud!")
    except:
        print("Viga, kasutaja ei ole lisatud")
         
