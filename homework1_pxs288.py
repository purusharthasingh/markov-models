############################################################
# CSE 597: Homework 1
############################################################

student_name = "Purushartha Singh"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
import random
import math

############################################################
# Section 1: Markov Models
############################################################


def tokenize(text):
    output = ""
    for char in text:
        if char in string.punctuation:
            output = output + " " + char + " "
        else:
            output += char
    return output.split()


def ngrams(n, tokens):
    start = ['<START>' for i in range(n-1)]
    words = start + tokens + ['<END>']
    output = []
    # print(words)
    for i in range(n-1,len(words)):
        tup = tuple(words[i-(n-1):i])
        output.append((tup,words[i]))
        # print (words[i])
    return output


class NgramModel(object):

    def __init__(self, n):
        self.order = n
        self.ngrams = {}

    def update(self, sentence):
        tokens = tokenize(sentence)
        ng_list = ngrams(self.order, tokens)
        # print(ng_list)
        for context, word in ng_list:
            if context in self.ngrams.keys():
                self.ngrams[context].append(word)
            else:
                self.ngrams[context] = [word]
        # print(self.ngrams)

    def prob(self, context, token):
        if context not in self.ngrams.keys():
            return 0
        token_count = self.ngrams[context].count(token)
        return token_count/len(self.ngrams[context])

    def random_token(self, context):
        r = random.random()
        p = 0
        tokens = self.ngrams[context]

        for token in sorted(set(tokens)):
            token_p = self.prob(context, token)
            if p <= r < p + token_p:
                return token
            else:
                p += token_p

    def random_text(self, token_count):
        context = tuple(['<START>' for i in range(self.order-1)])
        text = []

        for i in range(token_count):
            token = self.random_token(context)
            text.append(token)

            if self.order == 1:
                continue

            if token == '<END>':
                context = tuple(['<START>' for i in range(self.order-1)])
            else:
                context = tuple(list(context)[1:]+[token])
        return " ".join(text)

    def perplexity(self, sentence):
        tokens = tokenize(sentence)
        sen_ngrams = ngrams(self.order, tokens)

        sum = 0
        for con, token in sen_ngrams:
            tmp = self.prob(con, token)
            try:
                sum += math.log(tmp)
            except:
                sum += 0

        per = -sum/len(sen_ngrams)
        return math.exp(per)


def create_ngram_model(n, path):
    model = NgramModel(n)

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            model.update(line)

    return model

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
About 4-5 hours
"""

feedback_question_2 = """
Figuring out dealing with edge cases that exist for n=1, and for unexpected input
"""

feedback_question_3 = """
I liked trying to change something theoretical to something concrete. 
It would be nice if the description was specific in terms of handling test cases and using smoothing.
"""
