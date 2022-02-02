def Simple_Interest():
    print("SIMPLE INTEREST CALCULATOR")

Simple_Interest()

P = float(input("Principal?: "))
R = float(input("Rate?: "))
T = float(input("Time?: "))
Result = ((P * R * T) / 100)

print(Result)