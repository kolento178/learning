"""
# m = 100<99
# n=0xff==255
# print(m)
# print(n)

# print('hello,python')

# print('hello','python')		


# #print('hello')		

# x1=1
# d=3
# n=100
# x100=x1+3*(n-1)
# s=(x1+x100)*n/2						
# print(s)

# print rto be,or not to be":that was a question

# a='python'
# print'hello',a or 'world'
# b=('')
# print'hello',b or 'world'
#
# a=��ASDFGHJKL��
# print(a[:4])
"""



"""
print("Mary had a little lamb")
print("Its fleece was white as %s." % 'snow')
print("And everywhere thatMary went.")
print("."*10)   #what'd that do?

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1+end2+end3+end4+end5+end6+end7+end8+end9+end10+end11+end12)
"""



'''
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ("I had this thing.",
                   "That you could type right.",
                   "But it didn't sing.",
                   "So I said goodnight."
                   )
      )
'''



'''
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)

print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to types as much as we like.
Even 4 lines if we want, or 5, or 6.
    """)
'''



'''
from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s, I'm the %s script. " % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s ?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer))
'''




'''
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Flshies
\t* Catnip\n\t* Grass

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
'''




'''
print("How old are you?"),
age = input()

print("How tall are you?"),
height = input()

print("How much do you weigh."),
weight = input()

print("So,you're %r old,%r tall and %r heavy." % (age, height, weight))
'''




'''
from sys import argv


num = 0
for i in argv:
    print(i)
    if num == 1:
        print("The script is called:", i)
    elif num == 2:
        print("Your first variable is:", i)
    elif num == 3:
        print("Your second variable is:", i)
    elif num == 4:
        print("Your third variable is:", i)

# script, first, second, third = argv
# print("The script is called:", script)
#
# print("Your first variable is:", first)
#
# print("Your second variable is:", second)
#
# print("Your third variable is:", third)
'''





'''
from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
'''




'''
from sys import argv

niu, wen, ha, li = argv

print("The script is called:")
input(niu)

print("Your first variable is:")
input(wen)

print("Your second variable is:")
input(ha)

print("Your third variable is:")
input(li)
'''




'''
from sys import argv

script, user_name, niuge = argv
prompt = '>'

print("Hi %s,I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions, %s." % niuge)
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
    """ % (likes, lives, computer))
'''




'''
from sys import argv        #����ģ��

script, filename = argv     #���ò�������
txt = open(filename)        #����open�������ļ�

print("Here's your file %r" % filename)        #��ӡ
print(txt.read())                              #��ȡ�ļ�

print("Type the filename again:")              #��ӡ
file_again = input(">")                        #����>

txt_again = open(file_again)                   #���ļ�
print(txt_again.read())                        #��ȡ�ļ�
'''




'''
#�����ĵ�
from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C)")
print("If you do want that, hie RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
'''




'''
#�����ĵ�
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s " % (from_file, to_file))
indata = open(from_file).read()
print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %s" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright all done.")

out_file.close()

# from sys import argv
# script, from_file, to_file = argv
# out_file = open(to_file, 'w').write(open(from_file).read())        #һ�д���

import sys
out_file = open(sys.argv[1], 'w').write(open(sys.argv[2]).read())
'''






'''
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %r" % arg1)


def print_none():
    print("I got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()
'''




"""
from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline)

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
"""




'''
print("Let's practice everything.")
print('You\'d need to know\'but escapes with \\that do \nnewlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10-2+3-6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d bean, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point/10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, %d crates." % (beans, jars, crates))
'''




'''
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
aa = break_words('I am liqiang 1 2 3 4')
print(aa)
for i in aa:
    print(i)


def sort_words(words):
    """Sorts the words."""
    return sorted(words)
print(sort_words('acdb'))


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    return ['llll']
print_first_word(['j', 'a', 'ug', 'ea'])


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
print(sort_sentence('Takes in a full sentence and returns the sorted words.'))


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
print_first_and_last('Prints the first and last words of the sentence.')


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
print_first_and_last_sorted("Sorts the words then prints the first and last one.")
'''




