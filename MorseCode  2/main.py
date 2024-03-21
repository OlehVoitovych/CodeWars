# def decode_bits(bits):
#     # ToDo: Accept 0's and 1's, return dots, dashes and spaces
#     # 10101010001000111010111011100000001011101110111000101011100011101010001
#     return bits.replace("111111", '-').replace("11", '.').replace("00000000000000", '   ').replace("000000", ' ').replace("00", '')
#
#
# def decode_morse(morseCode):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
#     return search_equal(morseCode)
#
#
# def search_equal(coded):
#     temp = [x.split(' ') for x in decode_bits(coded).split('   ')]
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
#     print(temp)
#     s = ''
#     for word in temp:
#         for i in range(0, len(word)):
#             for key, value in MORSE_CODE_DICT.items():
#                 if value == word[i]:
#                     s += key
#         s += " "
#     if s[-1] is ' ':
#         return s[0:-1:]
#     return s
#
#
#
#
#
# print(decode_morse('10101010001000111010111011100000001011101110111000101011100011101010001'))

def decode_bits(bits):
    temp = ""
    bool = False
    outList = []
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    for c in range(0, len(bits)):

        if bits[c-1] == bits[c]:
            temp += bits[c]
        else:
            outList.append(temp)
            temp = ""
            temp += bits[c]

    s = ""
    for i in outList:
        s += i
    print(s)
    print(bits == s)
    print(bits.replace(s, ""))

    return outList
def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    seprList = decode_bits(morseCode)
    print(seprList)
    morseCode = ''
    # if len(seprList) > 1:
    #
    #     for word in seprList:
    #         for i in range(0, len(word)):
    #             morseCode += MORSE_CODE[word[i]]
    # else:
    #         for i in range(0, len(seprList[0])):
    #             morseCode += MORSE_CODE[seprList[0][i]]
    #
    # return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    return 0


def MORSE_CODE(char):
    return 0


decode_morse("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")