#Unit 3: PygLatin - part 10

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'
    
    
 #Unit 4: Taking a Vacation - part 7

def hotel_cost(nights):
  return 140 * nights


def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  
  elif city == "Pittsburgh":
    return 222
  
  elif city == "Los Angeles":
    return 475
  
  
def rental_car_cost(days):
  total = days * 40
  
  if days>= 7:
    total -= 50
    return total
 
  elif days>= 3:
    total -= 20
    return total
  
  return total
    
  

def trip_cost(city,days,spending_money):
  sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
  return sum
  
print(trip_cost("Los Angeles",5,600))
  

#Unit 5: A Day at the Supermarket - part 12
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for n in food:
        if stock[n] > 0:
            total = total + prices[n]
            stock[n] -= 1
        else:
            total = total
    print total
    return total
  
 #Unit 6: Student Becomes the Teacher - part 9

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total

def get_average(student):
    homework = average(student["homework"])* 0.1
    quizzes = average(student["quizzes"])* 0.3
    tests = average(student["tests"])* 0.6

    avrg = homework + quizzes + tests
    return avrg

def get_letter_grade(score):
    if score>= 90:
        return 'A'
    elif score>= 80:
        return 'B'
    elif score>= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))

#Unit 7: Battleship! - part 18

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"   
  for turn in range(4):
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)
  
