# import nltk
# nltk.download('words')

from nltk.corpus import words
word_list_orginal = words.words()

word_list = set([word.lower() for word in word_list_orginal])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(words, key):
    '''
    Encrypt your string with 'caesar_cipher' way:
        inp ---> your inputed string
        inp2 ---> the key you want to encrypt with
        out >>> the string after encrypt
    '''
    encrypted_words = ''

    for char in words.lower():
        if char in alphabet:
            encrypted_letter = alphabet[(alphabet.index(char.lower()) + key) % len(alphabet)]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += char
    return encrypted_words    


def decrypt(words, key):
    '''
    decrypt your string with caesar_cipher method:
        inp ---> your inputed string
        inp2 ---> the key you'v encrypted with..
        out >>> the string after decrypt
    '''
    return encrypt(words, -key)


def decrypt_randomly_key(words):
    '''
    Dncrypt your string with 'caesar_cipher' way:
        inp ---> your inputed encrypted string
        out >>> the string after decrypt
    '''
    def english_words(list_of_words):
        '''
        small method to count the number of english_words in the sentence..
            inp ---> tested string
            out >>> bolean if the number of english is greater one..
        '''
        number_correct = 0
        for word in list_of_words:
            if word in word_list:
                number_correct += 1
        if number_correct/len(list_of_words) >= 0.5:
            return True
        return False

    for key in range(len(alphabet)):    
        a = encrypt(words, (-1*(key)))
        b = english_words(a.split(' '))
        if b:
            return a

