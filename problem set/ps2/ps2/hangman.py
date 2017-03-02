# Problem Set 2, hangman.py
# Name: Xudong Sun
# Collaborators: NA
# Time spent: 4:00
# Late days used: 0

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # the set of letters in secret word    
    set_w = set(secret_word[i] for i in range(len(secret_word)))
    # the set of guessed letters
    set_g = set(letters_guessed)
    # according to the rules of "hangman", if the two sets above is identical
    # the word is guessed
    if set_w <= set_g: ## wrong for the first time !!!
        return(True)
    else:
        return(False)
    

   



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # make a string for guessed word outcome    
    guessed = ''   
    # pick out the letter one by one from secret_word
    # if the letter is guessed, put it in the same position in 'guessed' string
    # if not, use '_ ' to take up the position
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed += secret_word[i]
        else:
            guessed += '_ '
    return(guessed)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # make an empty string to contain available letters    
    available = ''    
    letters = string.ascii_lowercase
    # check every letter in the alphabet
    # if the letter is not guessed, put it into the string available
    for i in range(len(letters)):
        if (letters[i] not in letters_guessed): ## do not use loop with == True
            available += letters[i]
            
    return(available)
    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # two basic values to check the status    
    warnings = 3
    guesses = 6
    
    # a list as the container of guessed letters   
    letters_guessed = []    
    
    # introductions
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % (len(secret_word)))
    print('You have %d warnings left.' % (warnings))   
    print('------------')
    
    # using a while loop to guess once and once again
    # until the letters in secret word are all guessed
    while is_word_guessed(secret_word, letters_guessed) == False:
        
        # exclude the fail situation
        if guesses == 0:
            print('Sorry, you ran out of guessed, The word was else.')
            # the game is over            
            win = False
            break
        # a normal guess
        else:
            print('You have %d guesses left.' % (guesses))
            aval = get_available_letters(letters_guessed)            
            print('Available letters: %s' % (aval), end='')
            one_guess = input('Please guess a letter: ').lower()
            # check if the input is a letter
            if one_guess.isalpha() == False:
                warnings -= 1
                # before the player uses up 3 warnings                
                if warnings >= 0:
                    print('Oops! That is not a valid letter. You have %d warnings left:' % (warnings))
                    print(get_guessed_word(secret_word, letters_guessed))
                # after using up 3 warnings, guesses -1
                else:
                    print('Oops! That is not a valid letter. You have no warnings left:')
                    print('so you lose one guess:' + get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                
            # check if the input is a guessed letter     
            elif one_guess in letters_guessed:
                warnings -= 1
                # before the player uses up 3 warnings                 
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You have %d warnings left:" % (warnings))
                    print(get_guessed_word(secret_word, letters_guessed))
                # after using up 3 warnings, guesses -1
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left:")
                    print('so you lose one guess:' + get_guessed_word(secret_word, letters_guessed))             
                    guesses -= 1
                    
            # process a 'proper' input
            else:
                # put the letter into the list of guessed letters                
                letters_guessed.append(one_guess)
                # check if the letter is in the word
                if one_guess in secret_word:   
                    print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            
                else:
                    print('Oops! That letter is not in my word')
                    print('Please guess a letter: ' + get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
        
        print('------------')
        
    # win message
    if win == True:
        print('Congratulations, you won!')
        # calculating the score
        score = guesses * len(letters_guessed)   
        print('Your total score for this game is: ' + str(score))
    
                    
        
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # clear all the spaces in my_word    
    my_word_s = my_word.replace(' ','')
    # firstly check if the lenth of the word is the same
    if len(my_word_s) != len(other_word):
        return(False)
    # if my_word and other_word have same lenth,
    # then check the letters
    else:
        n = 0        
        for i in range(len(my_word_s)):
            if my_word_s[i] == '_':
                # hidden letter cannot be one of the letters
                # that have already been revealed                
                if other_word[i] in my_word_s:
                    return(False)
                    break
                else:
                    n += 1
            # check the guessed letters    
            elif my_word_s[i] != other_word[i]:
                return(False)
                break
            
            else:
                n += 1
    # if all guessed numbers are right, return True
        if n == len(other_word):
            return(True)
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # check every letter of the word
    # matched word count: n    
    n = 0
    # an empty string to contain possible matches
    matched_words = ''
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            n += 1
            matched_words += (word + ' ')
            
        
    if n == 0:
        return('No matches found')
    else:
        return(matched_words)
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
        # two basic values to check the status    
    warnings = 3
    guesses = 6
    
    # a list as the container of guessed letters   
    letters_guessed = []    
    
    
    # introductions
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % (len(secret_word)))
    print('You have %d warnings left.' % (warnings))   
    print('------------')
    
    # using a while loop to guess once and once again
    # until the letters in secret word are all guessed
    while is_word_guessed(secret_word, letters_guessed) == False:
        
        # exclude the fail situation
        if guesses == 0:
            print('Sorry, you ran out of guesses, The word was else.')
            # the game is over            
            win = False
            break
        # a normal guess
        else:
            print('You have %d guesses left.' % (guesses))
            aval = get_available_letters(letters_guessed)            
            print('Available letters: %s' % (aval), end='')
            one_guess = input('Please guess a letter: ').lower()
            # check if the player needs a hint            
            if one_guess == '*':
                print("Possible matches are:")
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            
            # check if the input is a letter
            elif one_guess.isalpha() == False:
                warnings -= 1
                # before the player uses up 3 warnings                
                if warnings >= 0:
                    print('Oops! That is not a valid letter. You have %d warnings left:' % (warnings))
                    print(get_guessed_word(secret_word, letters_guessed))
                # after using up 3 warnings, guesses -1
                else:
                    print('Oops! That is not a valid letter. You have no warnings left:')
                    print('so you lose one guess:' + get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                
            # check if the input is a guessed letter     
            elif one_guess in letters_guessed:
                warnings -= 1
                # before the player uses up 3 warnings                 
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You have %d warnings left:" % (warnings))
                    print(get_guessed_word(secret_word, letters_guessed))
                # after using up 3 warnings, guesses -1
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left:")
                    print('so you lose one guess:' + get_guessed_word(secret_word, letters_guessed))             
                    guesses -= 1
                    
            # process a 'proper' input
            else:
                # put the letter into the list of guessed letters                
                letters_guessed.append(one_guess)
                # check if the letter is in the word
                if one_guess in secret_word:   
                    print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            
                else:
                    print('Oops! That letter is not in my word')
                    print('Please guess a letter: ' + get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
        
        print('------------')
        
    # win message
    if is_word_guessed(secret_word, letters_guessed) == True:
        print('Congratulations, you won!')
        # calculating the score
        score = guesses * len(letters_guessed)   
        print('Your total score for this game is: ' + str(score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
