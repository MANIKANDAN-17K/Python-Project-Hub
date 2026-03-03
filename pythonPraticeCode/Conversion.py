def convert_to_base(n,base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    negative = False

    if n < 0 :
        negative = True
        n = -n
    
    while n > 0:
        reminder = n % base
        result = digits[reminder] + result
        n = n // base
    if negative:
        result = "-"+ result
    return result
num = int(input("Enter you number :"))
print("Binary : ",convert_to_base(num, 2))
print("Octal : ",convert_to_base(num, 8))
print("Hexadecimal : ",convert_to_base(num, 16))