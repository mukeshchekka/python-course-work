#find the runner
arr = list(map(int,input().split()))
arr = list(dict.fromkeys(arr))
a=sorted(arr)
maximum=max(a)
a.remove(maximum)
print(a[-1])
