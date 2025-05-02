# Made By Erdem Galibov

from colorama import Fore, init
from os import system
import random 

system("cls")
init()

def oyun():
    """Taş, kağıt, makas oyununu oynatır."""
    secenekler = ["taş", "kağıt", "makas"] 
    while True:
        # Kullanıcının seçimini al
        kullanici_secimi = input(Fore.BLUE + "Taş, kağıt veya makas seçin (çıkmak için 'q'): ").lower()
        if kullanici_secimi == "q": print(Fore.LIGHTBLUE_EX + "Oyundan çıkılıyor...") 
        break
    if kullanici_secimi not in secenekler:
        print(Fore.RED + "Geçersiz seçim. Lütfen taş, kağıt veya makas seçin.")
    bilgisayar_secimi = random.choice(secenekler),
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
    if kullanici_secimi == bilgisayar_secimi:
        print(Fore.CYAN + "Berabere!")
    elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"): 
        print(Fore.GREEN + "Kazandınız!")
    else: 
        print(Fore.RED + "Kaybettiniz!") 


if __name__ == "__main__":
    oyun() 