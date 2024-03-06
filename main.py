meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "ROFL jest używany jako reakcja na coś zabawnego, podobnie jak LOL"
            }

word = input("Wpisz współczesne słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Nie mamy jeszcze tego słowa... Ale pracujemy nad tym!")
