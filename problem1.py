n = int(input())
arr = list(map(int, input().split()))

cnt_5 = 0
cnt_bad = 0
max_cnt_5 = -1
start = 0

for end in range(n):
    if arr[end] == 5:
        cnt_5 += 1
    elif arr[end] <= 3:
        cnt_bad += 1
    
    while end - start + 1 > 7:
        if arr[start] <= 3:
            cnt_bad -= 1
        elif arr[start] == 5:
            cnt_5 -= 1

        start += 1
    
    if cnt_bad == 0 and end - start + 1 == 7:
        max_cnt_5 = max(cnt_5, max_cnt_5)
    
print(max_cnt_5)