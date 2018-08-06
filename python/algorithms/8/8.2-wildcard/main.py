

def match(w, s):
    pos = 0
    while pos < len(w) and pos < len(s) and (w[pos] == '?' or w[pos] == s[pos]):
            pos += 1


    if pos == len(w):
        return pos == len(s)

    if w[pos] == '*':
        for skip in range(len(s) + 1):
            if match(w[pos+1:], s[pos+skip:]):
                return True

    return False





C = int(input())
for _ in range(C):
    wildcard_pattern = input()
    N = int(input())
    for _ in range(N):
        word = input()
        if match(wildcard_pattern, word):
            print(word)
