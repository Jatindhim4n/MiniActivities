#1

Inches=int(input("Enter your Length (in inches)"))
Centimete=Inches * 2.54
print(f'Length in centimeter is {Centimete}')

#2
Kilogram=int(input("Enter your weight in KG"))
Stones=Kilogram * 0.157473
print(f'Weight in stones is {Stones}')

#3a
firstno=int(input("enter first no. of your binary no."))
secondno=int(input("enter second no. of your binary no."))
thirdno=int(input("enter third no. of your binary no."))
fourthno=int(input("enter your fourth no. of binary no."))

Your_binary_no = firstno+secondno+thirdno+fourthno

print(f'you entered ={firstno}{secondno}{thirdno}{fourthno}')

binary=(2**0)*firstno+(2**1)*secondno+(2**2)*thirdno+(2**3)*fourthno

print(f'This binary number in base ten is:{binary}')

#3c
no = int(input("Enter your number: "))


n1 = no % 2
q1 = no // 2
n2 = q1 % 2
q2 = q1 // 2
n3 = q2 % 2
q3 = q2 // 2
n4 = q3 % 2
q4 = q3 // 2
n5 = q4 % 2
q5 = q4 // 2
n6 = q5 % 2
q6 = q5 // 2
n7 = q6 % 2
q7 = q6 // 2
n8 = q7 % 2
q8 = q7 // 2
n9 = q8 % 2
q9 = q8 // 2
n10 = q9 % 2
q10 = q9 // 2
n11 = q10 % 2
q11 = q10 // 2
n12 = q11 % 2
q12 = q11 // 2
n13 = q12 % 2
q13 = q12 // 2
n14 = q13 % 2
q14 = q13 // 2
n15 = q14 % 2
q15 = q14 // 2
n16 = q15 % 2
q16 = q15 // 2
n17 = q16 % 2


binary_number = f"{n17}{n16}{n15}{n14}{n13}{n12}{n11}{n10}{n9}{n8}{n7}{n6}{n5}{n4}{n3}{n2}{n1}"




print(f"Binary Number: {binary_number}")

#4a

x = 0b10  # Binary 10 (2 in decimal)
y = 0b11  # Binary 11 (3 in decimal)

print(x & y)  # Bitwise AND
print(x | y)  # Bitwise OR
print(~x)     # Bitwise NOT
print(~y)     # Bitwise NOT

#4c

num = int(input("Enter a decimal number: "))
binary = bin(num)
print(f"Binary equivalent of {num} is {binary}")

#b

binary_input = input("Enter a binary number (e.g., 0b1101 or 1101): ")


if binary_input.startswith("0b"):
    binary_input = binary_input[2:]

decimal_value = int(binary_input, 2)
print(f"Decimal equivalent of {binary_input} is {decimal_value}")



