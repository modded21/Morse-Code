# This was part of an exercise we did in class, this program is only capable of running on Windows, so I apologize to my fellow macOS users.
import winsound
import time

morse_dict = {
    ' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', 'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

def main():
    # Get the string as input from the user.
    morse_string = input('Enter the string to be ' \
                         'converted to Morse code: ')
    # Step through the string, determine each
    # character's Morse code and play the corresponding sound.
    for ch in morse_string.upper():
        if ch in morse_dict:
            txt2morse(morse_dict[ch])
        else:
            print(f"Character '{ch}' is not supported in Morse code.")


def play_dot():
    winsound.Beep(1000, 100)  # Frequency of 1000 Hz for dot, duration of 100 ms


def play_dash():
    winsound.Beep(1000, 300)  # Frequency of 1000 Hz for dash, duration of 300 ms


def play_char(ch):
    for d in ch:
        if d == '.':
            play_dot()
        elif d == '-':
            play_dash()
        else:
            time.sleep(0.7)  # Space between words
    return ch


def txt2morse(morse_code):
    for ch in morse_code:
        print(play_char(ch))
    time.sleep(0.3)  # Space between characters


# Call the main function.
main()
