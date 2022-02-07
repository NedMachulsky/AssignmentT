# from logging import root
import os
from cbor import cbor
from lxml import html, etree
from bs4 import BeautifulSoup

WEBPAGESPATH = os.path.join(os.getcwd(), "WEBPAGES_RAW")



def isCharAlnum(char):
        """
        This method is responsible for determining if a given character is alphanumeric. An alphanumeric character is any character
        that is either a-z,A-Z,0-9. The reason I do not use the built-in .isalnum() function is because it counts certain special characters
        as alphanumeric, which I would not consider correct for this project.
        """
        return 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122


def processSentence(sentence):
        """
        This method is responsible for extracting all of the words from a given sentence(string of words separated by spaces).
        I follow the conventions set in project1, and use non-alphnumeric characters as delimiters.
        """
        words = "".join([char if isCharAlnum(char) else " " for char in sentence]).split(" ")
        return words



if __name__ == "__main__":

    rootdir = os.getcwd()
    for file in os.listdir(WEBPAGESPATH):
        pageDirectory = os.path.join(WEBPAGESPATH, file)
        if os.path.isdir(pageDirectory):
            print(pageDirectory)
            for webpage in os.listdir(pageDirectory):
                #if file == '1':
                fullPath = os.path.join(pageDirectory, webpage)
                print("FILE PATH:", fullPath)
                f = open(fullPath, "rb")
                fileContent = f.read()
                soup = BeautifulSoup(fileContent, features="html.parser")
                # Eliminate html style
                for script in soup(["script", "style"]):
                    script.extract()
                text = soup.get_text() # get text
                words = []
                for sentence in text.splitlines():
                    newSentence = processSentence(sentence.strip())
                    for word in newSentence:
                        if word != "" and len(word) > 1:
                            words.append(word.lower())
                print("TEXT:", words)
