def max(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0
    for x in arr:
        if x: streak +=1
        else: streak = 0
        if streak> best: best = streak
    return best
i = int(input("Enter a number : "))
print(max(i))