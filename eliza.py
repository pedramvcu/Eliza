
##  Pedram maleki   CMSC 416-Dr.McInnes
##  This program is called Eliza and is a recreation of the
##  famous rogerian pychotherapist eliza. In this program we
##  want to be able to have a conversation with the user and
##  try to make it feel real. This is type of therapy where the
##  therapist just asks questions and doesn't suggest solutions.

##  Feel free to talk to Eliza about anything!
##  You can say things like:
## "I am hungry" and eliza will answer "Why you are hungry?"
##  "I cannot finish my HW" and Eliza will answer "Have you done your best?" or "I'm sure you can, but why do you think that?"
##
##  To use, just start by saying your name is the format of "my name is <yourName>"
##  In order to exit, just type quit or bye

##  This code using regular expressions in order to disect the user
##  input and come up with answers. We first look for statements and
##  then look for keywords

#importing the needed libraries
import re
from time import sleep
import random

#This dictionary is used to change sentences from the
#response to a question.
opposites = {
    r"\bi\b": "you",
    r"\bme\b": "you",
    r"\bam\b": "are",
    r"\bmy\b": "your",
    r"\bwas\b": "were",
    r"\bi'd\b": "you would",
    r"\bI would\b": "you would",
    r"\bi've\b": "you have",
    r"\bI have\b": "you have",
    r"\bi'll\b": "you will",
    r"\bI will\b": "you will",
    r"\byou\b": "I",
    r"\bare\b": "am",
    r"\byou've\b": "I have",
    r"\byou have\b": "I have",
    r"\byou'll\b": "I will",
    r"\byou will\b": "I will",
    r"\byour\b": "my",
    r"\byours\b": "mine",
    }

#This dict has some response patters and some answers
#We look for these to come up with the proper response
answers = [
            ["[Cc]an you(.*)",
                    ["Maybe, but lets talk about you.","I'm just here to talk about you.","If I can, how would that make you feel?"]],
            ["[Ii] would like to(.*)",
                    ["Why is that?","When do you plan on doing that?"]],
            ["[Ii]s it(.*)",
                    ["What do you think?","Let's figure it out together. What do you say?"]],
            ["[Ii] don't know(.*)",
                    ["How does that make you feel?","You can figure it out, lets talk about something else."]],
            ["(.*)[Dd]o you(.*)",
                    ["Let's focus on you. What is on your mind now?","I just want to help you."]],
            ["[Ii] can[('t)(not)](.*)",
                    ["Have you done your best?","I'm sure you can, but why do you think that?"]],
            ["[Aa]re you(.*)",
                    ["What if I was %1","You want me to be %1?"]],
            ["(.*)[Ll]ove(.*)",
                    ["love is great. continue.","Love is strong feeling. Do you always feel that way?"]],
            ["[Yy]es",
                    ["Interesting. Tell me more","Great. Continue"]],
            ["[Nn]o",
                    ["Ok. Explain more please","Are you sure?"]],
            ["[Bb]ecause(.*)",
                    ["How did that happen?","Let's talk more about this. How do you figure that?"]],
            ["[Cc]an [Ii](.*)",
                    ["You sure can! Anything else?","If you think you can or you can't, either way, you are right. Tell me more"]]
            ]
#This list contains keywords to be spotted.
#At this point the program will only ask why
#you mentioned the keyword
wordSpot = ["pizza",
             "coke",
             "crave",
             "ice cream",
             "crazy",
             "crave",
             "sad",
             "depressed",
             "anxiety",
             "anxious",
             "happy",
             "angry",
             "hungry",
             "thirsty",
             "tired",
             "excited",
             "jumping",
             "grumpy",
             "grateful",
             "praying",
             "insane",
             "jealous",
             "sleepy",
             "hurt",
             "burger",
             "food",
             "water",
             "sorry",
             "conquer",
             "alcohol",
             "problem"
             ]


