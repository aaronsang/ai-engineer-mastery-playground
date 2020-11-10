"""
Tip calculator
"""
total_bill = float(input('Welcome to the tip calculator. What was the total bill? '))
tip = int(input('Thank you! What percentage tip would you like to leave? ')) / 100
people = int(input('How many people shared this meal? '))
final_bill = (total_bill * tip + total_bill) / people
print(f'Each person should pay ${round(final_bill, 2)}')
