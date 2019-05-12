#Unit Converter

"""
text:
purpose = Hello dear sir and/or madam. This program is used for converting kilometres into miles.
text = Please enter the kilometre number you wish to convert into miles.
question = Do you want another conversion?
ym = yes/no:
"""



purpose = "Hello dear sir and/or madam. This program is used for converting kilometres into miles."
print (purpose)

print("")

text = "please enter the kilometre number you wish to convert into miles."
print (text)

km = float(input("Kilometres: "))
miles = round(float(km)*0.621,2)
print(str(km)+ " kilometres = " + str(miles)+" miles")

while True:
    print("Do you want another conversion?")
    yn = (input("yes/no: "))

    if yn == "yes":
        print(text)
        km = float(input("Kiloemtres: "))
        miles = round(float(km)*0.621,2)
        print(str(km)+ " kilometres = " + str(miles)+" miles")

    else:
        print("Thank you for using our program. Have a nice day and goodbye.")
        break



























