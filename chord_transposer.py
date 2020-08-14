# Creator Josue Lopez
# Mon Jul 16 2018
# Python 3.6

"""
This source code is a program that helps transpose a list of the musical chords
from one musical key to another key.

Currently, the this program only supports # (sharp notes).

When the script is run, the 'main' function handles the entire program.
"""
# Imports

# Global Constants
MAJOR_KEY_LIST = {
    "A": 1,
    "A#": 2,
    "B": 3,
    "C": 4,
    "C#": 5,
    "D": 6,
    "D#": 7,
    "E": 8,
    "F": 9,
    "F#": 10,
    "G": 11,
    "G#": 12,
}

MINOR_KEY_LIST = {
    "Am": 1,
    "A#m": 2,
    "Bm": 3,
    "Cm": 4,
    "C#m": 5,
    "Dm": 6,
    "D#m": 7,
    "Em": 8,
    "Fm": 9,
    "F#m": 10,
    "Gm": 11,
    "G#m": 12,
}

LIST_OF_MAJOR_CHORDS = [
    "A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#"
]

LIST_OF_MINOR_CHORDS = [
    "Am",
    "A#m",
    "Bm",
    "Cm",
    "C#m",
    "Dm",
    "D#m",
    "Em",
    "Fm",
    "F#m",
    "Gm",
    "G#m",
]

LINE = "---------------------------------------------"
INPUT_INDENT = "\n--->"

# Global Variables
ORIGINAL_MINOR_CHORD_VALUE = ""
ORIGINAL_MAJOR_CHORD_VALUE = ""


def main():
    """ Main function that executes the commandline program """
    keys_to_transpose = []

    print(LINE)

    starting_key = input("From what key are you trying to transpose?" + INPUT_INDENT)
    ending_key = input("To what key are you trying to transpose?" + INPUT_INDENT)

    global transpose_steps
    transpose_steps = _calc_transpose_steps(
        starting_key, ending_key
    )  ### created the global variable

    print("Therefore we will be transposing with", transpose_steps, "steps")
    # -------------------------------------------------------------------------
    print(LINE)
    given_value = int(input("How manys chords are in your list?" + INPUT_INDENT))

    original_chords = input(
        f"Enter the {given_value} chords as capital letters in one LINE.\n"
    )

    if len(original_chords.split()) == given_value:
        keys_to_transpose = original_chords.split()
    else:
        raise ValueError(
            f"The number of chords you entered does not match the given value {given_value}."
        )

    # -------------------------------------------------------------------------
    print(LINE)
    print("These are your original keys:")
    print(original_chords)
    # -------------------------------------------------------------------------
    print(LINE)
    print("These are your Transposed Keys:")
    for key in keys_to_transpose:
        if key in MAJOR_KEY_LIST:
            transposing_major_func(key)
        if key in MINOR_KEY_LIST:
            transposing_minor_func(key)

    print("Done")


def _calc_transpose_steps(starting_key, ending_key):
    """ Util function:  Given a two char's, this function will calculate
        the number of transposing steps in between the keys
    """
    if starting_key in MAJOR_KEY_LIST:
        starting_digit = MAJOR_KEY_LIST[starting_key]
        ending_digit = MAJOR_KEY_LIST[ending_key]

    if starting_key in MINOR_KEY_LIST:
        starting_digit = MINOR_KEY_LIST[starting_key]
        ending_digit = MINOR_KEY_LIST[ending_key]

    transpose_steps = abs(starting_digit - ending_digit)
    return transpose_steps


def original_major_func(keys):
    """ Setter function to update the global variable """
    global ORIGINAL_MAJOR_CHORD_VALUE
    ORIGINAL_MAJOR_CHORD_VALUE = MAJOR_KEY_LIST[keys]


def original_minor_func(keys):
    """ Setter function to update the global variable """
    global ORIGINAL_MINOR_CHORD_VALUE
    ORIGINAL_MINOR_CHORD_VALUE = MINOR_KEY_LIST[keys]


def transposing_major_func(keys):
    """ Given a list of char's, prints a new list with transposed notes """
    new_transposed_chords = MAJOR_KEY_LIST[keys] + transpose_steps

    if new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
    print(LIST_OF_MAJOR_CHORDS[new_transposed_chords - 1], end=" ")


def transposing_minor_func(keys):
    """ Given a list of char's, prints a new list with transposed notes """
    new_transposed_chords = MINOR_KEY_LIST[keys] + transpose_steps

    if new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
    print(LIST_OF_MINOR_CHORDS[new_transposed_chords - 1], end=" ")


if __name__ == "__main__":
    main()