'''
import testy

aa = testy.break_words('I am liqiang 1 2 3 4')
print(aa)
for i in aa:
    print(i)

print(test.sort_words('acdb'))

test.print_first_word(['j', 'a', 'ug', 'ea'])
print(test.sort_sentence('Takes in a full sentence and returns the sorted words.'))
test.print_first_and_last('Prints the first and last words of the sentence.')
test.print_first_and_last_sorted("Sorts the words then prints the first and last one.")
'''





'''
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'about escapes with \\that do \nnewlines and \ttabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "All god\tthings come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
'''





'''
True and True
2. False and True
3. 1 == 1 and 2 == 1
4. "test" == "test"
5. 1 == 1 or 2 != 1
6. True and 1 == 1
7. False and 0 != 0
8. True or 1 == 1
9. "test" == "testing"
10.1 != 0 and 2 == 1
11."test" != "testing"
12."test" == 1
13.not (True and False)
14.not (1 == 1 and 0 != 1)
15.not (10 == 1 or 1000 == 1000)
16.not (1 != 10 or 3 == 4)
17.not ("testing" == "testing" and "Zed" == "Cool Guy")
18.1 == 1 and not ("testing" == 1 or 1 == 0)
19."chunky" == "bacon" and not (3 == 4 or 3 == 3)
20.3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
'''





"""
print("You enter a dark room with two doors. Do you go through door #1 or #2?")

door = input(">")
while int(door) > 0:
    if door == "1":
        print("There's a giant bear here eating a  cheese cake. What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear")

        bear = input(">")

        if bear == "1":
            print("The bear eats you face off. Good job!")
        elif bear == "2":
            print("The bear eats your legs off. Good jobs!")
        else:
            print("Well, doing %s is probably better. Bear runs away." % bear)
    elif door == "2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries.")
        print("2. Yellow jacket clothespins.")
        print("3. Understanding revolvers yelling melodies.")

        insanity = input(">")

        if insanity == "1" or insanity == "2":
            print("Your body survives powered by a mind of jello. Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck. Good job!")
    if door == "3":
        print("aha,I know you")
        door == "1"

    else:
        print("You stumble around and fall on a knife and die. Good job!")
    break
"""





"""
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s " % fruit)

for i in change:
    print("I got %r" % i)

elements = []
for i in range(0, a):
    print("Adding %d to the list." % i)
    elements.append(i)
for i in elements:
    print("Element was: %d" % i)
print(elements)
"""




"""
i = 0
numbers = []
a = 3

for i in range(0, a):
    print("At the top i is %d" % i)
    numbers.append(i)
    i += 1
    print("Now the number is :", numbers)
    print("At the bottom i is %d" % i)
print("The numbers:")
for num in numbers:
    print(num)
"""





"""
from sys import exit


def gold_room():
    print("This room is full o gold. How much do you take?")

    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print("There is a beat here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    # while True:
    #     next = input(">")
    #
    #     if next == "take honey":
    #         dead("The bear looks at you then slaps your face off")
    #     elif next == "taunt bear" and not bear_moved:
    #         print("The bear has moved from the door. You can go through it now.")
    #         bear_moved = True

    while True:
        next = input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")

    next = input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
"""





"""
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print("NY state has:", cities['NY'])
print("Or State has:", cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-'*10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print("The city for the state 'TX' is: %s" % city)
"""




"""
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family"
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
"""




# class Song(object):
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around me",
#                         "With pockets full of it"])
#
# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()




""""
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line, ha in self.lyrics.items():
            print(line, ha)

happy_bday = Song({"Happy birthday to you": "na",
                   "I don't want to get sued": "la",
                   "So I'll stop right there": "fa"})

bulls_on_parade = Song({"They rally around me": "hi",
                        "With pockets full of it": "ma"})

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
"""     





