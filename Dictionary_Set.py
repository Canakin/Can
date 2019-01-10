"""
Dictionary & Sets Homework 
Author : Can Cimenser 
"""

Dictionary = {"Song":"One", "Genre":"Trash Metal","Artist":"Metallica","Album":"And Justice For All","DurationInMinutes":"7.45","Year_Released":"1988","Spotifty_play_mn":"135.5","No_of_instruments":"3"}
for i in Dictionary:
    print(i,":",Dictionary[i])
#Here we print the keys and its values

def guess():
    key = input("Enter a key name")
    if key in Dictionary:
        value = input("Enter the value of the key")
        if value == Dictionary[key]:
            return True
        else:
            return False
    else:
        return False

print(guess())








