import time #imports a module to add a pause 
import sys
from credits import *

#figuring our how users might respond 
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]

#grabbing objects
note = 0
gun = 0
ID = 0
uniform = 0
alcohol = 0
boarding_pass = 0

def intro():
    print("\nENTRANCE\n")
    print ("""You are at the entrance to X Aiport, a small town airport with not much to see.  
    \nNext to you is the stinky, old toilet that smells like decomposing bodies. 
    \nHowever, if you ignore the odour and look straight ahead you will see the check-in desks to your right and the airport security to the left.""")
    good_ending()
    '''time.sleep(1)

    print (""" 
    A. Go to the toilet.
    B. Go straight to the check-in desk.
    C. Go straight to airport security.""")

    choice = input("\n>>> ")
    if choice in answer_A:
        toilet()
    elif choice in answer_B:
        check_in()
    elif choice in answer_C:
        security()
    else:
        print ("\nUse only A, B, or C please!\n")
        intro()'''





def toilet():
    print("\nTOILET\n")
    print("""You are in the world's most stinkiest toilet in the world. Peuhhy, you feel like fainting but you are really desperate to go.""")

    time.sleep(1)

    print("""\nOooo looks like you found a note on the floor. What would you like to do?""")

    time.sleep(1)

    print(""" 
    A. Go straight back to the entrance because you can't stand the stench.
    B. Pick up the note, go to the toilet and head to the check-in area as quick as you can. """)

    choice = input("\n>>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        note = 1
        time.sleep(1)
        print("\nNOTE: You are in a battle royale. Be careful out there and good luck!")
        time.sleep(1)
        check_in()
    else:
        print ("\n Use only A or B\n")
        toilet()

def check_in():
    print("\nCHECK-IN AREA\n")
    print("""You are now in the check-in area where you obviously check in your luggage, but it looks a bit empty. 
    \nIf you are feeling a little creeped out, you could always run back to the entrance.""")

    time.sleep(1)

    print("\nYou notice a shiny card in the bin on the way to the check-in desk. What would you like to do?")

    time.sleep(1)

    print("""
    A. Go straight to airport security now because you are in a hurry.
    B. Pick the card up and then proceed to the security screening area.
    C. Head back to the entrance because you are petrified.""")

    choice = input("\n>>> ")
    if choice in answer_A:
        security()
    elif choice in answer_B:
        boarding_pass = 1
        print ("Ahhh it was a boarding pass...This might come in handy!")
        time.sleep(1)
        security()
    elif choice in answer_C:
        intro()
    else:
        print("\n Use only A or B\n")
        check_in()

def security():
    print("\nSECURITY SCREENING AREA\n")
    print("""You are standing in the most feared area, also known as the security screening. 
    \nAgain, this area seems to be lacking passengers, so you wonder when the guards appeared.
    \nHmmmmmm...""")

    time.sleep(1)

    print("\nAs you walk towards the large scanning machines, one security guard abruptly asks 'What are you doing at this airport?")

    time.sleep(1)

    print("""
    A. I don't know you tell me!
    B. Ummm... ummm.. I'm going to Paris... I think??
    C. I'm going to Spain! 
    D. Oh.. let me go and check where I'm heading to...""" )

    choice = input(">>>")
    if choice in answer_A:
        print("The security guard doesn't look too pleased. ")
        time.sleep(1)
        if note < 0:
            print("""He punches you several times until he made sure you DIED... 
            YOU'RE DEAD, GAME OVER!!""")
            intro()
        else:
            print("The security guard becomes aggressive towards you, so he punches until you DIE!!! \n YOU'RE DEAD, GAME OVER!")
            intro()
            
    elif choice in answer_B:
        print("The security guard doesn't look too pleased.")
        time.sleep(1)
        if note != 1:
            print("""He punches you several times until he made sure you DIE... 
            YOU DEAD, GAME OVER!!""")
        else:
            print("\nThe security guard becomes aggressive towards you, so he punches until you DIE!!! \n YOU'RE DEAD, GAME OVER!")
            intro()
            
    elif choice in answer_C:
        print("The security guard laughs and lets you through...")

        if note != 1 and boarding_pass != 1:
            time.sleep(1)
            print("""The guard's face turned sour, he doesn't look too pleased... 
            When you laid your eyes towards the duty free shops, He directs a forceful punch to your stomach...""")
            time.sleep(1)
            print("YOU'RE DEAD, GAME OVER!!")
            intro()
        else:
            print("""\nYou knew the whole thing is a set up, so you FLING your boarding pass to the guards neck... 
            \nHis neck sliced open which led his colleagues to chase you, but you fought through with your bare hands.
            \nNow, the whole screening area is covered with corpses... The corpses YOU killed with your bare hands... 
            \nSince you silently chopped everyone there, you can now take their gun, uniform and ID. 
            \nDo you want them? Y/N""")
            choice = input(">>>")
            if choice in yes:
                gun = 1
                uniform = 1
                ID = 1
                duty_free()
            else:
                duty_free()
          
            
    elif choice in answer_D:
        print("Security: You come over here... Let me check your passport.")
        if note < 0 and boarding_pass < 0:
            print("You become hesistant as you do NOT have a passport. The guard sees right through you and becomes aggressive.")
            time.sleep(1)
            print("He punches you several times until he made sure you DIE... \n YOU'RE DEAD, GAME OVER!!")
            intro()
        else:
            print("""\nYou knew the whole thing is a set up, so you FLING your boarding pass to the guards neck... 
            \nHis neck sliced open which led his colleagues to chase you, but you fought through with your bare hands.
            \nNow, the whole screening area is covered with corpses... The corpses YOU killed with your bare hands... 
            \nSince you silently chopped everyone there, you can now take their gun, uniform and ID. 
            \nDo you want them? Y/N""")
            choice = input(">>>")
            if choice in yes:
                gun = 1
                uniform = 1
                ID = 1
                duty_free()
            else:
              duty_free()
                
    else:
        print("\n Use only A, B, C, or D\n") 
        security()
  
def duty_free():
  print("\nDUTY FREE\n")
  print("""If you like shopping then you'll really love this part of X Aiport. 
  This small airport is known for their cheap yet quality duty free products.
  \nYou were freely browsing about after your victorious battle unitl a salesperson appeared out of nowhere.
  \nHe asks you to sample thier new alcohol but you feel an ominous aura around him.""")
    
  time.sleep(1)
    
  print("\nWhat will you do?")
    
  time.sleep(1)
    
  print("""
  A. You trust the person will not harm you and you try the alcohol
  B. You ignore the guy and walk towards your gate.""")
    
  choice = input(">>>")
  if choice in answer_A:
    print("""Yikes, looks like you trust people too much because you just DIED. 
    \nYOU'RE DEAD, GAME OVER!!""")
    intro()
  elif choice in answer_B:
    alcohol = 1
    print("""The salesperson becomes aggressive like the security guard, but this time you know exactly what to do...
    You shoot the him with the gun you just acquired and boy he's dead.""")
      
    time.sleep(1)
      
    print("You take the rest of the alcohol because why not!!")
  else: 
    print("\nUse only A or B\n")
    duty_free()

intro()

#def gate():
 # print("""Unfortunately, an angry mob is heading your way after you finish your glorious kill...
  #\n What will you do?""")
      
  #time.sleep(1)
      
  #print("""
  #A. Run to your gate.
  #B. Might as well kill the angry mob... Why not??""")
  
  #choice = input(">>>")
  #if choice in answer_A:"""
    

 
