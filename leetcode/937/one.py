# ['1', 'A', 'a']


def solution1(logs):
    letters = []
    nums = []
    for idx, l in enumerate(logs):
        identificator, content = l.split()[0], " ".join(l.split()[1:])
        if content[0].isdigit():
            nums.append(l)
        else:
            letters.append((identificator, content))
    letters.sort(key=lambda x: (x[1], x[0]))
    ret = []
    for l in letters:
        ret.append(l[0] + " " + l[1])
    ret.extend(nums)
    return ret


def solution(logs):
    letters = []
    nums = []
    for idx, l in enumerate(logs):
        identificator, content = l.split()[0], " ".join(l.split()[1:])
        if content[0].isdigit():
            nums.append(l)
        else:
            letters.append(l)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + nums


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
Output = [
    "let1 art can",
    "let3 art zero",
    "let2 own kit dig",
    "dig1 8 1 5 1",
    "dig2 3 6",
]

logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
Output = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
print(solution1(logs))
