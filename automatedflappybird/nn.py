import numpy as np
import random

class Network():

     def __init__(self, weights=None):
         self.inner = 2
         self.hidden = 2
         self.outer = 1
         if not weights:
            self.weights = [np.random.randn(x,y) for x, y in zip([self.inner,self.hidden], [self.hidden, self.outer])]
         else: self.weights = weights


     def feedforward(self, a):
         for w in self.weights:
             a = sigmoid(np.dot(a,w))
         return a


def sigmoid(n):
    return 1 / (1 + np.exp(-n))

nn = Network()
n1 = Network()


