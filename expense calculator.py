exp = -1
total = 0 
maxexp = 0
minexp = 0

while exp!=0:
    exp = int(input("what is the expense? (type 0 to stop)"))
    total = total + exp
    if exp>maxexp:
        maxexp = exp


print("your total expenditure is " + str(total))
print("the maximum you spent is "+ str(maxexp))

if exp<maxexp:
        print(" the minimum expenditure is "+str(minexp))






