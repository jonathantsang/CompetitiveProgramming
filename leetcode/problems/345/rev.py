def reverseVowels(s):
    vowels = []
    word = []
    c = 0
    for n in range(0, len(s)):
        if(checkvowel(s[n])):
            vowels.append(s[n])
        word.append(s[n])
    for n in range(len(word)-1, -1, -1):
        if(checkvowel(word[n])):
            word[n] = vowels[c]
            c += 1
    return "".join(word)
                
            
        

def checkvowel(s):
    if ((s == "a") or (s == "e") or (s == "i") or (s == "o") or (s == "u")) \
    or ((s == "A") or (s == "E") or (s == "I") or (s == "O") or (s == "U")):
        return True
    return False