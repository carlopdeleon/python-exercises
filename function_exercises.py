# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(ab):
    if ab == 2 or ab == "2":
        return True
    else:
        return False
print(is_two(2))
print(is_two(3))
print(is_two("2"))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
list_vowels = ['a','e','i','o','u']
def is_vowel(chosen_vowel):
    if chosen_vowel in list_vowels:
        return True
    else:
        return False

    
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(a_consonant):
    if is_vowel(a_consonant) != True:
        return True
    else:
        return False

    
# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def accepts_strings(aword):
    if aword[0] in list_vowels:
        return aword[0].lower() + aword[1:]
    else:
        return aword[0].upper() + aword[1:]


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip():
    bill = int(input('How much did it cost?: '))
    tip_percent = int(input('What percent tip do you want? 10/15/20:'))
    total_tip = bill * (tip_percent/100)
    return total_tip

calculate_tip()


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount():
    original_price = int(input('How much did it cost?: '))
    discount = int(input('What percentage is the discount?: '))
    discount_total = original_price * (discount/100)
    total = original_price - discount_total
    return total


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas():
    the_string = input('What is your number:')
    conversion = int(the_string.replace(',',''))
    return conversion


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade():
    grade_percentage = int(input('What was your score?:'))
    
    if 90 <= grade_percentage <= 100:
        return "A"
    elif 80 <= grade_percentage <= 89:
        return "B"
    elif 70 <=  grade_percentage <= 79:
        return "C"
    elif 60 <= grade_percentage <= 69:
        return "D"
    else:
        return "F"


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed
def remove_vowels():
    list_vowels = ['a','e','i','o','u','A','I','O','E','U']
    the_string = input('What words?: ')
    smash_word = ''
    for vowels in the_string:
        if vowels not in list_vowels:
            smash_word = smash_word + vowels
    return smash_word


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is
def normalize_name():
    name = input("what is your name?: ")
    updated_name = name.lower().strip().replace(' ', '_')
    return updated_name
normalize_name() 


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
import numpy as np

def cumulative_sum():
    number_list = int(input('What numbers?: '))
    adding_list = []
    for number in number_list:
        adding_list.append(number)
    return np.cumsum(adding_list)


    # Class Review Solution
def cumulative_sum(numbers):
    output = []
    total = 0
    for num in numbers:
        total += num
        output.append(total)
    return output