rate1 = 0.10
rate2 = 0.25
rate1_single_limit = 3200
rate1_married_limit = 64000

marital_status = input(" Please enter 's' for single, 'm' for married: ")
income = float(input("please enter your income : "))

tax1 = 0
tax2 = 0

if marital_status == 's':
   if income <= rate1_single_limit:
       tax1 = rate1 * income
   else:
      tax1 = rate1 * rate1_married_limit
      tax2 = rate2 * (income- rate1_single_limit)
else:
    if income <= rate1_married_limit:
        tax1 = rate1 * income
    else:
        tax1 = rate1 * rate1_married_limit
        tax2 = rate2 * (income- rate1_married_limit)
total_tax = tax1 + tax2

print("The tax is %.2f" % total_tax)

richter = float(input("Enter a magnitude on the Richter scale: "))
if richter >= 8:
    print("Most structures fall.")
elif richter >= 7:
    print("many building destroyed.")
elif richter >= 6:
    print("many building considerably.")
elif richter >= 4.5:
    print("Damage to poorly constructed.....")
elif richter >= 0:
    print("No damage!.")
else: 
    print("Invalied magnitude")

#Boolean operator examples
string = "Python"
print("P" in string)