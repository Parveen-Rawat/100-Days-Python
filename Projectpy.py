#Brand Name Generator
'''print("Welcome to the Brand Name Generator\n")
city_name = input("What city did you grew up\n")
pet_name = input("what is your pet name\n")
print("Your Brand Name could be " + city_name + " " + pet_name)'''

# Tip calculator
'''print("Welcome to the tip calculator\n")
bill = input("How much was your total bill? $")

tip = input("how much tip you would like to give?  10, 20, 15 ")

split = input("How many people to split the bill ")

a = 1 + int(tip)/100
b = float(bill) * a
c = b/float(split)
print(f"Each person should pay: {c}")'''

# Treasure Game
memo = """**********************************************************************************************
                                        .,,,.
                                     ,cdMMMMMMMb.
                                  ,dMMMMMMMMMMMMMb
                             .ueiWMMMMMMTT??TTMMM
                           ,dMM>MMMP"";;;;;;;;;;;;;,.  
                         ,MMMMMP"`,ce$$$$beiu`;;;;;;;;,   ,c,
                       ;dMMMM" u$$$$$P",,J$$$$h`;;;;;;;  `?X$$>   
                       MMMMF d$$$$$$$Ld"..`?$$`$b`''''    d"??'
                       `MM',$$$$$$$$$$$ $$$$$$b?$$      ,d"  
                         ".$$$$$$$$$$$$$$$$P"?$h,er.   ,P'  
                          `?$$$$$$$$$$$$$F ,cd$iGbd$$,?$$bo.
                          /'"-S$$$$????$$$$CCCRR$$$$$$ $$$$$k
                          $P.de$$Ed?R$bbbdh $$$$$$$$$F,$$$$?$>
                          `"??I$$$$k         `"???"',d$$$$$$L
                          ..,d$$"z$$        <$$UUU$$$$$$$$$$R
                      .umMMM.$$$$$$$L       !$$$$$$$$$$$$$$$f  
                    .dMMMMM'i$$$P""$$.      4$$$$$$$$$$$$$$P   
                  .dMMMMMMM.$$$F:dM,?$.     d$?$$$$$$$$$$P'  
                 uMMMMPRMMM.$$$C:MMM,?bc,,cdF;$$$$$$$$P'  
                uMMMF;ee;?,,?$$$b:MMM,"????" ```   
              .:MMM'd$$$$<$$,?$$F:::::::::::.
            :::4MMM:$P,oi;$$d$$$$;$<$:??MMMMMMMMMTT":.
       ..:::::::::::d$$$$F;E$P;:::::::::::::::::      
      d$$i::::::::::?$$$$;$E$R>::::::::::: :::::: 
     d$$$$$eii::::::?$$$f;$&$R>d$$$$$$$$$$$$$$>?$$$$$;$$$B:::          "??<
   `?$$$$$$$$$$$$$$$$P?:::::::d$$ $F.d$$$$$$$$$$$$$$E
      `""???????::::::::::::;$$$," ",$$$$$$$$$$$$$$F
        ::::::::::::::::::::::<$$$$$$$$$$$$$$$$$$$$$$
        :::::::::::::::::::::::<$$$$$$$$$$$$$$$$$$$$$F
        ::::::::::::::::::::::::$$$$$$$$$$$$$$$$$$$$P
        ::::::::::::::::::::::::?$$$$$$$$$$$$$$$$$$"
        `::::::::::::::::::::::::?$$$$$$$$$$$$$$$"
         :::::::::::::::::::::::::?$$$$$$$$$$$P"
        .:::::::::::::::::::::::::;$$$$C?>""`.
       `::::::::::::::::::::::::::`$$$$$$$$7?R?+
         :::::::::::::::::::::::udh`$$$$$$$:$$$$c 
          ::::::::;;;;;;;cmumdMMMMM $$$$$$5U;?$$"
         dMMMMMMUMMMMMMMMMMMMMMMMMM  ?$$$$$$$$>` 
         MMMMMMMMMMMMMMMMMMMMMMMMM"    "?R$$PF    
        'MMMMMMMMMMMMMMMMMMMMMMMFdL
         ?MMMMMMMMMMMMMMMMMMMMMMMMML
          ?MMMMMMMMMMMMMMMMMMMMMMMMMc
           `MMMMMMMMMML??MF?;MMMMMMMMk
            MMMMMMMMMMMMb;?MMMMMMMMMMML
            ?MMMMMMMMMMMMMM;MMMMMMMMMMM
            `MMMMMMMMMMMMMMM;MMMMMMMMMM:m.
             `MMMMMMMMMMMMMMM;MMMMMMMMNNMM
              `MMMMMMMMMMMMMMM;?MMMMMMMMMN
               L?MMMMMMMMMMMMMMb;MMMMMMMMNM.
              :?b>MMMMMMMMMMMMMP;MMMMMMMMMMM.
             xMb..:::.."":::::. 
           :6TTMMMMMMMMMMMRRTIdMM"::::::::::`:::::: 
            ?WWWbbbeeedddWWMRP"":::::::::::::.:::::  
             "?????????":':::::::::::::::::::.:::
             :::::''::::::::::::::::::::::::::.::::
              :::'':::::::::::::::::::::::::::.::'`
              ;;;;;;;;;'````
****************************************************************************************************"""
print(memo)
print("\n Welcome to the treasure Island.\n")
print("Your mission is to find the hidden treasure\n")
choice = input("""You are at the cross road where you want to go \n 
                    type "[left]" or "[right]"\n
               """)

if choice == "left" or choice == "Left":
    second_choice = input("""You have come to a lake . There is an island on the other side of the lake.\n \t type "wait" to wait for the boat or type "swim" to swim across the lake.\n""")
    if second_choice == "wait":
        print("You arrived at the island unharmed. There is a house with three doors.\n ")
        third_choice = input("one red, one yellow, one orange .Which colour would you choose.\n")
        if third_choice == "red":
            print("You won\n")
        elif third_choice == "yellow":
            print("you lost: game over")
        else:
            print("you fell into the dungeon and eaten by the monstors: game over")
    else: 
        print("You chose to swim and got eaten by a sea dragon : GAME OVER")
            
else: 
    print("You chose right; fell into the hole and die: GAME OVER")