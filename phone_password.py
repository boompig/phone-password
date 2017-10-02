from argparse import ArgumentParser
import logging

def char_seq_from_phone_number(num, word=""):
    """
    :returns list
    """
    assert type(word) == str, "Argument 'word' must be a string"
    keypad = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    if(len(num) == 0):
        return [word]
    else:
        n = int(num[0])
        assert n in keypad, "Keypads do not have a letter associated with number %d" % n
        words = []
        for letter in keypad[n]:
            assert type(letter) == str
            words.extend(char_seq_from_phone_number(num[1:], word + letter))
        return words

def filter_words(candidate_words):
    dict_file = "/usr/share/dict/words"
    real_words = set([])
    with open(dict_file) as fp:
        for line in fp:
            real_words.add(line.strip())
    real_words.add("squidward")
    real_words.add("daniel")
    logging.debug("Loaded dictionary with %d words", len(real_words))
    return [word for word in candidate_words if word in real_words]

def words_from_number(num):
    candidate_words = char_seq_from_phone_number(num)
    real_words = filter_words(candidate_words)
    return real_words

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("phone_number")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    words = words_from_number(args.phone_number)
    if words:
        print "The following words match the number sequence:"
        for word in words:
            assert type(word) == str
            print(word)
    if words == []:
        print "Error: no words found for this sequence"
