import re


def solution(new_id):
    new_id = degree_1(new_id)
    new_id = degree_2(new_id)
    new_id = degree_3(list(new_id))
    new_id = degree_4(new_id)
    new_id = degree_5(new_id)
    new_id = degree_6(new_id)
    new_id = degree_7(new_id)

    return new_id


def degree_1(text):
    return text.lower()


def degree_2(text):
    return re.sub(r'[^a-z0-9-_.]', '', text)


def degree_3(text):
    arr = []
    index = 0
    size = len(text) - 1
    for i in range(size):
        if text[i] == '.':
            if i == 0:
                index = 0
            else:
                if index + 1 == i:
                    arr.append(i)
                index = i

    index = 0
    for i in range(len(arr)):
        text.pop(arr[i] - index)
        index = index + 1

    return text


def degree_4(text):
    while len(text) > 0 and text[0] == '.':
        text.pop(0)

    while len(text) > 0 and text[len(text) - 1] == '.':
        text.pop(len(text) - 1)

    return text


def degree_5(text):
    if len(text) == 0:
        text.append('a')
    return text


def degree_6(text):
    while len(text) > 15:
        text.pop(len(text) - 1)

    while len(text) > 0 and text[len(text) - 1] == '.':
        text.pop(len(text) - 1)

    return text


def degree_7(text):
    while len(text) < 3:
        text.append(text[len(text) - 1])

    return ''.join(text)

new_id = "aaaaaaaaaaaa..s"
new_id = ".bb."
new_id = "a.a"
new_id = "a.a"
print(solution(new_id))