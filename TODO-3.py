# TODO: Write a conditional that prints the color of the selected sportsball
import random

picked_sportsball = random.choice(['tennis', 'basketball', 'golf'])

if picked_sportsball == "tennis":
     print("The {} ball you're playing has the color yellow".format(picked_sportsball))
elif picked_sportsball == basketball:
     print("The {} ball you're playing has the color brown".format(picked_sportsball))
else:
     print("The {} ball you're playing with has the color withe".format(picked_sportsball))