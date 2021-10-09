import sys
sys.stdin = open("input.txt")

cnt = 0

for ts in range(int(input())):
    word = input()
    length_of_word = len(word)
    flag = True
    check_set = {word[0]}
    for idx in range(1, length_of_word):
        letter = word[idx]
        if letter not in check_set:
            check_set.add(letter)
        elif letter == word[idx-1]:
            continue
        else:
            flag = False
            break
    if flag:
        cnt += 1
'''
for ts in range(int(input())):
    check_list = [0]*26
    word = input()
    length_of_word = len(word)
    flag = True

    check_list[ord(word[0])-97] += 1

    for idx in range(1, length_of_word):
        letter = word[idx]
        if check_list[ord(letter)-97] == 0:
            check_list[ord(letter)-97] += 1
        elif letter == word[idx-1]:
            check_list[ord(letter)-97] += 1
        else:
            flag = False
            break
    if flag:
        cnt += 1
'''
    
print(cnt)