#This function will generate the answers to the
#responses recieved from the user
def answer(response):
    #this just holds a list of words that have been
    #modified
    words=[]

    #in this loop we go throught the dict of answers that are
    #already written out. If a match is found we return that answer
    for key, values in answers:
        #we look for a match and alse get rid of any . and !
        temp = re.match(key, response.rstrip(".!"))
        #if a match is found, we randomly pick a value and return it
        if temp:
            answerWords = random.choice(values)
            return answerWords


    #if no match was found in the prevous step, we enter this for loop
    #we will look throught the keywors in the wordspot list
    for keyword in wordSpot:
        #using the search function to look for a match
        result = re.search(keyword, response)
        if result:
            #once a match is found, we break the entire user response into
            #a list of words and transform all the 'I's or 'am' or 'you's etc.
            #to the appropriate opposite
            words = response.lower().split()
            #loop throught the words in the responce
            for i, j in enumerate(words):
                #we loop through all the items in the opposite dict and
                #check them against the words in response
                for we, you in opposites.items():
                    #looking for a mactch
                    result1 = re.search(we,j)
                    #if a match is found, we change the word
                    if result1:
                        result2 = re.sub(we,you, j)
                        words[i] = result2

    #if the first for loop didn't return anything and the second for loop
    #did't find a match, words will be empty whcih means no answer is
    #found. We ask user to try again
    if len(words) == 0:
        return "I'm not sure I understand. Can you explain some more?"
    #if words have been changed, we reconstruct the list of words into a string
    #and add a why and a ? to it and return as answer
    else:
        result3 = " ".join(words)
        result3 = "Why " +result3 +"?"
        return result3




#This is the eliza method which will be getting info from the user and passing it to the answer
#methos
def eliza(elizaName, userName):
    displayName="["+userName+"] "
    print(elizaName + "Hi " + userName + "." + " How can I help you today?")
    #we continue the conversaion untill user enters quit or bye
    while True:

        print(displayName, end='')
        patientResponse=input()
        #re.match()
        if(patientResponse.lower()=="quit" or patientResponse.lower()=="bye"):
            print(elizaName + "Goodbye!")
            break
        elizaResponse=answer(patientResponse)
        print(elizaName + elizaResponse)





def main():

    elizaName="[Eliza] "
    #boolean to make sure I get the name
    goodname=True
    userName=""
    print(elizaName+"Hi, I'm a psychotherapist. What is your name? (To exit, enter quit or bye)")
    userName=input()

    if(userName.lower()=="quit" or userName.lower()=="bye"):
        exit(0)


    #This regex look for the name. I check for a greeting as well if
    #it was entered. So "Hi, my name is or just my name is will both work
    userInput = re.search(r'[\w]*my name is ([\w\s]*)', userName, re.IGNORECASE)

    #The name need to be in the format of my name is so in this block
    #I check for the format and ask the user to enter it properly
    #a greeting before 'my name is' is acceptable
    if userInput:
        goodname=False

    else:
        #while loop runs until the name is entered properly
        while (goodname):
            print(elizaName+"Please enter your name is the following format: ")
            print(elizaName+"my name is 'your name' (you can also say hello!) ")
            userName = input()
            if (userName.lower() == "quit" or userName.lower() == "bye"):
                exit(0)

            # This regex look for the name. We check for a greeting as well if
            # it was entered. So "Hi, my name is or just my name is will both work
            userInput = re.search(r'[\w]*my name is ([\w\s]*)', userName, re.IGNORECASE)

            if userInput:
                goodname=False
            else:
                goodname=True

    # group 1 is where the name is stored and we extract it
    userName = userInput.group(1)

    # just checking for he who must not be named!!!
    theOneWeDontName = userName
    if (theOneWeDontName.lower() == "voldomort" or theOneWeDontName == "lord voldomort"):
        print("He"), sleep(2), print("who"), sleep(2), print("Must Not Be Named"), sleep(2), print()

    # passing names to the eliza method for the rest of the conversation
    eliza(elizaName, userName)


#just main
if __name__ == '__main__':
    main()