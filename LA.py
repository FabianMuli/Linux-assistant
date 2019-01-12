import os
import aiml


def main():
    if __name__ == '__main__':
        kernel = aiml.Kernel()

        if os.path.isfile("LABrain.brn"):
            kernel.bootstrap(brainFile="LABrain.brn")
    
        else:
            kernel.bootstrap(learnFiles="std.xml", commands="load aiml b")
            kernel.saveBrain("LABrain.brn")

        """def input_text():
            text = input("~> ")

            return text """

        while True:
            ai_speech = kernel.respond(text)

            print("Sarah: " + ai_speech)


main()
