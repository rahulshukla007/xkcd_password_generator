import random
import argparse

#Parser for command-line options
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", type=int, default=4, help="include WORDS words in the password")
parser.add_argument("-c", "--caps",  type=int, default=0, help="capitalize the first letter of CAPS random words")
parser.add_argument("-n", "--numbers", type=int, default=0, help="insert NUMBERS random numbers in the password")
parser.add_argument("-s", "--symbols", type=int, default=0, help="insert SYMBOLS random symbols in the password")

args = parser.parse_args()

#open the words file
word_text = open("words.txt")

list_of_word = word_text.read().splitlines()

random_words = random.sample(list_of_word, args.words)

caps_counting = 0
list_of_caps_letter = []
#here we check the caps count must be equal or less than total words
if (args.caps > 0 and args.caps <= args.words):
    random_caps = random.sample(random_words, args.caps)
    random_words = list(set(random_words) - set(random_caps))
    while (caps_counting < args.caps):
        list_of_caps_letter.append(random_caps[caps_counting].title())
        caps_counting += 1

    random_words = random_words + list_of_caps_letter
    random.shuffle(random_words)

number_counting = 0
list_of_number = []
if (args.numbers > 0):
    while (number_counting < args.numbers):
        temporary_list = [str(random.randint(0, 9))]
        number_counting += 1
        list_of_number = list_of_number + temporary_list

    random_words = random_words + list_of_number
    random.shuffle(random_words)

if (args.symbols > 0):
    list_of_symbol = ["~","!","@","#","$","%","^","&","*",".",":",";"]
    random_symbol = random.sample(list_of_symbol, args.symbols)

    random_words = random_words + random_symbol
    random.shuffle(random_words)

password_generator = "".join(random_words)
print(password_generator)