converted_terms = dict()
# converted_terms = {'A': 6, 'B': 12, 'C': 3}

def convert_terms(terms):
    for term in terms:
        t, l = term.split(' ') # "A 6"
        converted_terms[t] = int(l)

def convert_privacy_date_input(d):
    # "2021.05.02"
    yyyy, mm, dd = map(int, d.split('.'))
    return dd + mm*28 + (yyyy-2022)*12*28

def is_valid(today, d, t):
    converted_today = convert_privacy_date_input(today)
    converted_date = convert_privacy_date_input((d))
    expiration_date = converted_date + 28*converted_terms[t]
    if expiration_date <= converted_today:
        return False
    return True

def solution(today, terms, privacies):
    answer = []
    convert_terms(terms)
    
    for idx, privacy in enumerate(privacies):
        d, t = privacy.split(' ') # "2021.05.02", "A"
        if not is_valid(today, d, t):
            answer.append(idx+1)

    return answer

today = '2022.05.19'
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

result = solution(today, terms, privacies)
print(result)