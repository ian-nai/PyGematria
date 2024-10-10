import string
from string import punctuation
import re

agrippa_dict = {
    'A': '1',
    'a': '1l',
    'B': '2',
    'b': '2l',
    'C': '3',
    'c': '3l',
    'D': '4',
    'd': '4l',
    'E': '5',
    'e': '5l',
    'F': '6',
    'f': '6l',
    'G': '7',
    'g': '7l',
    'H': '8',
    'h': '8l',
    'I': '9',
    'i': '9l',
    'J': '600',
    'j': '600l',
    'K': '10',
    'k': '10l',
    'L': '20',
    'l': '20l',
    'M': '30',
    'm': '30l',
    'N': '40',
    'n': '40l',
    'O': '50',
    'o': '50l',
    'P': '60',
    'p': '60l',
    'Q': '70',
    'q': '70l',
    'R': '80',
    'r': '80l',
    'S': '90',
    's': '90l',
    'T': '100',
    't': '100l',
    'U': '200',
    'u': '200l',
    'V': '700',
    'v': '700l',
    'W': '900',
    'w': '900l',
    'X': '300',
    'x': '300l',
    'Y': '400',
    'y': '400l',
    'Z': '500',
    'z': '500l',
    ' ': 'space'
}

rudolff_dict = {
    'A': '1',
    'a': '1l',
    'B': '2',
    'b': '2l',
    'C': '3',
    'c': '3l',
    'D': '4',
    'd': '4l',
    'E': '5',
    'e': '5l',
    'F': '6',
    'f': '6l',
    'G': '7',
    'g': '7l',
    'H': '8',
    'h': '8l',
    'I': '9',
    'i': '9l',
    'J': '9j',
    'j': '9jl',
    'K': '10',
    'k': '10l',
    'L': '11',
    'l': '11l',
    'M': '12',
    'm': '12l',
    'N': '13',
    'n': '13l',
    'O': '14',
    'o': '14l',
    'P': '15',
    'p': '15l',
    'Q': '16',
    'q': '16l',
    'R': '17',
    'r': '17l',
    'S': '18',
    's': '18l',
    'T': '19',
    't': '19l',
    'U': '20',
    'u': '20l',
    'V': '20v',
    'v': '20vl',
    'W': '21',
    'w': '21l',
    'X': '22',
    'x': '22l',
    'Y': '23',
    'y': '23l',
    'Z': '24',
    'z': '24l',
    ' ': 'space'
}


english_qaballa_dict = {
    'A': '1',
    'a': '1l',
    'B': '20',
    'b': '20l',
    'C': '13',
    'c': '13l',
    'D': '6',
    'd': '6l',
    'E': '25',
    'e': '25l',
    'F': '18',
    'f': '18l',
    'G': '11',
    'g': '11l',
    'H': '4',
    'h': '4l',
    'I': '23',
    'i': '23l',
    'J': '16',
    'j': '16l',
    'K': '9',
    'k': '9l',
    'L': '2',
    'l': '2l',
    'M': '21',
    'm': '21l',
    'N': '14',
    'n': '14l',
    'O': '7',
    'o': '7l',
    'P': '26',
    'p': '26l',
    'Q': '19',
    'q': '19l',
    'R': '12',
    'r': '12l',
    'S': '5',
    's': '5l',
    'T': '24',
    't': '24l',
    'U': '17',
    'u': '17l',
    'V': '10',
    'v': '10l',
    'W': '3',
    'w': '3l',
    'X': '22',
    'x': '22l',
    'Y': '15',
    'y': '15l',
    'Z': '8',
    'z': '8l',
    ' ': 'space'
}

hebrew_dict = {
    'א': '1',
    'בּ': '1',
    'ב': '2',
    'גּ': '3',
    'ג': '3',
    'דּ': '4',
    'ד': '4',
    'ה': '5',
    'ו': '6',
    'ז': '7',
    'ח': '8',
    'ט': '9',
    'י': '10',
    'כּ': '20',
    'כ': '20',
    'ךּ': '20',
    'ך': '20',
    'ל': '30',
    'מ': '40',
    'ם': '40',
    'נ': '50',
    'ן': '50',
    'ס': '60',
    'ע': '70',
    'פּ': '80',
    'פ': '80',
    'ףּ': '80',
    'ף': '80',
    'צ': '90',
    'ץ': '90',
    'ק': '100',
    'ר': '200',
    'שׁ': '300',
    'שׂ': '300',
    'תּ': '400',
    'ת': '400',
    ' ': 'space'
}


