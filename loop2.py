principal = float(input("What is your principal?"))
rate = float(input("What is your interest rate?"))
term =  int(input("What is term?"))
totalInterest = 0
for i in range (term):
    interest = principal * rate
    print(i, round(principal, 2) , round(interest, 2))
    principal = principal + interest
    totalInterest = totalInterest + interest
    print("Total interest is:", round(totalInterest, 2))
    print("Total princia; is:, ", round(principal, 2))
 
