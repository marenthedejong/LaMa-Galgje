import random
#zorgt dat er een random woord wordt gekozen uit de lijst

words= ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier','fotografie', 'waardebepaling', 'specialiteit', 'verzekering','universiteit','heesterperk']
#alle woorden waar de computer uit kan kiezen


word = random.choice(words)  
#definieert wat de variabele 'word' is

guess = input ('Raad een letter! Of raad het woord als je het al weet!')
#vraagt om input speler 