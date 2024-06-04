age = int(input("Enter age: "))

if age<13:
    group="Child"
elif (age<20):
    group="Tenegar"
elif age<60:
    group="Adult"
else:
    group="Senior"

print(group)
