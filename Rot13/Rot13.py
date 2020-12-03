def shift(strng, num=13):
    """
    strng: a string
    num: an int (default 13) specifying the length of the ceaser shift (how many places to move along the alphabet)
    returns a new string where each letter has been shifted by num places (ignores numbers/spaces/punctuation etc.) 
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for char in strng:
        if char in letters:
            index = letters.index(char)
            new_string += letters[(index + num) % 26]
        elif char in letters.upper():
            index = letters.upper().index(char)
            new_string += letters.upper()[(index + num) % 26]
        else:
            new_string += char
    return new_string

def rot13(strng):
    return shift(strng)

