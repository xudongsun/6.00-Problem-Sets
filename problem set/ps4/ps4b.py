# Problem Set 4B
# Name: Xudong Sun
# Collaborators: NA
# Time Spent: 3:00

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # mapping dictionary        
        d = {}
        # all letters
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        # for every letter assign the shifted letter
        for i in range(len(upper)):
            if i + shift < len(upper):
                n = i + shift
            else:
                n = i + shift - 26 # wrap
            # put the mapping pair into the dictionary     
            d[upper[i]] = upper[n]
            d[lower[i]] = lower[n]
            
        return d
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # get text with get method      
        text = self.get_message_text() #?
        text_shift = ''
        # get dictionary with build_shift_dict method
        d = self.build_shift_dict(shift)
        # check every character in the text
        for char in text:
            # if it is a letter, shift it according to the mapping dictionary
            if char.isalpha():
                text_shift += d[char]
            # if it is not a letter, leave it be
            else:
                text_shift += char
            
        return text_shift
    

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # inherit all basic attributes of Message class
        Message.__init__(self, text)     #?   
        self.shift = shift
        # inherit methods from super class
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)
    
    # __str__method, only for checking output    
    def __str__(self):
        return "text: '" + str(self.message_text) +"', shift= " + str(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # basic values: best shift value, maximum number of valid words
        best_shift = 0  
        max_real_words = 0
        # dexcrypted message
        dec_message = ''
        
        # get the word list ?? why super().valid words dosen't work?
        wordlist = self.valid_words
        # try every possible shift in range(26)
        for i in range(26):
            message = self.apply_shift(i)
            # split the message into a list of words
            words_l = message.split()
            # count real words
            n_real_words = 0
            # check every word in word list
            for word in words_l:
                if is_word(wordlist, word):
                    n_real_words += 1    
        
            # the i with bigger number of real words substitute the former ones
            # (one of) the best shift will be left when the for loop is finished
            if n_real_words > max_real_words:
                best_shift = i
                max_real_words = n_real_words
                dec_message = message
                
        return (best_shift, dec_message)
        

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

     # test case 1: plaintext
#    plaintext = PlaintextMessage('plain text', 5)
#    print('Expected Output: uqfns yjcy')
#    print('Actual Output:', plaintext.get_message_text_encrypted())

     # test case 2: plaintext
#    plaintext1 = PlaintextMessage('Details about "object", use "object??" for extra details', 14)
#    print('Expected Output: Rshowzg opcih "cpxsqh", igs "cpxsqh??" tcf slhfo rshowzg')
#    print('Actual Output:', plaintext1.get_message_text_encrypted())
   
     # test case 3: ciphertext
#    ciphertext = CiphertextMessage('uqfns yjcy')
#    print('Expected Output:', (21, 'plain text'))
#    print('Actual Output:', ciphertext.decrypt_message())
   
     # test case 4: ciphertext
#    ciphertext = CiphertextMessage('Uh yhbuhwyx Chnyluwncpy Jsnbih')
#    print('Expected Output:', (6, 'An enhanced Interactive Python'))
#    print('Actual Output:', ciphertext.decrypt_message())
       
     # test case 5: change_shift test
#    plaintext.change_shift(6)
#    print("Expected Output: text: 'plain text', shift = 6")
#    print('Actual Output:', plaintext)
#    print('Expected Output: vrgot zkdz')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    
    
#    ciphertext1 = CiphertextMessage('Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr oqzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu.')
#    print('Unencrypted story:', ciphertext1.decrypt_message())
    
    """
    Unencrypted story: (12, 'Jack Florey is a mythical character created on the
    spur of a moment to help cover an insufficiently planned hack. He has been 
    registered for classes at MIT twice before, but has reportedly never passed 
    aclass. It has been the tradition of the residents of East Campus to become 
    Jack Florey for a few nights each year to educate incoming students in the 
    ways, means, and ethics of hacking.')
    
    """
    
    
    
    
    
    
    
    
    
    
    
    
    