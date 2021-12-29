a={"a":1,"b":2,"c":3,"d":4,"e":5}
b=1
for i in a:
    b=b*a[i]
    # b*=a[i]
print(b)