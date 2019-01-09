"""
If Statement homework
Here we compare the height of three people
"""

Can_height = 71
Ali_height = 70
Baris_height = "67"
#Here are the variables in inches, where last variable is a string

def height_comparison(Can_height,Ali_height,Baris_height):
    if Can_height == Ali_height or int(Baris_height) == Can_height or Ali_height == int(Baris_height):
       return True 
    elif not Can_height == Ali_height and not int(Baris_height) == Can_height and not Ali_height == int(Baris_height):
        return False
        
print(height_comparison(Can_height,Ali_height,Baris_height))
