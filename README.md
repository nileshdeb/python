#. Create a program to prompt the user to input their exam score and display their grade based on the score 
range. 

score = float(input("Enter your exam score: "))

if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

