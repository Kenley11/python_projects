def investment_return():
    salary = int(input("What is your annual salary? ($): "))
    monthly_contributions_percentage = int(
        input("How much do you contribute each month? (%): ")) / 100
    current_age = int(input("How old are you?: "))
    target_retirement_age = int(input("At what age do you want to retire?: "))
    expected_return_rate = int(
        input("What is your expected return? (%): ")) / 100
    current_401k_balance = float(
        input("Enter your current 401(k) balance ($): "))
    employer_match = int(input("What is your employer match? (%): ")) / 100
    match_limit = int(input("What is the match limit? (%): ")) / 100

    annual_contributions_dollarAmount = round(
        (salary * monthly_contributions_percentage))

    investing_years = target_retirement_age - current_age

    employee_contributions = (investing_years) * \
        annual_contributions_dollarAmount

    annual_employer_contributions = (salary * match_limit * employer_match)
    lifetime_employer_contributions = (
        salary * match_limit * employer_match * investing_years)

    total_year_contribution = annual_contributions_dollarAmount + \
        annual_employer_contributions

    starting_balance = current_401k_balance

    for age in range(current_age + 1, target_retirement_age + 1):
        investment_return = starting_balance * expected_return_rate
        starting_balance += total_year_contribution + investment_return

        print(f"\nAt the end of age {age}:")
        print(
            f"  Starting Balance: ${'{:,.2f}'.format(starting_balance - total_year_contribution - investment_return)}")
        print(
            f"  Overall Employee Contributions: ${'{:,.2f}'.format(employee_contributions)}")
        print(
            f"  Overall Employer Contributions: ${'{:,.2f}'.format(lifetime_employer_contributions)}")
        print(f"  Investment Return: ${'{:,.2f}'.format(investment_return)}")
        print(
            f"  Total Contributions: ${'{:,.2f}'.format(total_year_contribution)}")
        print(f"  Ending Balance: ${'{:,.2f}'.format(starting_balance)}\n")
        print('---------------------------')


def freedom():
    desired_retirement_amount = int(
        input('What is your retirement savings goal? ($): '))
    current_age = int(input("How old are you?: "))
    target_retirement_age = int(input("At what age do you want to retire?: "))
    salary = int(input("What is your annual salary? ($): "))
    monthly_contributions_percentage = int(
        input("How much would you be willing to contribute each month? (%): ")) / 100
    expected_return_rate = int(
        input("What is your expected return? (%): ")) / 100
    current_401k_balance = float(
        input("Enter your current 401(k) balance ($): "))
    employer_match = int(input("What is your employer match? (%): ")) / 100
    match_limit = int(input("What is the match limit? (%): ")) / 100

    annual_contributions_dollar_amount = round(
        salary * monthly_contributions_percentage)
    investing_years = target_retirement_age - current_age
    employee_contributions = (investing_years * 12) * \
        annual_contributions_dollar_amount
    annual_employer_contributions = (salary * match_limit * employer_match)
    total_year_contribution = annual_contributions_dollar_amount + \
        annual_employer_contributions
    starting_balance = current_401k_balance

    years = 0
    while starting_balance < desired_retirement_amount and current_age + years < target_retirement_age:

        investment_return = starting_balance * expected_return_rate

        starting_balance += total_year_contribution + investment_return

        years += 1

    if starting_balance >= desired_retirement_amount:
        print(
            f"You will reach your retirement goal of ${desired_retirement_amount:,.2f} in {years} years at age {current_age + years}.")
    else:
        print(f"Sorry, it seems unlikely to reach your retirement goal within the specified time frame.")


query = input(
    'Which program would you like to run? [Freedom][Investment]').lower()
if query == 'freedom' or query == 'f':
    freedom()
elif query == 'investment' or query == 'i':
    investment_return()
