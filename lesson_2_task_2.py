def is_year_leap(a):
    if a%4 == 0:
        return True
    else:
        return False
a = int(input())    
b =   is_year_leap(a)
print('год',a,end = ":")
print(b)  