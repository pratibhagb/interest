def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    return si
if __name__ == "_main_":
    p=float(input("Enter principal amount:"))
    r=float(input("Enter rate of interest:"))
    t=float(input("Enter time:"))
    result=simple_interest(p,t,r)
    print("Simple interest:",result)