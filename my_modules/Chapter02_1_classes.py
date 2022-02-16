import string
class TextContainer():
    """A simple container, containing text"""
    def __init__(self, text):
        self.text = text       
    
    def count_words(self):
        return len(self.text.split())
    
    def count_chars(self):
        return len(self.text)

    def count_letters(self):
        ascii_count = sum(c in string.ascii_letters for c in self.text)
        return ascii_count

    def remove_punctuation(self):
        punctuations = string.punctuation
        output = self.text
        for character in punctuations:
            output = output.replace(character,"")
        return output


class InvalidArgumentException(Exception):
    pass


class Person():
    """A simple container, containing text"""
    def __init__(self, name):
        words = name.split()
        input_ok = True
        for word in words:
            if word[0].isupper() == False or word.isalpha() == False:
                input_ok = False
        if(input_ok == True):
            self.name = name
        else:
            raise InvalidArgumentException("Error while validating the provided name")



    