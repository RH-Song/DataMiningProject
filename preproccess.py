#!/usr/bin/env python
# coding=utf-8

def readTrainFile(filename, userList):
    keywords = ('for','help')
    train = open(filename, 'r')
    for line in train:
        wordsInLine = line.strip().split(' ')
        for key in keywords:
            if key in wordsInLine:
                indexOfKey = wordsInLine.index(key)
                user = wordsInLine[indexOfKey + 1]
                indexOfbuy = wordsInLine.index('buy')
                item = wordsInLine[indexOfbuy + 2]
                userList.append((str(user), str(item)))

def printList(l):
    for i in l:
        print i

userList = []
# filenames
trainFile = "train0.txt"
readTrainFile(trainFile, userList)
printList(userList)
