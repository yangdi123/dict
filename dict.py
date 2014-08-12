#!/usr/bin/env python3

import sys
import os


def checkWordList(word):
    """
    check the word . if it in wordList .program continue
    """
    flag = None
    with open('/usr/share/dict/american-english') as f:
        for line in f:
            if line.strip().lower() == word:
                # convert the word in list to lowercase
                flag = True
    if flag:
        return word
    else:  # else the program exit
        print()
        print("(~_~): Are you sure {:-^8} is a word?".format(word))
        print()
        sys.exit()


def searchWord(word):
    flag = None
    text = None
    with open('/home/dave/dict/dict') as f:
        for line in f:
            if line.split(':')[0] == word:
                text = line
                flag = True
    if flag:  # if find the word record print it.
        for _ in text.split(':'):
            print(_)
    else:     # else interactive ask user wheather add the word
        print('(#_#): {:-^8} not in my dictionary!'.format(word))
        print(' ')
        yes = {'y', 'yes'}
        if input('add {}. y/n: '.format(word)) in yes:
            addWord(word)


def addWord(word):
    """
    add the user input
    """
    list = ['英音', '美音', 'vt.', 'vi.', 'adj.', 'adv.', 'n.', 'other. ']
    print(''+word)
    content = str()
    for _ in list:
        text = input(_)
        if text:
            content += ':' + _ + text
    line = word + content
    with open('/home/dave/dict/dict', 'a', encoding='utf8') as f:
        f.write(line+'\n')
    os.system('sort /home/dave/dict/dict > /home/dave/dict/dict.tmp')
    os.system('mv /home/dave/dict/dict.tmp /home/dave/dict/dict')
    print('Add successfully!')


def countWords():
    """
    traversal
    """
    nu = 0
    for line in open('/home/dave/dict/dict'):
        nu += 1
    print()
    print('(^_^): already have {} words!'.format(nu))
    print()


def main():
    for word in words:
        word = word.lower()  # all input convert to lowercase
        checkWordList(word)
        searchWord(word)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('(*_*)Usage:{} [--options] [word1] [word2] ...'
              .format(sys.argv[0]))
        sys.exit()
    elif sys.argv[1] == '--count':
        countWords()
    else:
        words = sys.argv[1:]
        main()
