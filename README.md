# PyGematria 
The [PyGematria](github.com/ian-nai/pygematria) package makes numerological analysis of texts easy and accessible, and supports multiple gematria systems and alphabets/languages. The package can also translate words and sentences back and forth from numbers to letters, preserving capitalization and punctuation from the original strings.

<p align="center">
<img src="https://raw.githubusercontent.com/ian-nai/gematria/refs/heads/main/isopsephic_stele.jpg?token=GHSAT0AAAAAACWFJMCQMMRXUHGGCQ3B2H3KZYFPHOA" height="376" width="183.5">
</p>

[The photo above is an example of isopsephy from the Sanctuary of Artemis Orthia, 2nd century AD](https://commons.wikimedia.org/wiki/File:Isopsephic_stele.jpg).

## Supported Systems and Alphabets
The package supports the following systems:

* [The Heinrich Cornelius Agrippa system](https://en.wikipedia.org/wiki/Numerology#Agrippan_method)
* [The Christoph Rudolff system](https://en.wikipedia.org/wiki/Gematria#Latin)
* [Hebrew gematria](https://en.wikipedia.org/wiki/Gematria#methods-of-hebrew-gematria)
* [Greek isopsephy](https://en.wikipedia.org/wiki/Isopsephy)
* [English Qaballa](https://en.wikipedia.org/wiki/English_Qaballa)

When no system is specified by the user, the package defaults to the Agrippa method. The systems above can be called in functions using the following arguments:

* Agrippa: 'agrippa'
* Rudolff: 'rudolff'
* Hebrew: 'hebrew'
* Greek isopsephy: 'greek'
* English Qaballa: 'eq'

## Installation

The package can be installed via pip:
```python
pip install pygematria
```

Or by cloning the GitHub repository.

## Example Usage

To convert a string (or list of strings) to its numerical value, simply pass the string (or list) to the string_values function:

```python
import pygematria
from pygematria import conv

# getting the values of individual letters
conv.string_values('Hi')
# returns [8, 9]

# getting the values of words by passing a list
conv.string_values(['Hello', 'world'])
# returns [103, 1054]
```

We can also specify a different dictionary very easily when calling the function:
```python
conv.string_values(['Hello', 'world'], 'eq')
# returns [40, 30]
```

To return both the letters/words and their values as tuples, use the string_and_num_values function:

```python
# getting the values of individual letters
conv.string_and_num_values('Hi')
# returns  [('H', '8'), ('i', '9')]

# getting the values of words by passing a list
conv.string_and_num_values(['Hello', 'world'])
# returns  [('Hello', '103'), ('world', '1054')]
```

Specifying a different dictionary:
```python
conv.string_and_num_values(['Hello', 'world'], 'rudolff')
# returns  [('Hello', '49'), ('world', '67')]
```


## Full List of Functions

#### Please note: the examples below default to using the Agrippa dictionary. If you would like to use a different dictionary, specify it where 'dict_name' is indicated in the function call. 

#### When an 'l' is included next to a number, it indicates that the letter with that value was lowercase in the original string. Including the 'l' marker here allows for the reconstruction of the original string from the returned numerical values. 

## string_values('string' or [list], 'dict_name')
Takes either a string or list of strings, and outputs a list of integers with the numerological value of the strings passes--e.g., passing ['This', 'is', 'a', 'test.'] returns [207, 99, 1, 295].

#### Example:
```python
conv.string_values('Test.')
# returns [100, 5, 90, 100]
```

 ## string_and_num_values('string' or [list], 'dict_name')
Takes either a string or list of letters or words and returns tuples of the letters or words and their numerical values as a list--e.g., passing ['This', 'is', 'a', 'test.'] returns the following: [('This', '207'), ('is', '99'), ('a', '1'), ('test.', '295')].

#### Example:
```python
conv.string_and_num_values('Test')
# returns [('T', '100'), ('e', '5'), ('s', '90'), ('t', '100')]
```

### nums_to_list('string' or [list])
Takes either a string or list of numbers and outputs them to a list for later parsing. For a string, ensure there are only "+" signs between numbers for proper parsing (e.g., '100 + 20'). When passing lists, the function can handle multiple words written as strings like the example above--e.g., ['100 + 8 + 9 + 90', '9 + 90'], which returns as ['100', '8', '9', '90', 'space', '9', '90'].

#### Example:
```python
conv.nums_to_list(['100 + 8 + 9 + 90', '9 + 90'])
# returns ['100', '8', '9', '90', 'space', '9', '90']
```

## lets_to_nums('string' or [list], 'dict_name')
Takes either a string or a list of letters and converts them to numbers, returning a list. 

#### Example:
```python
conv.lets_to_nums('Test.')
# returns ['100', '5l', '90l', '100l', '.']
```

## nums_to_lets('string' or [list], 'caps_setting', 'dict_name')
Takes either a string or a list of numbers and converts them to letters, returning a list. The "caps_setting" field takes defaults to standard (returning lowercase for any number marked with an 'l'), but can also be set to 'lowercase' and 'caps' if the user would like an entirely capitalized or lowercase string.

#### Example:
```python
conv.lets_to_nums(['100', '5l', '90l', '100l', '.'])
# returns ['Test.']
```

## num_list_to_words([list], 'caps_setting', 'dict_name')
Takes a list of numbers and outputs a list of words--e.g., given ['100', '8l', '9l', '90l'], the function returns 'Test'. The "caps_setting" field takes defaults to standard (returning lowercase for any number marked with an 'l'), but can also be set to 'lowercase' and 'caps' if the user would like an entirely capitalized or lowercase string.

#### Example:
```python
conv.num_list_to_words(['100', '8l', '9l', '90l', 'space', '9l', '90l', 'space', '1l', 'space', '100l', '5l', '90l', '100l', '.'])
# returns 'This is a test.'
```
