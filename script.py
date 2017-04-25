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