iso_dict = {
    'Α': '1',
    'α': '1l',
    'Β': '2',
    'β': '2l',
    'Γ': '3',
    'γ': '3l',
    'Δ': '4',
    'δ': '4l',
    'Ε': '5',
    'ε': '5l',
    'Ϝ': '6',
    'ϝ': '6l',
    'Ϛ': '6',
    'ϛ': '6l',
    'Ζ': '7',
    'ζ': '7l',
    'Η': '8',
    'η': '8l',
    'Θ': '9',
    'θ': '9l',
    'Ι': '10',
    'ι': '10l',
    'Κ': '20',
    'κ': '20l',
    'Λ': '30',
    'λ': '30l',
    'Μ': '40',
    'μ': '40l',
    'Ν': '50',
    'ν': '50l',
    'Ξ': '60',
    'ξ': '60l',
    'Ο': '70',
    'ο': '70l',
    'Π': '80',
    'π': '80l',
    'Ϙ': '90',
    'ϙ': '90l',
    'Ρ': '100',
    'ρ': '100l',
    'Σ': '200',
    'σ': '200l',
    'Τ': '300',
    'τ': '300l',
    'Υ': '400',
    'υ': '400l',
    'Φ': '500',
    'φ': '500l',
    'Χ': '600',
    'χ': '600l',
    'Ψ': '700',
    'ψ': '700l',
    'Ω': '800',
    'ω': '800l',
    'Ϡ': '900',
    'ϡ': '900l',
    ' ': 'space'
}


greek_dict = {
    'Α': '1',
    'α': '1l',
    'Β': '2',
    'β': '2l',
    'Γ': '3',
    'γ': '3l',
    'Δ': '4',
    'δ': '4l',
    'Ε': '5',
    'ε': '5l',
    'Ϝ': '6',
    'ϝ': '6l',
    'Ϛ': '6',
    'ϛ': '6l',
    'Ζ': '7',
    'ζ': '7l',
    'Η': '8',
    'η': '8l',
    'Θ': '9',
    'θ': '9l',
    'Ι': '10',
    'ι': '10l',
    'Κ': '20',
    'κ': '20l',
    'Λ': '30',
    'λ': '30l',
    'Μ': '40',
    'μ': '40l',
    'Ν': '50',
    'ν': '50l',
    'Ξ': '60',
    'ξ': '60l',
    'Ο': '70',
    'ο': '70l',
    'Π': '80',
    'π': '80l',
    'Ϙ': '90',
    'ϙ': '90l',
    'Ρ': '100',
    'ρ': '100l',
    'Σ': '200',
    'σ': '200l',
    'Τ': '300',
    'τ': '300l',
    'Υ': '400',
    'υ': '400l',
    'Φ': '500',
    'φ': '500l',
    'Χ': '600',
    'χ': '600l',
    'Ψ': '700',
    'ψ': '700l',
    'Ω': '800',
    'ω': '800l',
    'Ϡ': '900',
    'ϡ': '900l',
    ' ': 'space'
}

num_to_let_dict_agrippa = {value: key for key, value in agrippa_dict.items()}
num_to_let_dict_rudolff = {value: key for key, value in rudolff_dict.items()}
num_to_let_dict_english_qaballa = {value: key for key, value in english_qaballa_dict.items()}
num_to_let_dict_hebrew = {value: key for key, value in hebrew_dict.items()}
num_to_let_dict_greek = {value: key for key, value in greek_dict.items()}

def nums_to_list(input_list):
    if isinstance(input_list, str):
        list_of_all_words = []
        split_list = input_list.split("+")
        no_spaces_list = []
        for entry in split_list:
            entry = entry.replace(" ", "")
            no_spaces_list.append(str(entry))

        return no_spaces_list
    
    if isinstance(input_list, list):
        list_of_all_words = []
        for num in input_list:
            split_list = num.split("+")
            split_list.append("space")
            no_spaces_list = []
            for entry in split_list:
                entry = entry.replace(" ", "")
                no_spaces_list.append(entry)
            list_of_all_words.append(no_spaces_list)
        
        final_list = [x for xy in list_of_all_words for x in xy]

        # removing the final space
        final_list.pop()
        return final_list
    
# function to take list of words and output gematric values - can input each using string_to_nums in a wrapper function
def list_to_nums(input_list, dict_name="agrippa"):
    final_list = []
    for el in input_list:
        num_to_append = string_to_nums(el, dict_name)
        final_list.append(num_to_append)

    return final_list

        

def string_to_nums(input_string, dict_name="agrippa"):
    if dict_name == "agrippa":
        cur_string_to_num_dict = agrippa_dict
    elif dict_name == "rudolff":
        cur_string_to_num_dict = rudolff_dict
    elif dict_name == "hebrew":
        cur_string_to_num_dict = hebrew_dict
    elif dict_name == "eq":
        cur_string_to_num_dict = english_qaballa_dict
    elif dict_name == "greek":
        cur_string_to_num_dict = greek_dict
    raw_values = []
    for letter in input_string:
        for key, value in cur_string_to_num_dict.items():
            if key == letter:
                raw_values.append(value)
        if letter in punctuation:
            raw_values.append(letter)

    return raw_values

