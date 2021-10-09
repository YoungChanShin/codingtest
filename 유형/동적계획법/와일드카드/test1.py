import sys
sys.stdin = open("input.txt")

croatian_alphabet = ["c=","c-", "dz=", "d-", "lj", "nj", "s=", "z="]
croatian_word = input()
len_of_word = len(croatian_word)
cache_word = ""
cnt = 0
for idx in range(len_of_word):
    letter = croatian_word[idx]
    if cache_word == "":
        if letter == "c" or letter == "d" or letter == "l" or letter == "n" or letter == "s" or letter == "z":
            cache_word = letter
        else:
            cnt += 1
            
    elif cache_word == "c":
        if letter == "=" or letter == "-":
            cache_word = ""
        else:
            cache_word = letter
        cnt += 1
    
    elif cache_word == "l" or cache_word == "n":
        if letter == "j":
            cache_word = ""
        else:
            cache_word = letter
        cnt += 1
    
    elif cache_word == "z" or cache_word == "s":
        if letter == "=":
            cache_word = ""
        else:
            cache_word = letter
        cnt += 1

    # "dz=", "d-"
    elif cache_word == "d":
        if letter == "-":
            cache_word = ""
            cnt += 1
        elif letter == "z":
            cache_word = "dz"
        else:
            cache_word = letter
            cnt += 1
    
    elif cache_word == "dz":
        if letter == "=":
            cache_word = ""
            cnt += 1
        else:
            cache_word = letter
            cnt += 2
    else:
        cnt += 1
        cache_word = letter

if cache_word != "":
    cnt += len(cache_word)
print(cnt)
        