sp = 800
cp = 500
if(cp == sp):
    print("No Profit")
elif (sp > cp):
    profit = sp - cp
    print("Profit : ", profit)
else:
    loss = cp - sp
    ("loss : ", loss)