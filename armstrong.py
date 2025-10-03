num = int(input("Enter a number: "))
order = len(str(num))
sumpowers = sum(int(digit) ** order for digit in str(num))
if num == sumpowers:
    print(num, "is an armstrong number.")
else:
    print(num, "is not an armstrong number.")

 

