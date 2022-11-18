# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))
def convert(kilometers,conv_fac = 0.621371):
    # calculate miles
    miles = kilometers * conv_fac
    return miles


print(f'{kilometers} kilometers is equal to {convert(kilometers)} miles')