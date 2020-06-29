import random
#zorgt dat er een random woord wordt gekozen uit de lijst

words= ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier','fotografie', 'waardebepaling', 'specialiteit', 'verzekering','universiteit','heesterperk']
#alle woorden waar de computer uit kan kiezen

word = random.choice(words)  
#definieert wat de variabele 'word' is

print('Je hebt 5 beurten! Het woord is', len(word), 'letters lang')
#geeft weer hoe lang het woord is

guesses =''

turns = 5 
#zorgt dat er max. 5 beurten zijn

while turns > 0: 
     #wat er gebeurt als er nog beurten zijn 
     
    failed = 0 
      
    
    for letter in word:  
          
        
        if letter in guesses:  
            print(letter) 
              
        else:  
            print("_") 
           #laat aantal letters zien en de goed geraden letter op de juiste plek 
            

    guess = input ('Raad een letter! Of raad het woord als je  het al weet!')
    #vraagt om input speler

    guesses += guess  
    #laat de computer onthouden welke letters al zijn geraden

     
    if guess not in word: 
          
        turns -= 1
          
       
        print("FOUT") 
          
       
        print("Je hebt nog maar", + turns, 'beurten!')
        #zorgt dat er een beurt af gaat als de geraden letter niet in het woord zit 
        if turns == 0: 
            print('Je hebt verloren, jammer joh!') 
            print("Het woord is: ", word)
            #verliesbericht voor als beurten op zijn
   
      
   
     
          
          
       

             

