birth_y = int(input('enter your bith year='))
age = 2024
Your_age_now = int(age) - int(birth_y)
print('Your age right now=', Your_age_now)

if Your_age_now > 100:
    print('congradulations')

if Your_age_now < 18:
    print('Go to school my boy')

if Your_age_now > 18 < 100:
    print('Go to work bro')