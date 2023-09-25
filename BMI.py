#BMI IN PYTHON 🥰

c = input("type man or woman : ")
if c == "man":
    weight = int(input("👨Enter Your Weight : (kg) : "))
    height = float(input("Enter Your Height : (Foot) : "))
    age = int(input("Enter your age in years : "))
    cm = height / 30.48
    manAns = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age ) 
    print("🥰  ", manAns)

elif c == "woman":
    wweight = int(input("👩Enter Your Weight : (kg) : "))
    wheight = float(input("Enter Your Height : (Foot) : "))
    wage = int(input("Enter your age in years : "))
    wcm = wheight / 30.48 
    woemanAns = 447.593 + (9.247 * wweight) + (3.098 * wcm) - (4.330 * wage)
    print("🥰  ",woemanAns)
else:
    print("🤸‍♂️")
