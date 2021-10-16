from homework1_pxs288 import *
import random

# print(tokenize("'Medium-rare,' she said."))
# print(ngrams(3, ['a', 'b', 'c']))


m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
# print(m.prob((), "c"))
# print(m.prob((), "a"))
# print(m.prob((), "<END>"))
random.seed(1)
print(m.ngrams)
print([m.random_token(()) for i in range(25)])
# print(m.random_text(13))
print(m.perplexity("x y"))

m2 = NgramModel(2)
m2.update("a b c d")
m2.update("a b a b")
# print(m2.prob(("<START>",), 'a'))
# print(m2.prob(("b",),"c"))
# print(m2.prob(("a",),"x"))
random.seed(5)
# print([m2.random_token(('<START>',)) for i in range(6)])
# print([m2.random_token(('b',)) for i in range(6)])
# print(m2.random_text(15))
# print(m2.perplexity("a b"))

ng = create_ngram_model(3, 'frankenstein.txt')
print(ng.random_text(60))