def nums_to_combined(input_list):
    final_list = []
    temp_list = []
    for i in input_list:
        if i == 'space':
            final_list.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)

    final_list.append(temp_list)

    final_cleaned_nums = []
    final_cleaned_strs = []
    for sublist in final_list:
        temp_sublist_strs = []
        temp_sublist_nums = []
        for j in sublist:
            j = re.sub('[^0-9]','', j)
            if j:
                temp_sublist_nums.append(int(j))
                temp_sublist_strs.append(j)
        final_cleaned_nums.append(temp_sublist_nums)
        final_cleaned_strs.append(temp_sublist_strs)

    simple_nums = []
    for num_sublist in final_cleaned_nums:
        simple_nums_sublist = sum(num_sublist)
        simple_nums.append(simple_nums_sublist)

    complex_nums = []
    for str_sublist in final_cleaned_strs:
        complex_sublist = (' + ').join(str_sublist)
        complex_nums.append(complex_sublist)

    return complex_nums


def num_list_to_words(input_nums, caps_setting="standard", dict_name="agrippa"):
    if dict_name == "agrippa":
        cur_num_to_let_dict = num_to_let_dict_agrippa
    elif dict_name == "rudolff":
        cur_num_to_let_dict = num_to_let_dict_rudolff
    elif dict_name == "hebrew":
        cur_num_to_let_dict = num_to_let_dict_hebrew
    elif dict_name == "eq":
        cur_num_to_let_dict = num_to_let_dict_english_qaballa
    elif dict_name == "greek":
        cur_num_to_let_dict = num_to_let_dict_greek
    if caps_setting == "caps":
        string_list = []
        for character in input_nums:
            if str(character) in cur_num_to_let_dict:
                string_list.append(cur_num_to_let_dict[character])
            elif str(character) in string.punctuation:
                string_list.append(character)
            else:
                pass
        caps_list = [char.upper() for char in string_list]
        final_list = ''.join(caps_list)
        return(final_list)
    if caps_setting == "lower":
        string_list = []
        for character in input_nums:
            if character in cur_num_to_let_dict:
                string_list.append(cur_num_to_let_dict[character])
            elif character in string.punctuation:
                string_list.append(character)
            else:
                pass
        caps_list = [char.lower() for char in string_list]
        final_list = ''.join(caps_list)
        return(final_list)

    if caps_setting == "standard":
        string_list = []
        for character in input_nums:
            if character in cur_num_to_let_dict:
                string_list.append(cur_num_to_let_dict[character])
            elif character in string.punctuation:
                string_list.append(character)
            else:
                pass
        final_list = ''.join(string_list)
        return(final_list)


# converting our string of numbers into a combined value
def add_numbers(input_list):
    for el in input_list:
        ints_in_string = [int(x) for x in re.findall(r'\d+', el)]
        final_sum = sum(ints_in_string)
        return final_sum   


# take a list of words, then get each value of word and return a tuple with the word and the value
def string_and_num_values(input_list, dict_name="agrippa"):
    if isinstance(input_list, str):
        final_list = []
        for el in input_list:
            num_to_combine = string_to_nums(el, dict_name)
            combined_val = nums_to_combined(num_to_combine)
            final_sum = add_numbers(combined_val)
            final_list.append((el, str(final_sum)))
            for val in final_list:
                if val[1] == '0':
                    final_list.remove((val[0], val[1]))
        
        return final_list


    elif isinstance(input_list, list):
        final_list = []
        for el in input_list:
            num_to_combine = string_to_nums(el, dict_name)
            combined_val = nums_to_combined(num_to_combine)
            final_sum = add_numbers(combined_val)
            final_list.append((el, str(final_sum)))

        return final_list

# returns the numerical value of a string
def string_values(input_list, dict_name="agrippa"):
    if isinstance(input_list, str):
        final_list = []
        for el in input_list:
            num_to_combine = string_to_nums(el, dict_name)
            combined_val = nums_to_combined(num_to_combine)
            final_sum = add_numbers(combined_val)
            final_list.append((final_sum))
            for val in final_list:
                if val == 0:
                    final_list.remove(val)
        
        return final_list


    elif isinstance(input_list, list):
        final_list = []
        for el in input_list:
            num_to_combine = string_to_nums(el, dict_name)
            combined_val = nums_to_combined(num_to_combine)
            final_sum = add_numbers(combined_val)
            final_list.append(final_sum)

        return final_list


def lets_to_nums(input, dict_name="agrippa"):
    if isinstance(input, str):
        returned_nums = string_to_nums(input, dict_name)
        return returned_nums
    elif isinstance(input, list):
        string_to_pass = ''.join(str(x) for x in input)
        returned_nums = string_to_nums(string_to_pass, dict_name)
        return returned_nums

def nums_to_lets(input, caps_setting="standard", dict_name="agrippa"):
    if isinstance(input, str):
        words = input.split()
        words = [''.join(char for char in s if char not in string.punctuation) for s in words]
        words = [s for s in words if s]
        returned_lets = num_list_to_words(words, caps_setting, dict_name)
        return returned_lets
    elif isinstance(input, list):
        list_of_strings = []
        for x in input:
            list_of_strings.append(str(x))
        returned_lets = num_list_to_words(list_of_strings, caps_setting, dict_name)
        return returned_lets
    elif isinstance(input, int):
        returned_lets = num_list_to_words(input, caps_setting, dict_name)
        return returned_lets