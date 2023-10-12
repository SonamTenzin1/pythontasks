day = input("enter day ")

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday']:
    print("Weekday")

elif day == "Friday":
    print('TGIF')

elif day in ['Saturday', 'Sunday']:
    print('weekend')

else :
    print('Invalid output')