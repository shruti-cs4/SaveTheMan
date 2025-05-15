import random 
print('''Welcome To Save The Man \n 
    A game where your IQ is your superpower! Can you outwit the challenges and rescue our little MAN from ASCII ZOMBIEE!!''')

print('''                                      
                                    ,,,,,
                                   '['_']'
                                  __/\ /\__
                                 / /| : |\ \ 
                                / / |_:_| \ \ 
                               (_|  | | |  |_)
                                    |_|_|
                                   (_] [_)
''')
print("*Don't leave spaces while answering*")
score = 0
Ques = [
    ("What word is spelled incorrectly in every single dictionary?", "incorrectly"),
    ("Turn me on my side, and I am everything. Cut me in half, and I am nothing. What number am I?", "8"),
    ("Arjun said, 'She is the daughter of my grandfather's only son.' How is Arjun related to the girl in the photograph?", "brother"),
    ("In a certain code language, STUDENT is written as TUTDNES. How will SOURCES be written in that code language?", "sources"),
    ("All the six members of family A, B, C, D, E, and F are traveling together. B is the son of C but C is not the mother of B. A and C are married. E is the brother of C. D is the daughter of A. F is the brother of B. Who is the mother of B?", "a"),
    ("If 34 is related to 12, then 99 is related to?", "81"),
    ("A    man once said he went 35 days without sleep. Is it possible, yes or no?", "yes"),
    ("What word becomes longer after you add two letters to it?", "long"),
    ("What's something that has a lot of problems not many people are eager to solve?", "mathbook"),
    ("In a class seven students are standing in a row. Q is standing left to R but right to P. O is standing right to N and left to P. Similarly, S is standing right to R and left to T. Find out who is standing in the middle?", "q")
]
random.shuffle(Ques)

for Q, A in Ques:
    Ans = input(Q + "\n").lower()
    if Ans == A:
        score += 2
        print("Correct.\n")
    else:
        print("Wrong.\n")

if score < 12 :
    print('''
                               ______________  
                              /              \ 
                             /                \ 
                      /   \  \       \/       /  /   \  
                      ||||<|  \   vvvvvvvv   /  |>||||
                      vvvv \   |  |      |  |   / vvvv
                         \  \  |  |      |  |  /  /
                          \  \ \  \^^^^^^/  / /  /
                           \    ------------    /
                                  OH NOES!
                               ASCII ZOMBIEE!!
                                 YOU LOST!! :(
    ''')
else:
    print(''' 
          

                                     ,,,,,,
                                    '['__']'            YESSS!!!
                               _  __/ \ / \__  _       YOU WON!! YOU SAVED ME:)
                              ( \/ /|  :  |\ \/ )      THANKS & CONGRATULATIONS
                               \__/ |__:__| \__/ 
                                    |  /\ |  
                                    | | | |
                                    | | | |
                                   (__] [__)
    ''')
print("Your Score = ", score)







