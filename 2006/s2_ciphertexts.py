

# IMPORTANT INFO

# THE EDGE CASE IN THIS QUESTION IS THAT IF YOU ARE GIVEN 26 OF THE 27
# POSSIBLE CHARACTERS, YOU NEED A WAY TO AUTOFILL THAT LAST CHARACTER,
# SINCE YOU TECHNICALLY ALREADY KNOW IT IF YOU HAVE 26 OUT OF 27.
#
# IF YOU DO NOT ACCOUTN FOR THIS, YOU ONLY GET 30/1050



cipher = {}
plaintext = input()
ciphertext = input()
new_cipher = input()

keyset = []
valset = []
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
    keyset.append(c)
    valset.append(c)

for i in range(len(plaintext)):
    if ciphertext[i] not in cipher:
        cipher[ciphertext[i]] = plaintext[i]
    if ciphertext[i] in keyset:
        keyset.remove(ciphertext[i])
    if plaintext[i] in valset:
        valset.remove(plaintext[i])

if len(keyset) == 1:
    cipher[keyset[0]] = valset[0]

message = ""
for c in new_cipher:
    if c in cipher:
        message += cipher[c]
    else:
        message += "."

print(message)