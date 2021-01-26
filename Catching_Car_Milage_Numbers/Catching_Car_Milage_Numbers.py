def is_palindrome(number):
    return str(number) == str(number)[ : : -1]

def mostly_zeros(number):
    if len(str(number)) == 1:
        return False
    i = len(str(number)) - 1
    while i > 0:
        if str(number)[i] != "0":
            return False
        i -= 1      
    return True

def same_digits(number):
    return all(str(number)[i] == str(number)[0] for i in range(0, len(str(number))))

def inc_seq(number):
    if str(number)[-1] == "0" and str(number)[-2] == "9":
        num_string = str(number)[ : -1]
    else:
        num_string = str(number)
    for i in range(0, len(num_string) - 1):
        if int(num_string[i + 1]) != int(num_string[i]) + 1:
            return False
    return True

def dec_seq(number):
    if str(number)[-1] == "0" and str(number)[-2] == "1":
        num_string = str(number)[ : -1]
    else:
        num_string = str(number)
    for i in range(0, len(num_string) - 1):
        if int(num_string[i + 1]) != int(num_string[i]) - 1:
            return False
    return True

def is_awesome(number, awesome_phrases):
    return not all(number != i for i in awesome_phrases)

def is_interesting_temp(number, awesome_phrases):
    if number <= 99:
        return False
    if any([is_palindrome(number), mostly_zeros(number), same_digits(number), inc_seq(number), dec_seq(number), is_awesome(number, awesome_phrases)]):
        return True
    else:
        return False

def is_interesting(number, awesome_phrases):
    if is_interesting_temp(number, awesome_phrases):
        return 2
    elif is_interesting_temp(number + 1, awesome_phrases) or is_interesting_temp(number + 2, awesome_phrases):
        return 1
    else:
        return 0
