origin = input('Enter a word:')

word = origin.lower()
new_word =""

for x in range(len(word)):
    new_letter = origin[len(word)-1-x]
    new_word = new_word + new_letter
    if new_letter == 'i':
        new_word = new_word[0:len(new_word)-1] + '1'
    elif new_letter == 'a':
        new_word = new_word[0:len(new_word)-1] + '@'
    elif new_letter == 'o':
        new_word = new_word[0:len(new_word)-1] + '0'

new_word = new_word + "b@1"
print(new_word)
