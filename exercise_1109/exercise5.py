def outter_fun(a,b):
    def inner_fun(a,b):
        return a+b

    sum = inner_fun(a,b) + 5
    return sum

ans = outter_fun(5,10)
print(ans)
