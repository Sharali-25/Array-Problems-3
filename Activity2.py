def move_zeros(n):
    arr = [0,1]*n
    write =0
    for x in arr:
        if x: arr[write] = x;write +=1
    arr[write:] = [0] * (len(arr)-write)
    return arr
print("move zeros 3 = ",move_zeros(3))
print("move zeros 4 = ",move_zeros(4))
o =int(input("Enter a numberr : "))
print(move_zeros(o))