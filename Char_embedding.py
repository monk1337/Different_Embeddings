import unicodedata
import string

all_letters = string.ascii_letters + " .,;'-"


def unicodeToAscii(s):
    return ''.join(
       c for c in unicodedata.normalize('NFD', s)
       if unicodedata.category(c) != 'Mn'
       and c in all_letters
   )
   
sentences = ["Running the example prints the first item in the dataset",
             "Now according to the image I have to do max_pooling",
             "Structures like lists and NumPy arrays can be sliced"]


vocab_genration = []

for sentence in sentences:
    for letter in unicodeToAscii(sentence.lower()):
        vocab_genration.append(letter)

final_vocab = list(set(vocab_genration))

int_to_char = {m:n for m,n in enumerate(final_vocab,1)}

int_to_char.update({1:'<UNK>',0:'<PAD>'})


char_to_int = { n:m for m,n in int_to_char.items()}



# encoded_part

encoded_sentences=[]

for sent in sentences:
    local_sentence =[]
    for lett in sent.lower():
        if lett in char_to_int:
            local_sentence.append(char_to_int[lett])
        else:
            local_sentence.append(char_to_int['<UNK>'])
    encoded_sentences.append(local_sentence)
            
print(encoded_sentences)


#[[8, 4, 12, 12, 11, 12, 23, 21, 13, 20, 1, 21, 1, 24, 9, 22, 10, 15, 1, 21, 10, 8, 11, 12, 13, 16, 21, 13, 20, 1, 21, 19, 11, 8, 16, 13, 21, 11, 13, 1, 22, 21, 11, 12, 21, 13, 20, 1, 21, 17, 9, 13, 9, 16, 1, 13], 
#[12, 6, 14, 21, 9, 2, 2, 6, 8, 17, 11, 12, 23, 21, 13, 6, 21, 13, 20, 1, 21, 11, 22, 9, 23, 1, 21, 11, 21, 20, 9, 3, 1, 21, 13, 6, 21, 17, 6, 21, 22, 9, 24, 1, 10, 6, 6, 15, 11, 12, 23], 
#[16, 13, 8, 4, 2, 13, 4, 8, 1, 16, 21, 15, 11, 18, 1, 21, 15, 11, 16, 13, 16, 21, 9, 12, 17, 21, 12, 4, 22, 10, 5, 21, 9, 8, 8, 9, 5, 16, 21, 2, 9, 12, 21, 7, 1, 21, 16, 15, 11, 2, 1, 17]]
