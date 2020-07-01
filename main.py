def galgje():

 import random
 #zorgt dat er een random woord wordt gekozen uit de lijst

 words= ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier','fotografie', 'waardebepaling', 'specialiteit', 'verzekering','universiteit','heesterperk']
 #alle woorden waar de computer uit kan kiezen

 word = random.choice(words)  
 #definieert wat de variabele 'word' is en laat computer random woord kiezen

 print('Welkom bij lama galgje!')

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
        
        print('Je hebt gewonnen, gefeliciteerd!')  
        print("Het woord is: ", word)  
        opnieuw()
        #winnaarsbericht en vraag opnieuw te spelen
        
    guess = input("Raad een letter:")
    
    guesses += guess  
    #laat de computer onthouden welke letters al zijn geraden 

    if guess not in word:
          
        turns -= 1
         #aantal beurten neemt met 1 af 
       
        print("FOUT") 
        print("Je hebt nog maar", + turns, 'beurten!')

        guessed.append(guess)
        guessed.sort()
        #zorgt ervoor dat de fout geraden letters in een lijst komen die ook op alfabetische volgorde staat

        print('Deze letters zitten niet in het woord:', guessed)

        if turns == 0: 
            print('Je hebt verloren, jammer joh!') 
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
#functie voor het opnieuw spelen van het spel

galgje()
#laat het spel beginnen

  

    
         



    
            
    

    
      
   
      
   
     
          
          
       

             

