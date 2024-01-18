def f(x, y):
    if x >=0 and y >= 0:
        return x + y
    
    elif x >=0 and y <= 0:
        return x + y**2
    
    elif x <=0 and y >= 0:
        return x**2 + y
    
    elif x <=0 and y <= 0:
        return x**2 + y**2

print(f(2,3))