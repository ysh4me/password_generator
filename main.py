import random

longeur = int(input("Entrez la longueur du mot de passe souhaité : "))

letter_minus_y_n = input("Voulez-vous des lettres minuscules? (y/n): ")
letter_minus = 'abcdefghijklmnopqrstuvwxyz'

letter_majus_y_n = input("Voulez-vous des lettres majuscules? (y/n): ")
letter_majus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chiffre_y_n = input("Voulez-vous des chiffres? (y/n): ")
chiffre = '0123456789'

special_y_n = input("Voulez-vous des caractères spéciaux? (y/n): ")
special = ''


longeur_special = 0

if special_y_n == 'y':
    longeur_special = int(input("Entrez le nombre des caractères spéciaux souhaité : "))
    special = '!@#$%^&*()_+'

if letter_minus_y_n == 'y' and letter_majus_y_n == 'y' and chiffre_y_n == 'y' and special_y_n == 'y':
    letter = letter_minus + letter_majus + chiffre + special
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'n' and chiffre_y_n == 'y' and special_y_n == 'y':
    letter = letter_minus + chiffre + special
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'y' and chiffre_y_n == 'y' and special_y_n == 'y':
    letter = letter_majus + chiffre + special
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'y' and chiffre_y_n == 'n' and special_y_n == 'y':
    letter = letter_minus + letter_majus + special
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'y' and chiffre_y_n == 'y' and special_y_n == 'n':
    letter = letter_minus + letter_majus + chiffre
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'n' and chiffre_y_n == 'n' and special_y_n == 'y':
    letter = letter_minus + special
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'n' and chiffre_y_n == 'y' and special_y_n == 'n':
    letter = letter_minus + chiffre
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'y' and chiffre_y_n == 'n' and special_y_n == 'y':
    letter = letter_majus + special
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'y' and chiffre_y_n == 'y' and special_y_n == 'n':
    letter = letter_majus + chiffre
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'y' and chiffre_y_n == 'n' and special_y_n == 'n':
    letter = letter_majus
elif letter_minus_y_n == 'y' and letter_majus_y_n == 'n' and chiffre_y_n == 'n' and special_y_n == 'n':
    letter = letter_minus
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'n' and chiffre_y_n == 'y' and special_y_n == 'y':
    print("Vous ne pouvez pas avoir de mot de passe composé uniquement de chiffres et de caractères spéciaux")
    exit()
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'n' and chiffre_y_n == 'n' and special_y_n == 'y':
    print("Vous ne pouvez pas avoir de mot de passe composé uniquement de caractères spéciaux")
    exit()
elif letter_minus_y_n == 'n' and letter_majus_y_n == 'n' and chiffre_y_n == 'y' and special_y_n == 'n':
    print("Vous ne pouvez pas avoir de mot de passe composé uniquement de chiffres")
    exit()
else:
    print("Veuillez choisir au moins une option")
    exit()

password = ''.join(random.sample(letter, longeur + longeur_special))
print(password)
