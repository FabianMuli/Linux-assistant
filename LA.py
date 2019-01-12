import os
import aiml


def main():
    if __name__ == '__main__':
        kernel = aiml.Kernel()

        if os.path.isfile("ai_brain.brn"):
            kernel.bootstrap(brainFile="ai_brain.brn")
        else:
            kernel.bootstrap(learnFiles="std.xml", commands="load aiml b")
            kernel.saveBrain("ai_brain.brn")

        def input_text():
            text = input("~> ")

            return text

        while True:
            text = input_text()

            if text == "save":
                kernel.saveBrain("ai_brain.brn")
                text = " "

            ai_speech = kernel.respond(text)

            print("Sarah: " + ai_speech)


main()
