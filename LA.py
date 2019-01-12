#!/usr/bin/env python
import aiml
import os
import sys


def main():
    if __name__ == '__main__':
        kernel = aiml.Kernel()

        if os.path.isfile("LABrain.brn"):
            kernel.bootstrap(brainFile="LABrain.brn")
    
        else:
            kernel.bootstrap(learnFiles="std.xml", commands="load aiml b")
            kernel.saveBrain("LABrain.brn")

        while True:
           print(kernel.respond(raw_input("~> ")))


main()
