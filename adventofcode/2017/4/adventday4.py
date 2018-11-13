f = open("adventday4text.txt")

valid_passphrases_p1 = 0
valid_passphrases_p2 = 0
for line in f.readlines():
    passphrases = []
    invalid_p1 = False
    invalid_p2 = False
    for word in line.split():
        passphrases.append(word)
    # Prevent a false positive where the word will check against itself
    for first_word in range(len(passphrases) - 1):
        for second_word in range(first_word + 1, len(passphrases)):
            if passphrases[first_word] == passphrases[second_word]:
                invalid_p1 = True
            if sorted(list(passphrases[first_word])) == sorted(list(passphrases[second_word])):
                invalid_p2 = True
    if not invalid_p1:
        valid_passphrases_p1 += 1
    if not invalid_p2:
        valid_passphrases_p2 += 1

print valid_passphrases_p1, valid_passphrases_p2
