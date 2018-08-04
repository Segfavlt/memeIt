import argparse

class damnitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-d'):
        st  = "damnit " + values
        st = st.upper()
        print("```")
        print(" ".join(st))
        for (index,letter) in enumerate(st[1:],0):
                # twice the index b/c of the characters in between
                print('{0} {1}{0}'.format(letter,' '*2*index))
        print("```")


class spongeBobAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-s'):
        letters = '' 
        # add spaces to separate words
        for value in values:
            letters += value + ' '
        meme = ''
        for i in range(len(letters)):
            if (i%2 != 0):
                meme += letters[i].upper()
            else:
                meme += letters[i]
        print(meme)

class lossAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string='-l'):
        print('|   ||')
        print('||  |_')
