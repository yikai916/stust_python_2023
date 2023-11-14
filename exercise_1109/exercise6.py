def recursive(num):
    if num >= 0:
        return num + recursive(num-1)
    else:
        return 0

sum = recursive(100)
print(sum)