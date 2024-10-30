print("Profit finder")

print("Enter your cost and selling price below")

cost=int(input("Write your cost price"))
selling=int(input("Write your selling price"))

profit=selling-cost

if profit>=0 :
     print("You have made a profit of", profit)

else:
     print("You have lost", profit)
     