def Compound_Interest():
    print("COMPOUND INTEREST CALCULATOR")

Compound_Interest()

P = float(input("Principal?: "))
R = float(input("Rate?: "))
T = float(input("Time?: "))
n = float(input("Number of compoundments?: "))

Q = R/n
a = n * T
M = (1 + Q)
S = (M**a)
Result = (P * S)

print(Result)