import random
import pandas as pd

boxes = {'Alan': 5,
         'Alice': 5,
         'Bo': 5,
         'Emma': 5,
         'Eric': 10,
         'Eugene': 10,
         'Ewing': 5,
         'Jonathan Hom': 5,
         'Livvy': 5,
         'Martin': 5,
         'Ricky': 5,
         'Ryan': 10,
         'Sammy': 5,
         'Sutee': 10,
         'Tim - Bos Brother': 5,
         'Whitney': 5}


def randomly_choose(choices):
    res = []
    for i in range(10):
        choice = random.choice(choices)
        res.append(choice)
        choices.remove(choice)
    return res


def randomly_assign_box(box_dict):
    remaining_people = list(box_dict.keys())
    person = random.choice(remaining_people)
    box_dict[person] -= 1
    if box_dict[person] == 0:
        del box_dict[person]
    return person, box_dict

# Bengals columns
# Rams rows

# randomly decide rows and columns, arbitrary 10 iterations
for i in range(10):
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    bengals_nums = randomly_choose(possibilities)
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rams_nums = randomly_choose(possibilities)

matrix = [[0 for i in range(10)] for j in range(10)]

# randomly decide person in box, arbitrary 10 iterations
for i in range(10):
    for j in range(10):
        matrix[i][j], boxes = randomly_assign_box(boxes)


df = pd.DataFrame(matrix, index=rams_nums, columns=bengals_nums)

df.to_csv("C:\\Users\\whitn\\super_bowl_boxes.csv")