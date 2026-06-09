ransomNote = "aa"
magazine = "aab"

def main(magazine, ransomNote):
    for i in ransomNote:
        if i not in magazine:
            return False
        magazine = magazine.replace(i,"",1)
    return True


print(main(magazine, ransomNote))