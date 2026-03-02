from art import text2art
from colorama import Fore, Back, Style
# Bonus

art1 = text2art("Mohsen alfawaz",font='rnd-xlarge')
print(Fore.BLUE + art1)
art2 = text2art("TEST",font='rnd-large')
print(Back.CYAN + art2)
