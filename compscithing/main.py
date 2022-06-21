alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
editedAlphabet = ['c','f','l','k','%','o', 'm', '&', 'z', 'p', '$', 'n', 'q', 't', 'v', 'd', 'j', '#', '@', 'r', 'w', 'x', 's', 'y', 'u']

phrase = input("Enter your phrase: ")
phraseList = list(phrase)
newPhrase = ''
distance = input("Enter your phrase: ")

for i in range(0, len(alphabet)):
  for j in range(0, len(phraseList)):
    if phraseList[j] == alphabet[i]:
      newPhrase += editedAlphabet[i]


print(newPhrase)
