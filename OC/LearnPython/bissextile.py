year = int(input("Pleas input a Year : "))
if year % 400 == 0:
    print(" is bissextil")
elif year % 100 == 0:
    print(" is not bissextil")
elif year % 4 == 0:
    print(" is bissextil")
else:
    print(" is not bissextil")

print(type(year))