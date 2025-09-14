"""
write a program to prompt the user for hours ,rate per hour
to compute gross pay

"""

print("Please Enter your Over Time Hours : ")

hours = int(input())

print("Please Enter Rate/Hour : ")

rate = float(input())

print("Gross =  " ,hours*rate)