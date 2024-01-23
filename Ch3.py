width = height = length = ""
while width.isdigit() != True:
    width = input("What is the width of the cuboid? ")
while length.isdigit() != True:
    length = input("What is the length of the cuboid? ")
while height.isdigit() != True:
    height = input("What is the height of the cuboid? ")
volume = int(width)*int(length)*int(height)
print("Volume =",str(volume) )