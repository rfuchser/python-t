
# IMPORT MODULE
import requests

# GET API STATUS REUEST CODE
response = requests.get('https://deckofcardsapi.com/api/deck/new/')

# CHECK IF STATUS CODE IS 200
if response.status_code == 200:
    deck_id = response.json()['deck_id']
    requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
else:
    print(f"Request unsuccessful. Status code: {response.status_code}")
    exit()

# GET 5 CARD
draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")

# SAVE CARD IN VARIABLE
draw = draw_response.json()


# LOOP TROUGH THE CARD AND PRINT VALES
i = 1

for card in draw['cards']:
    print(f"Card {i} is {card['value']} of {card['suit']}")
    i +=1