import sys

# 'O' is raised, '.' is unraised (flat)
braille_dictionary = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

# reverse the braille dictionary to map letters easily
english_to_braille = {v: k for k, v in braille_dictionary.items()}

# check if input is braille (only 'O' and '.' characters)
def isBraille(input_string):
    return all(char in {'O', '.'} for char in input_string)

# translate english to braille with all cases
def translate_to_braille(text):

    result = [] # store braille characters

    for char in text:

        if char.isupper():
            result.append(english_to_braille['capital'])  # add capital marker
            result.append(english_to_braille[char.lower()]) # proceding with corresponding letter

        elif char.isdigit():
            result.append(english_to_braille['number'])  # add number marker
            result.append(english_to_braille[char]) # proceding with corresponding number

        elif char == ' ':
            result.append(english_to_braille[' ']) # check for space 

        else:
            result.append(english_to_braille[char])

    return ''.join(result) # combine list into single string for output

# translate braille to English
def translate_to_english(braille):

    result = [] # store english characters
    i = 0

    # flags
    isCapital = False
    isNumber = False
    
    while i < len(braille):

        char = braille[i: i + 6]  # read each 6-dot braille character
        
        # check all cases again and set corresponding flags
        if char == '.....O':
            isCapital = True

        elif char == '.O.OOO':
            isNumber = True

        elif char == '......':
            result.append(' ')

        # translate
        else:

            symbol = braille_dictionary[char] # translate braille character to english

            if isCapital:
                result.append(symbol.upper())
                isCapital = False  # reset

            elif isNumber:
                result.append(symbol) 
                isNumber = False  # reset

            else:
                result.append(symbol)
        
        i += 6  # next
    
    return ''.join(result) # combine list into single string for output

def main():
    
    # ensure 1 argument from user
    if len(sys.argv) != 2:
        return
    
    input_string = sys.argv[1] # get user input
    
    # check if user input is braille or english
    if isBraille(input_string):
        print(translate_to_english(input_string))
        
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
