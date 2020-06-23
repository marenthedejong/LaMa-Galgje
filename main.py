import random
#zorgt dat er een random woord wordt gekozen uit de lijst

words= ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier','fotografie', 'waardebepaling', 'specialiteit', 'verzekering','universiteit','heesterperk']
#alle woorden waar de computer uit kan kiezen


word = random.choice(words)  
#definieert wat de variabele 'word' is

print('Je hebt 5 beurten! Het woord is', len(word), 'letters lang')
#geeft weer hoe lang het woord is

guess = input ('Raad een letter! Of raad het woord als je het al weet!')
#vraagt om input speler 