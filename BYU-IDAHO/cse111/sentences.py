import random

# #################################### #
# File: sentences.py                   #
# Author: John Asada                   #
# Purpose: A Milestone Assignment      #
# #################################### #

def get_determiner(quantity = 1):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity = 1):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    
    if quantity == 1:
        words = [ "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    
    else:
        words = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    word = random.choice(words)
    return word
    
def get_verb(quantity = 1, tense = "present"):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    word = random.choice(words)
    return word

def get_preposition():
    """
    Return a randomly choosen preposition 
    from this list of prepositons
    "about", "above", "across", "after", "along", 
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of", 
    "off", "on", "unto", "out", "over",
    "past", "to", "under", "with", "without"
    
    Return : a radomly choosen position
    """
    prepositions = ["about", "above", "across", "after", "along", 
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of", 
    "off", "on", "unto", "out", "over",
    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity = 1):
    """
    Build and return a prepositional phrase composed of three(3) words:
    A preposition, a determinder and a noun by calling the
    'get_preposition', 'get_determiner' and ' get_noun' functions.
    Parameters 
        quantity: an integer that determines if the determinder and nouns are singular or plural.
    Return : a prepositional phrase"""
    
    return f"{get_preposition()} {get_determiner(quantity=quantity)} {get_noun(quantity=quantity)} "

def random_word_creator():
    patterns = [
        "f\'{get_determiner()} {get_noun()} {get_verb(tense=\"past\")}\'",
        "f\'{get_determiner()} {get_noun()} {get_preposition()} {get_determiner()} {get_noun()} {get_verb(tense=\"present\")}\'",
        "f\'{get_prepositional_phrase(2)}\'",
        "f\'{get_determiner()} {get_noun()} {get_preposition()} {get_verb(tense=\"past\")} \'"
    ]
    return str(eval(random.choice(patterns))).capitalize()

def main():
    print("Welcome to Sentence creator\nInput the amount of sentences needed: ", end="")
    amount = int(input())
    for _ in range(amount):
        print(random_word_creator())
    print("Thanks for using sentence creator app")

main()
