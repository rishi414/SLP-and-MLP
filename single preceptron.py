x1=1
w1=0.2
target=2
def active(z):
    return z
max=5
for i in range(max):
    z=w1*x1
    y=active(z)
    err=target-y
    if(err==0):
        print("output accured:",y)
        break
    print("Not equal to target, current output:", y)
    w1=w1+err
