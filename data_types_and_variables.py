# 1.You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
Little_Mermaid = 3
Brother_Bear = 5
Hercules = 1
price_per_day = 3
Total = (Little_Mermaid * price_per_day)+ (Brother_Bear * price_per_day) + (Hercules * price_per_day) 
print("$",Total)


# 2.Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google = 400
amazon = 380
facebook = 350
gg_hrs = 6
amz_hrs = 4
fb_hrs = 10
week_income = (google *gg_hrs) + (amazon * amz_hrs) + (facebook * fb_hrs)
print('$',week_income)


# 3.A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_limit = 20
students = ["studentA", "studentB", "studentC", "studentD"]
len(students)
can_be_enrolled = class_limit - len(students) >= 0


    # class review solution
class_is_not_full = True
schedule_does_not_conflict = True
enroll = class_is_not_full and schedule_does_not_conflict
print(enroll)


# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
product_items = ["product1", 'product2', 'product3']
product_offer_req = len(product_items) >= 2

len(product_items)

    #class solution
purchase_more_than_two = True
product_not_expired = True
prem_membership = False
discount_eligible = product_not_expired and (purchase_more_than_two or prem_membership)


# 5.Username and Password
my_pw = "dundundun"
my_usn = "cpd"

password = len(my_pw) >= 5
username = len(my_usn) <= 20
test = password != username









