# Estimate the time left for you to live.

# 🚨 Don't change the code below 👇
age = int(input("What is your current age: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ggg = int(input('How many years do you wish to live for: '))
years_remaining = ggg - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
hours_remaining = years_remaining * 8765
minutes_remaining = years_remaining * 525600
seconds_remaining = years_remaining * 31,536,000

outcome = (f"You have {years_remaining} years,{months_remaining} months, {weeks_remaining} weeks, {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes and {seconds_remaining} seconds remaining on earth, so please maximize each second.")

print(outcome)

# Open to learning how to leap year calculation separately and other ways to write the code to arrive at the same result.

