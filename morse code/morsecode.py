MORSE_CODE = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'}

def main():
    translation(user_input())

def user_input():

    print("This program translates words to morse code\n")
    words = input("Enter a word or phrase to be encoded: ")
    words = words.upper()
    if words == 'EXIT':
        return False
    return words


def translation(words):

    i = 0

    if words == "EXIT":
        exit(main())


    if words != "":
        for letter in words:
            if letter not in MORSE_CODE.keys():
                print('please enter only normal characters')
                words = ''
        for i in range (len(words)):
            print(MORSE_CODE[words[i]])
            i += 1




while True:
    main()