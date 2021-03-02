cnt = 2
# for i in range(4):
#     print(i)
#     if i==3:
#         break
# else:
#     print("break")

for i in range(4):
    cnt += 1
    if cnt>3:
        cnt -= 4

print(cnt)
# else는 break를 만나지 못했을 때 발생