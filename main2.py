
score = 0

print("Quiz de 5 questions : pour réussir, il faut obtenir au moins 3 points.")

question1 = input("Répondez par Vrai ou Faux : Le WWW est sorti en 1986 ").lower()

if question1 == "faux":
    score += 1
    print("Votre réponse est correcte !")
else:
    print("Votre réponse est fausse :(")


question2 = input("Est-ce que l'inventeur du WWW était Tim Berners-Lee ? ").lower()

if question2 == "vrai":
    score += 1
    print("Votre réponse est correcte !")
else:
    print("Votre réponse est fausse :(")


question3 = input("Amazon était-il le seul magasin de e-commerce en 1995 ? ").lower()

if question3 == "faux":
    score += 1
    print("Votre réponse est correcte !")
else:
    print("Votre réponse est fausse :(")


question4 = input("Est-ce que la bulle Internet a explosé en 2000 ? ").lower()

if question4 == "vrai":
    score += 1
    print("Votre réponse est correcte !")
else:
    print("Votre réponse est fausse :(")


question5 = input("IBM veut dire Personal Computer ? ").lower()

if question5 == "faux":
    score += 1
    print("Votre réponse est correcte !")
else:
    print("Votre réponse est fausse :(")


print(f"Vous avez obtenu {score}/5 points.")

if score >= 3:
    print("Vous avez réussi le quiz !")
else:
    print("Vous avez échoué le quiz.")
score = 0
print("Quiz de 5 questions: pour réussir le quiz il faut plus de 2 points")
question1 = input("Répondez par Vrai ou Faux: Le WWW est sorti en 1986 ")
if question1 == "faux":
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')

question2 = input("Répondez par Vrai ou Faux: Est ce que l'inventeur du WWW était Tim Berners-Lee? ")
if question2 == "vrai":
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')

question3 = input("Répondez par Vrai ou Faux: Amazon etait le seul magasin e du type e-commerce en 1995 ")
if question3 == "faux":
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')


question4 = input("Répondez par Vrai ou Faux: est ce que la bulle d'internet explose en 2000? ")
if question4 == "vrai":
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')


question5 = input("Répondez par Vrai ou Faux: IBM veut dire personal computer? ")
if question5 == "faux":
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')



print(score)
if score >= 3:
    print(f'Vous avez eu {score} point! Vous avez reussi le quiz!')
else:
    print(f'Vous avez eu {score} point. Vous avez échoué le quiz.')
