#!/usr/bin/env python
import aiml
import os
import sys

class LA():
    def __init__(self):
        self.kernel = aiml.Kernel()

    def initialize(self):
        if os.path.isfile("LABrain.brn"):
            self.kernel.bootstrap(brainFile="LABrain.brn")
    
        else:
            self.kernel.bootstrap(learnFiles="std.xml", commands="load aiml b")
            self.kernel.saveBrain("LABrain.brn")

        properties_file = open(os.sep.join(["LA/lib/system","rosie.properties"]))
        for line in properties_file:
            parts = line.split('=')
            key = parts[0]
            value = parts[1]
            self.kernel.setBotPredicate(key,value)

        while True:
            print(self.kernel.respond(raw_input("~> ")))


def main():
    la = LA()
    la.initialize()

if __name__ =='__main__':
    main()
        
