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
input_indent = "\n\n--->"

def main():
    keys_to_transpose = []

    print (line)
    
    starting_key = input("From what key are you trying to transpose?" + input_indent)
    
    ending_key = input("To what key are you trying to transpose?" +input_indent)
    
    
    halfstep_calc(starting_key,ending_key)
    
    print ("Therefore we will be transposing with", transpose_steps, "steps")
    #----------------------------------------------------------------------------
    print (line)
    given_value = int(input("How manys chords are in your list?" + input_indent))
    
    counter = 0
    
    if counter == 0:
        original_chords = input("Enter the first chord as a capital letter.\n")
    
    
        keys_to_transpose.append(original_chords)
        counter += 1
    while counter < given_value:
        original_chords = input("Enter the next chord as a capital letter.\n")
    
        keys_to_transpose.append(original_chords)
        counter += 1
    #----------------------------------------------------------------------------
    print (line)
    print ('These are your original keys:')
    for key in keys_to_transpose:
        if key in major_key_list:
            original_MAJOR_func(key)
            print (key)
        if key in minor_key_list:
            original_MINOR_func(key)
            print (key)
    #----------------------------------------------------------------------------
    print (line)
    print ('These are your Transposed Keys:')
    for key in keys_to_transpose:
        if key in major_key_list:
            transposing_major_func(key)
        if key in minor_key_list:
            transposing_minor_func(key)
            
    print('Done')


transpose_steps = ''

def halfstep_calc(starting_key,ending_key):
    global transpose_steps
    if starting_key in major_key_list:
        starting_digit = major_key_list['%s' % starting_key]
        ending_digit = major_key_list['%s' % ending_key]
        transpose_steps = abs(starting_digit - ending_digit)
    if starting_key in minor_key_list:
        starting_digit = minor_key_list['%s' % starting_key]
        ending_digit = minor_key_list['%s' % ending_key]
        transpose_steps = abs(starting_digit - ending_digit)

original_major_chord_value = ''
def original_MAJOR_func(keys):
    global original_major_chord_value
    original_major_chord_value = major_key_list[ "%s" % keys ]

original_minor_chord_value = ''
def original_MINOR_func(keys):
    global original_minor_chord_value
    original_minor_chord_value = minor_key_list[ "%s" % keys ]


def transposing_major_func(keys):
    global transpose_steps
    keys = keys
    new_transposed_chords = (major_key_list[ "%s" % keys ] + transpose_steps)
    if new_transposed_chords < 12:
        print (list_of_major_chords[new_transposed_chords-1])
    elif new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
        print (list_of_major_chords[new_transposed_chords-1])

def transposing_minor_func(keys):
    global transpose_steps
    keys = keys
    new_transposed_chords = (minor_key_list[ "%s" % keys ] + transpose_steps)
    if new_transposed_chords < 12:
        print (list_of_minor_chords[new_transposed_chords-1])
    elif new_transposed_chords > 12:
        new_transposed_chords = new_transposed_chords - 12
        print (list_of_minor_chords[new_transposed_chords-1])

if __name__ == "__main__":
    main()
