bill_amount = float(input("What was the total bill? "))
people_count = int(input("How many are splitting the bill? "))
tip_percent = float(input("How much do you want to tip? "))

total_tip = bill_amount * (tip_percent/100)
round_total_tip = round(total_tip, 2)
total_bill = total_tip + bill_amount
round_total_bill = round(total_bill, 2)
split_bill = total_bill/people_count
rounded_split_bill = round(split_bill, 2)

message = f'''
The total bill is ${round_total_bill}
Meaning the total tip is ${round_total_tip}
Each of the {people_count} people owes ${rounded_split_bill}
'''

print(message)