a = [4,2,6]
b = [1,2,3]

listsum = []
for i in range(len(a)):
    listsum.append([a[i],b[i]])

new_list = sorted(listsum, key=lambda x: x[0])
print(new_list)
