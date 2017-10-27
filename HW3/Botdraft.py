print('Hi! I am bot =) I can answer questions... Write "bye" for the end of conversation')
a = {
'How are you?': 'I am fine, thank you =)',
'What is your name?': 'My name is Bot'
}
while True:
    question = input('Your question:   ')
    if ("?" in question):
        keys = list(a)
        found = False
        for key in a.keys():
             if key == question:
                found = True
        if found:
            print(' ', a[question])
        if not found:
            print('Hmmm...' + question)
            answer = input('Your answer:   ')
            a[question] = answer
    if question == 'bye': break
    if ("?" not in question):
        print('...')
