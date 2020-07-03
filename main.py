def galgje():

 import random
 #zorgt dat er een random woord wordt gekozen uit de lijst

 words= ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier','fotografie', 'waardebepaling', 'specialiteit', 'verzekering','universiteit','heesterperk']
 #alle woorden waar de computer uit kan kiezen

 word = random.choice(words)  
 #definieert wat de variabele 'word' is en laat computer random woord kiezen

 print('Welkom bij lama galgje!')

 naam = input("Hoe heet je? ") 
  #vraagt om naam/input gebruiker

 def printHallo(naam):
   print('Hallo ' + naam + ', veel plezier!')
   #gepersonaliseerde welkomsboodschap

 printHallo(naam)

 print('Je mag geen cijfers invoeren en je mag slechts 1 letter tegelijk raden. Als je een cijfer intoetst gaat dit niet van je beurten af, maar als je meer letters tegelijk probeert te raden gaat er wel een beurt af. Je mag door zolang je nog beurten hebt.')
 #spelregels
 print('Je hebt 5 beurten! Het woord is', + len(word), 'letters lang')
 #geeft weer hoe lang het woord is

 guesses = ''

 turns = 5 
  #zorgt dat er max. 5 beurten zijn

 guessed =[]
 #lijst met (fout) geraden letters

 while turns > 0: 
     #wat er gebeurt als er nog beurten zijn 
     
    failed = 0 
    #aantal keer dat er fouten worden gemaakt
    
    for letter in word: 
        
        if letter in guesses:  
            print(letter) 
        
        else:  
            print("_") 
           #laat aantal letters zien en de goed geraden letter op de juiste plek 
            failed +=1
           #het aantal fouten neemt met 1 toe

    if failed == 0: 
        
        print(naam, ', je hebt gewonnen, gefeliciteerd!')  
        print("Het woord is: ", word)  
        opnieuw()
        #winnaarsbericht en vraag opnieuw te spelen
        
    guess= input("Raad een letter:").lower()
    #vraagt om input gebruiker en zorgt dat het niet uitmaakt of het een grote of kleine letter is die wordt ingevoerd

    if guess.isnumeric() == True:
     print('Je mag geen cijfers gebruiken!')
     #zorgt ervoor dat er een foutboodschap komt bij invoer van een getal

    guesses += guess  
    #laat de computer de geraden letter bij de guesses opslaan

    if ( guess not in word and guess.isalpha()and len(guess) ==1):
      #dus dit gebeurt alleen als de letter niet in het woord zit en dus een letter (en geef cijfer is)

        turns -= 1
         #aantal beurten neemt met 1 af 
       
        print("FOUT") 
        print("Je hebt nog maar", + turns, 'beurten!')

        guessed.append(guess)
        guessed.sort()
        #zorgt ervoor dat de fout geraden letters in een lijst komen die ook op alfabetische volgorde staat

        print('Deze letters zitten niet in het woord:', guessed)

    if len(guess) >1 and guess.isalpha():
     print('Je mag slechts 1 letter per keer raden!')
     turns -= 1
     print("Je hebt nog maar", + turns, 'beurten!')
     #als de lengte van de invoer langer dan 1 karakter is neemt het aantal beurten met 1 af en wordt er een foutboodschap getoond

    if turns == 0: 
            print(naam,', je hebt verloren, jammer joh!') 
            print("Het woord is: ", word)
            opnieuw()
            #verliesbericht voor als beurten op zijn

def opnieuw():
 restart = input("Wil je opieuw spelen?").lower()
 
 if restart == 'ja':
   galgje()
 
 elif restart == 'nee':
   print('Bedankt voor het spelen, tot ziens!')
   exit()
#functie voor het opnieuw spelen van het spel, bij ja gaat het spel opnieuw anders stopt het

galgje()
#laat het spel beginnen
