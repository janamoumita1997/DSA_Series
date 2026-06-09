ransomNote = "aa"
magazine = "aab"

def main(magazine, ransomNote):
    magazine_words = {}
    for i in magazine:
        magazine_words[i] = magazine_words.get(i,0) + 1

    for j in ransomNote:
        if j not in magazine_words:
            return False
        else:
            if magazine_words[j]>0:
                magazine_words[j] -= 1
            else:
                return False
    return True



print(main(magazine, ransomNote))