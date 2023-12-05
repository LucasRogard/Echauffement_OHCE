import time

def main():
    heure_actuelle = time.localtime().tm_hour
    if 6 <= heure_actuelle < 18:
        print("Bonjour")
    else :
        print("Bonsoir")

    while True:
        saisie = input()

        if saisie == "exit":
            if 6 <= heure_actuelle < 18:
                print("Au revoir")
            else:
                print("Bonne soirée")
            break

        if saisie == saisie[::-1]:
            print("Bien dit !")
        else:
            print(saisie[::-1])

main()
