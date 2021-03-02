import sys
sys.stdin = open("input.txt")
def match(w,s):
    pos = 0
    while (pos < len(s) and pos<len(w) and (w[pos]=="?"or w[pos] == s[pos])):
        pos +=1
        if (pos == len(w)):
            return pos == len(s)
        if (w[pos] == "*"):
            for skip in range(len(s)- pos + 1):
                if (match(w[pos+1:], s[pos+skip:])):
                    return True
    return False

for ts in range(int(input())):
    