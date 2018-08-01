# Creator Josue Lopez
# Mon Jul 16 2018
# Python 3.6

'''
This source code is a program that helps transpose a list of the musical chords
from one musical key to another key.

Currently, the this program only supports # (sharp notes).

When the script is run, the 'main' function handles the entire program.
'''
# Imports

# Global Constants
major_key_list = {'A':1,'A#':2,'B':3,'C':4,'C#':5,'D':6,'D#':7,'E':8,'F':9,'F#':10,'G':11,'G#':12}
minor_key_list = {'Am':1,'A#m':2,'Bm':3,'Cm':4,'C#m':5,'Dm':6,'D#m':7,'Em':8,'Fm':9,'F#m':10,'Gm':11,'G#m':12}
list_of_major_chords = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
list_of_minor_chords = ['Am','A#m','Bm','Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#m']
line = "---------------------------------------------"
input_indent = "\n--->"

# Global Variables
original_minor_chord_value = ''
original_major_chord_value = ''

def main():
    keys_to_transpose = []

    print (line)
    
    starting_key = input("From what key are you trying to transpose?" + input_indent)
    ending_key = input("To what key are you trying to transpose?" +input_indent)
    
    global transpose_steps
    transpose_steps = _calc_transpose_steps(starting_key,ending_key) ### created the global variable 
    
    print ("Therefore we will be transposing with", transpose_steps, "steps")
    #----------------------------------------------------------------------------
    print (line)
    given_value = int(input("How manys chords are in your list?" + input_indent))
    
    original_chords = input(f"Enter the {given_value} chords as capital letters in one line.\n")
    
    if len(original_chords.split()) == given_value :
        keys_to_transpose = original_chords.split()
    else:
        raise ValueError(f'The number of chords you entered does not match the given value {given_value}.')
    
    #----------------------------------------------------------------------------
    print(line)
    print('These are your original keys:')
    print(original_chords)
    #----------------------------------------------------------------------------
    print(line)
    print('These are your Transposed Keys:')
    for key in keys_to_transpose:
        if key in major_key_list:
            transposing_major_func(key)
        if key in minor_key_list:
            transposing_minor_func(key)
            
    print('Done')


def _calc_transpose_steps(starting_key,ending_key):
    if starting_key in major_key_list:
        starting_digit = major_key_list[starting_key]
        ending_digit = major_key_list[ending_key]
       
    if starting_key in minor_key_list:
        starting_digit = minor_key_list[starting_key]
        ending_digit = minor_key_list[ending_key]
      
    transpose_steps = abs(starting_digit - ending_digit)
    return transpose_steps


def original_MAJOR_func(keys):
    global original_major_chord_value
    original_major_chord_value = major_key_list[keys]


def original_MINOR_func(keys):
    global original_minor_chord_value
    original_minor_chord_value = minor_key_list[keys]


def transposing_major_func(keys):
    new_transposed_chords = (major_key_list[keys] + transpose_steps)
    
    if new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
    print (list_of_major_chords[new_transposed_chords-1], end=' ')

def transposing_minor_func(keys):
    new_transposed_chords = (minor_key_list[keys] + transpose_steps)
    
    if new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
    print (list_of_minor_chords[new_transposed_chords-1], end=' ')

if __name__ == "__main__":
    main()
