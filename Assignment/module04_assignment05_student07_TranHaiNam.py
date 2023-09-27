MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-' }
letterMorseDictionary = {
    'DOT' : '.',
    'SPACE' : ' ',
    'DASH' : '-'
}
def decrypt(message):
        message.split(" ")
        new_message = ""
        for i in message.split(" "):
                new_message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(i)]
        return new_message                
message=".- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."

# ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH

      
def decrypt_double(message):
        new_message = decrypt(message)
        for char in letterMorseDictionary:
                new_message = new_message.replace(char, letterMorseDictionary[char])
        return new_message
abc = decrypt_double(message)
