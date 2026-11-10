score = 0
print("Quiz de 5 questions: pour réussir le quiz il faut plus de 2 points")

question1 = input("Vrai ou faux: Le WWW est sorti en 1986 ")
if question1 == "Faux" or "faux" or 'fake' or 'f':
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')

question2 = input("Vrai ou faux: Est ce que l'inventeur du WWW était Tim Berners-Lee? ")
if question2 == "Vrai" or "vrai" or 'true' or 'v':
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')

question3 = input("Vrai ou faux: Amazon etait le seul magasin e du type e-commerce en 1995 ")
if question3 == "Faux" or "faux" or 'fake' or 'f':
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')


question4 = input("Vrai ou faux: est ce que la bulle d'internet explose en 2000? ")
if question4 == "Vrai" or "vrai" or 'true' or 'v':
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')


question5 = input("Vrai ou faux: IBM veut dire personal computer? ")
if question5 == "Faux" or "faux" or 'fake' or 'f':
    score =+ 1
    print('votre réponse est correcte!')

else:
    print('votre réponse est fausse :(')



print(score)
if score <= 3:
    print(f'Vous avez eu {score} point! Vous avez reussi le quiz!')

else:
    print(f'Vous avez eu {score} point. Vous avez échoué le quiz.')
