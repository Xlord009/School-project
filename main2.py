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
