# 1a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = "thursday"
if day_of_the_week == "thursday":
    print("true")
else:
    print("false")
    
    # Class Review Solution
day_of_the_week = input('Enter day of the week: ')
if day_of_the_week.strip().lower() in ['saturday','sunday']:
    print('Weekend')
else:
    print('Weekday') 

    
# 1b.  prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekdays = ['monday','tuesday','wednesday','thursday','thursday']
weekend = ['saturday','sunday']
if day_of_the_week in weekdays:
    print("Its a weekday")
else:
    print("Keep waiting")

    
# 1c. create variables and make up values for:
    # A. number of hours worked in one week
    # B.the hourly rate
    # C.how much the week's paycheck will be.
# WRITE THE PYTHON CODE THAT CALCULATES THE WEEKLY PAYCHECK. YOU GET PAID 1.5X IF YOU WORK MORE THAN 40HRS.

hrs_worked = 45
wage = 40
weekly_income = hrs_worked * wage
overtime = (hrs_worked - 40) * (wage * 1.5)
if hrs_worked <= 40:
    income = hrs_worked * wage
    print(hrs_worked)
else:
    big_money = (hrs_worked * wage) + overtime
    print(big_money)
    
full_time_pay = wage * 40
print(full_time_pay)


# 2.Loop Basics
    # A. While
    # - Create an integer variable ' i ' with a value of 5.
    # - Create a while loop that runs so long as i is less than or equal to 15
    #- Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1
    
    # Class Review Solution
i = 100 
while i >= -10:
    print(i)
    i = i -5
    
    

    
pick_number = int(input("What number?: "))

def multiplication(multiply):
    for number in range(pick_number):
        print(num)

    # Class Review Solution
your_num = int(input('Input your number: '))

for i in range(1, 11):
    print(f'{your_num} x {i} == {your_num * i}') 

    
    # Class Review solution
for i in range(1,10):
    print(i * str(i))    

    # Class Review Solution
while True:
    your_num = input('Input your number here: ')
    if your_num.isdigit() and int(your_num) % 2 == 1 and 0 < int(your_num) < 50:
        break
    else:
        print('Invalid input. Try harder.')

counter = 1

while counter < 50:
    if counter == int(your_num):
        counter += 2
    else:
        print(counter)
        counter += 2
        
        
# 3. Fizzbuzz
    #One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.¶
    #- Write a program that prints the numbers from 1 to 100.
    #- For multiples of three print "Fizz" instead of the number
    #- For the multiples of five print "Buzz".
    #- For numbers which are multiples of both three and five print "FizzBuzz"
for number in range(2,101):
    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(counter)
    counter += 1    
    
    
# 4.Display a table of powers.
    #- Prompt the user to enter an integer.¶
    #- Display a table of squares and cubes from 1 to the value entered.
    #- Ask if the user wants to continue.
    #- Assume that the user will enter valid data.
    #- Only continue if the user agrees to. 
start = int(input("Choose number:\t"))
keep_going = input("Do you want to continue[Y/N]:\t")
print()

def table_of_powers(start):
    for number in range(start):
        if keep_going.lower() == 'n':
            break
        else:
            print(number, number ** 2, number **3)
        
table_of_powers(start)
    
    
# 5.Convert given number grades into letter grades.   
score = int(input('What is your grade percentage?: '))
more_grades = input('Do you want to continue? [Y/N]')


def passfail(score):
    while True:
        if score >= 88:
            print('A')
        elif score >= 80:
            print('B')
        elif score >= 67:
            print('C')
        elif score >= 60:
            print('D')
        else:
            print('F')
        if more_grades.lower() == 'n':
            break
    
passfail(score)


# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
     #-a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
my_dictionary = [{'title': '1984', 'author': 'George Orwell', 'genre': 'dystopian'},
                {'title': 'Tuesdays with Morrie', 'author': 'Mitch Albom', 'genre': 'life lessons'},
                {'title': 'To Sleep in a Sea of Stars', 'author': 'Chirstopher Paolini', 'genre': 'scify'},
                {'title': 'Project Hail Mary', 'author': 'Andy Weir', 'genre': 'scify'}]
search_genre = input('Choose genre:\t')


def genre(my_dictionary):
    empty_list = []
    for gtype in my_dictionary:
        if gtype['genre'] == search_genre:
            empty_list.append(gtype["title"])
    print(empty_list)
        
genre(my_dictionary)    
    
    