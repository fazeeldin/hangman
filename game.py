import time
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play hangman!"
print ""
time.sleep(1)
print "Start guessing..."
time.sleep(0.5)

from IPython.display import clear_output

word = "python"
str_guesses = ''
turns = 7

while turns > 0:         
    failed = 0    
    
    for char in word:
        if char in str_guesses:    
            print char,    
        else:
            print "_",                
            failed += 1 
    if failed == 0:        
        print "You won"  
        break              
    guess = raw_input("guess a character:") 
    str_guesses += guess
    clear_output()
    if guess not in word:
        turns -= 1        
        print "You have", + turns, 'more guesses\n' 
        if turns == 6:
                print ' | '
                print '\n'
        elif turns == 5:
                print ' | '
                print ' O '
                print '\n'
        elif turns == 4:
                print ' | '
                print ' O '
                print ' | '
                print '\n'
        elif turns == 3:
                print ' | '
                print ' O '
                print '-| '
                print '\n'
        elif turns == 2:
                print ' | '
                print ' O '
                print '-|-'
                print '\n'
        elif turns == 1:
                print ' | '
                print ' O '
                print '-|-'
                print '/  '
                print '\n'
        elif turns == 0:
                print ' | '
                print ' O '
                print '-|-'
                print '/ \\'
                print '\n'
                print "You got hanged!" 
