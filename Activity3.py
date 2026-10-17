def max_one(n):
    arr = [1] + [0]*n + [1]
    streak = best = 0
    for x in arr:
        if not x: streak +=1
        else: streak = 0
        if streak>best: best = streak 
    return best
print("The streak for 3 is : ", max_one(3))
print("The streak for 5 is : ",max_one(5))
p = int(input("Enter a number : "))
print(max_one(p))