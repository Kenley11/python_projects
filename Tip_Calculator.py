bill_before_tip = float(input('What is the current bill: \n$'))
tip = int(input('How much would you like to tip:\n%'))
query_people = input('Are you splitting the bill with others?: [Y][N]\n').lower()

tip_percent = tip / 100
full_tip_amount = round(bill_before_tip * tip_percent)
final_bill = round((bill_before_tip * tip_percent) + bill_before_tip)

if query_people == 'y':
    num_of_people = int(input('How many:\n'))
    tip_per_person = round(full_tip_amount / num_of_people)
    print(f'\nTotal bill: ${final_bill}.\nTotal tip: ${full_tip_amount}.\nEach person should tip: ${tip_per_person}.\n')
if query_people == 'n':
    print(f'\nTotal bill: ${final_bill}.\nTotal tip: ${full_tip_amount}.\n')





