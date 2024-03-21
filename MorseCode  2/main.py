MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                   '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                   '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                   '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                   '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
                   '-....-': '-', '-.--.': '(', '-.--.-': ')'}
# def search_equal(codedList):
#     MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
#                        'C': '-.-.', 'D': '-..', 'E': '.',
#                        'F': '..-.', 'G': '--.', 'H': '....',
#                        'I': '..', 'J': '.---', 'K': '-.-',
#                        'L': '.-..', 'M': '--', 'N': '-.',
#                        'O': '---', 'P': '.--.', 'Q': '--.-',
#                        'R': '.-.', 'S': '...', 'T': '-',
#                        'U': '..-', 'V': '...-', 'W': '.--',
#                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                        '1': '.----', '2': '..---', '3': '...--',
#                        '4': '....-', '5': '.....', '6': '-....',
#                        '7': '--...', '8': '---..', '9': '----.',
#                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
#                        '?': '..--..', '/': '-..-.', '-': '-....-',
#                        '(': '-.--.', ')': '-.--.-'}
#     print(codedList)
#     s = ''
#     for word in codedList:
#         for i in range(0, len(word)):
#             for key, value in MORSE_CODE_DICT.items():
#                 if value == word[i]:
#                     s += key
#         s += " "
#     if s[-1] == ' ':
#         return s[0:-1:]
#     return s

def decode_bits(bits):
    temp = ""
    out = ""
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    for c in range(0, len(bits)):
        temp += str(bits[c])
        if c != len(bits) - 1:
            if bits[c] != bits[c + 1]:
                if "1" in temp and temp.count("1") < 3:
                    out += '.'
                    temp = ""
                    pass
                elif "1" in temp and temp.count("1") > 3:
                    out += '-'
                    temp = ""
                    pass
                elif "0" in temp and temp.count("0") < 3:
                    temp = ""
                    pass
                elif "0" in temp and temp.count("0") < 7:
                    out += ' '
                    temp = ""
                    pass
                elif "0" in temp and temp.count("0") >= 7:
                    out += '   '
                    temp = ""
                    pass
        else:
            if "1" in temp and temp.count("1") < 3:
                out += '.'
                temp = ""
                pass
            elif "1" in temp and temp.count("1") > 3:
                out += '-'
                temp = ""
                pass
            elif "0" in temp and temp.count("0") < 3:
                temp = ""
                pass
            elif "0" in temp and temp.count("0") < 7:
                out += ' '
                temp = ""
                pass
            elif "0" in temp and temp.count("0") >= 7:
                out += '   '
                temp = ""
                pass
    return [x.split(' ') for x in out.split('   ')]


def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    seprList = decode_bits(morseCode)
    morseCode = ""
    if len(seprList) > 1:
        for i in range(len(seprList)):
            for j in range(0, len(seprList[i])):
                morseCode += MORSE_CODE[seprList[i][j]]
            morseCode += " "
        return morseCode[0:-1:]
    else:
        for i in range(0, len(seprList[0])):
            morseCode += MORSE_CODE[seprList[0][i]]
        return morseCode