'''
class Animal(object):

    def __init__(self, move):
        self.move = move


class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        self.name = name


class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

    def employer(self, emploo):
        self.emploo = "how are you"




class Salmon(Fish):

    pass



rover = Dog('Rover')
satan = Cat('Santan')
mary = Person('Mary')


class Map(object):
    
    pass


class Engine(object):
    
    def __init__(self, play):
        self.play = play

xiaoming = Employee('xiaoming')
print(super(xiaoming.name))
'''






"""
# class Fish(object):
#     def __init__(self, eating):
#         self.eating = eating
# class Halibut(Fish):
#     def __init__(self, swimming):
#         super().__init__('eating')
#         self.swimming = swimming
#     pass
# 
# print(Halibut('xiaoming').eating)

class Fish(object):
    _eating = ''
    ddddddddd = ''

    def __init__(self):
        pass

    def __init__(self, eating):
        self._eating = eating

    def getEating(self):
        return self._eating

    def setEating(self, eating):
        self._eating = eating
        return self

class Halibut(Fish):
    def __init__(self, swimming):
        super().__init__('eating')
        self.swimming = swimming
    pass
Halibut('xiaoming').setEating('asdsaf').ddddddddd = "sssssss"
print()

# class Fish(object):
#     def eat(self):
#         print('eating Fish.')
# 
# 
# class Halibut(Fish):
#     def __init__(self, name):
#         self.name = name
# 
#     def swimming(self):
#         print('I\'m '+ self.name + ', i am swimming.')
# xiaoming = Halibut('xiaoming')
# xiaoming.eat()
# xiaoming.swimming()
"""                     #�̳�





""""
import random
import urllib.request
import sys

WORD_UrL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class Mouse(object)":
      "Make a class named Mouse that is-a object",
    "class Cat(object):\n\tdef __init__(self, miao)":
      "class cat has-a __init__(self, miao)",
    "class Fish(object):\n\tdef swimming(self, swim)":
      "class fish has-a function named swimming that takes self and swim",
    "mikey = Mouse()":
      "Set mikey to an instant of class Mouse",
    "Fish.swimming(swim)":
      "From Fish get the swimming function,and call it with parameters self,swim",
    "swimming.swim = 'swim'":
    "From swimming get the swim attribute and set it to 'swim'."
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True


# load up the words from the website
for word in urllib.request.urlopen(WORD_UrL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count('###'))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range (0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_name:
            result = result.replace("###", word, 1)

        # fake other names
            for word in other_names:
                result = result.replace("***", word, 1)

        # fake parameter lists
            for word in param_names:
                result = result.replace("@@@", word, 1)
"""




"""
class Animal(object):
    speak_type = ''

    def speak(self):
        print(self.speak_type)

    def getSpeak_type(self):
        return self.speak_type

    def setSpeak_type(self, speak_type):
        self.speak_type = speak_type


class Cat(Animal):
    def __init__(self, speak_type1):
        super(Cat, self).setSpeak_type(speak_type1)


class Dog(Animal):
    def __init__(self, speak_type1):
        super(Dog, self).setSpeak_type(speak_type1)


def i_want_it(animal):
    if isinstance(animal, Animal):
        animal.speak()


i_want_it(Cat('lll'))
i_want_it(Dog('wangwang'))


# class A(object):
#     t = 'dd'
#     def getT(self):
#         return self.t
#
#     def setT(self,t):
#         self.t = t
# class B(A):
#     def __init__(self):
#         super(B, self).setT('ggg')
#         print(super(B, self).getT())
#
# B()


class Animal(object):

    def speak(self, speak_type):
        print("%s" % speak_type)


class Cat(Animal):
    def __init__(self, speak_type1):
        super(Cat, self).speak(speak_type1)

maomi = Cat("hahaha")
"""




# ������ʽ
# import re
#
# a = 'adkdxxIxxkldaofxkxxlovexxkdklxxyouxxkdkjlka'
#
# s = re.findall('xx(.*?)xx', a)
# print(s[1])
# for each in s:
#     print(each)
#
# w = re.search('\w+xx(.*?)xx\w+xx(.*?)xx\w+xx(.*?)xx', a).group(2)
# print(w)
#
# h = re.sub('I(.*?)love', '123%d45'%123, a)
# print(h)

