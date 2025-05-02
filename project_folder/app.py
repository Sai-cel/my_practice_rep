import pandas as pd

df=pd.read_csv("data_set_folder/data1.txt")
final_data = df

def function(a,b,c,d):
    return a+b+c

print(function(3,4,5,8))


def function1(a,b,c,d,f):
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e =int(f)
    return a+b+c+d+e

print(function1(4,5,6,7,8))