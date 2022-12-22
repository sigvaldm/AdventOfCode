
x = [[1, 3], [8,11], [7, 9], [2, 6], ]

def union_of_intervals(intervals):
    # Given a list of intervals, 
    x = sorted(intervals, key=lambda a: a[0])
    i = 0
    while i<len(x)-1:
        f, t = x[i]
        fn, tn = x[i+1]
        if f < fn < t:
            if tn > t:
                x[i][1] = tn
            del x[i+1]
        else:
            i += 1
print(x)
