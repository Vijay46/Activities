word = """A DC machine is an electromechanical energy alteration device. 
The working principle of a DC machine is when electric current flows through a coil within a magnetic field, 
and then the magnetic force generates a torque that rotates the dc motor. 
The DC machines are classified into two types such as DC generator as well as DC motor."""
print(word)

def s(word):


    word_replace=input('enter word to be replaced from paragraph:')
    word_new=input('enter a new word')
    word_new=word.replace(word_replace,word_new)
    print(f'{word_new}  {word}')
s(word)