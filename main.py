import os

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure(enter column number and row number, e.g. \"11\" - column 1, row 1) ")

x_axis = int(position[0])-1
y_axis = int(position[1])-1
map[y_axis][x_axis] = "X"

print(f"{row1}\n{row2}\n{row3}")
os.system('pause')