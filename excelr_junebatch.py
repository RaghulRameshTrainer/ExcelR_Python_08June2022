age=200
if age>18 and age<=100:
    print("You can vote")
    print("It is valid only for indian citizen")
    print("Please check your own contry standards if you are from other country")
elif age<0 or age>100:
    print("Invalid age. Please check")
elif age==0:
    print("You are a just born baby!")
else:
    print("You cannot vote")
    print("Because you are less than 18 years old")
    print("Out of conditional statement")