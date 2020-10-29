import string

def substitution(text, key):
    ALPHABET = list(string.ascii_uppercase)
    PLAIN_TEXT = list(text.upper())
    cypherText = ""

    for char in PLAIN_TEXT:
        if not char == '\n' or not char == ' ':
            replaceCharIndex = ALPHABET.index(char) + key
            if(replaceCharIndex > 25):
                replaceCharIndex -= 26
            cypherText = cypherText + ALPHABET[replaceCharIndex]
        else:
            cypherText = cypherText + char

    return cypherText

def decodeSubstitution(text, key):
    ALPHABET = list(string.ascii_uppercase)
    PLAIN_TEXT = list(text.upper())
    cypherText = ""

    for char in PLAIN_TEXT:
        if not char == ' ':
            replaceCharIndex = ALPHABET.index(char) - key
            if(replaceCharIndex < 0):
                replaceCharIndex += 26
            cypherText = cypherText + ALPHABET[replaceCharIndex]
        else:
            cypherText = cypherText + char

    return cypherText

def generateVigenereCipherKey(text, key):
    generatedKey = ""
    while len(generatedKey) < len(list(text)):
        generatedKey += key
    return generatedKey[0: len(text)]

def vigenere(text, key):
    key = generateVigenereCipherKey(text, key)
    cipherText = []
    for i in range(0, len(text)):
        if not ord(text[i]) == 32:
            x = ((ord(text[i]) - ord(key[i]) + 26) % 26) + 65
            print(x)
            cipherText.append(chr(x))
        else:
            cipherText.append(text[i])
    
    return("" . join(cipherText)) 


def letterFrequency(text):
    dictionary = {}
    for char in text:
        if not char == ' ':
            if char in dictionary:
                dictionary[char] = dictionary[char] + 1
            else:
                dictionary[char] = 1

    {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}

    print({k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])})

text = "wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

letterFrequency(text)