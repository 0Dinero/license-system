import time
import auto_py_to_exe
from discord_webhook import DiscordWebhook
from random import seed
from random import randint

##GENERATOR

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', '1', '2', '3', '4', '5','6', '7', '8', '9']
dc_wh = "your_webhook"
seed()
x = randint(0, 24)
let_1 = letters[x]
seed()
x = randint(0, 24)
let_2 = letters[x]
seed()
x = randint(0, 24)
let_3 = letters[x]
seed()
x = randint(0, 24)
let_4 = letters[x]
seed()
x = randint(0, 24)
let_5 = letters[x]
seed()
x = randint(0, 24)
let_6 = letters[x]
seed()
x = randint(0, 24)
let_7 = letters[x]
seed()
x = randint(0, 24)
let_8 = letters[x]
seed()
result = let_1 + let_2 + let_3 + let_4 + "-" + let_5 + let_6 + let_7 + let_8
webhook = DiscordWebhook(url=dc_wh, content=result)
response = webhook.execute()

##COMPARING

time.sleep(1.25)
xx = input("We need an access-code to continue: ")
if xx == result:
    #access code
    print("You have access")
else:
    exit()
