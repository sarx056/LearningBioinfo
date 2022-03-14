"""mini project time! we're gonna make a mystical octosphere or whatever that is lol
so the user gets to ask some questions and the computer will answer yes or no,
its like telling fortunes"""

import random

def number_to_fortune(num):
    """lets make a helper function to assign answers to numbers"""

    if num == 0:
        return 'yes!'
    if num == 1:
        return 'no, sorry:( '
    if num == 3:
        return 'maybe yes maybe not'
    else:
        return 'out of range, no answers!'


def main(question):
    """writing the main function which is pretty simple"""

    print((input('ask your question to the mystical octosphere!: ')))
    print('shaking the octosphere....')
    answer = random.randrange(0, 3)
    answer_fortune = number_to_fortune(answer)
    print('white cloud starts swirling and changing color....')
    print('the octosphere says ' + answer_fortune)


# test the code
main('test')
main('test')
main('test')
