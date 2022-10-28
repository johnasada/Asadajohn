from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest

prepositions = ["about", "above", "across", "after", "along", 
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of", 
    "off", "on", "unto", "out", "over",
    "past", "to", "under", "with", "without"]
singular_determiners = ["the", "one"]
plural_determiners = ["some", "many"]
singular_nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]
plural_nouns = ["adults", "birds", "boys", "cars", "cats",
    "children", "dogs", "girls", "men", "women"]
past_tense = ["drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"]
singular_present_tense = ["drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"]
plural_present_tense = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
prepositions = ["about", "above", "across", "after", "along", 
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of", 
    "off", "on", "unto", "out", "over",
    "past", "to", "under", "with", "without"]
def test_get_determiner():
    # Test the singular determiners.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
        
def test_get_noun():
    
    # Test the singular nouns.
    
    for _ in range(4):
        word = get_noun(1)
        
        # Verify that the word returned from get_noun
        # is one of the words in the singular_nouns list.
        assert word in singular_nouns
        
    
    for _ in range(4):
        # Test the plural nouns.
        word = get_noun(2)
        # Verify that the word returned from plural_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns
        
def test_get_verb():
    # Test the past tense of verbs
    
    for _ in range(4):
        word = get_verb(0, "past")
        
        # This verify that the word returned from get_verb
        # is one of the words from past_tense list
        assert word in past_tense
    
    
    for _ in range(4):
        word = get_verb(1, "present")
        
        # This verify that the word returned from get_verb
        # is one of the words from singular_present_tense list
        assert word in singular_present_tense
    
    
    
    for _ in range(4):
        word = get_verb(2, "present")
        # This verify that the word returned from get_verb
        # is one of the words from plural_present_tense list.
        assert word in plural_present_tense
        
      
    
    for _ in range(4):
        word = get_verb( 1, "future")
        
        # This verify that the word returned from get_verb
        # is one of the words from future_tense list.
        assert word in future_tense
def test_get_preposition():
    
    for _ in range(len(prepositions)):
        assert get_preposition() in prepositions
    
def test_prepositional_phrase():
    for _ in range(6):
        sentences = get_prepositional_phrase().split()
        assert sentences[0] in prepositions
        assert sentences[1] in singular_determiners
        assert sentences[2] in singular_nouns
    for _ in range(6):
        sentences = get_prepositional_phrase(2).split()
        assert sentences[0] in prepositions
        assert sentences[1] in plural_determiners
        assert sentences[2] in plural_nouns

#Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])