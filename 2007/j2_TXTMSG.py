slang = {'CU': 'see you',
    ':-)': "I'm happy",
    ':-(': "I'm unhappy",
    ';-)': 'wink',
    ':-P': 'stick out my tongue',
    '(~.~)': 'sleepy',
    'TA': 'totally awesome',
    'CCC': 'Canadian Computing Competition',
    'CUZ': 'because',
    'TY': 'thank-you',
    "YW": "you're welcome",
    'TTYL': 'talk to you later'
    }

while True:
    text = input()
    if text == "TTYL":
        print("talk to you later")
        break
    if text in slang:
        print(slang[text])
    else:
        print(text)
