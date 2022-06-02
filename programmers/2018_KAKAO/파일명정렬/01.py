def fileNmParser(f):
    endOfH = -1
    endOfN = len(f)

    for idx, l in enumerate(f):
        if l.isdigit():
            endOfH = idx
            for idx2, ll in enumerate(f[idx:]):
                if not ll.isdigit():
                    return f[:idx].lower(), int(f[idx : idx + idx2]), idx
            return f[:endOfH].lower(), int(f[endOfH:endOfN]), idx

    return f[:endOfH].lower(), int(f[endOfH:endOfN]), idx


def solution(files):
    files.sort(key=lambda x: fileNmParser(x))
    return files


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))


["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
["IMG01.GIF", "img1.png", "img2.JPG", "img02.png", "img10.png", "img12.png"]
