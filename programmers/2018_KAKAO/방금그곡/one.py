# C, C#, D, D#, E, F, F#, G, G#, A, A#, B
def convertTime(t):
    h, m = map(int, t.split(":"))
    return 60 * h + m


def solution(m, musicinfos):
    answer = "(None)"
    answerPlayLength = 0
    m = (
        m.replace("A#", "U")
        .replace("C#", "W")
        .replace("D#", "X")
        .replace("F#", "Y")
        .replace("G#", "Z")
    )

    for mi in musicinfos:
        st, et, nm, melody = mi.split(",")
        st, et = map(convertTime, [st, et])
        playTime = et - st + 1

        melody = (
            melody.replace("A#", "U")
            .replace("C#", "W")
            .replace("D#", "X")
            .replace("F#", "Y")
            .replace("G#", "Z")
        )

        melodyLen = len(melody)
        fullMelody = melody * (playTime // melodyLen)
        fullMelody += melody[: playTime % melodyLen]

        if m in fullMelody:
            if answerPlayLength < playTime:
                answerPlayLength = playTime
                answer = nm
    return answer


m = "DEA"
musicinfos = ["12:00,12:10,HELLO,ABCDE", "13:00,13:13,WORLD,ABCDEF"]

print(solution(m, musicinfos))