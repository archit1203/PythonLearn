"""
MADLIBS GENERATOR

# Template
# User Input
# Build the story
"""
import json
import os


class MadLibs:
    def __init__ (self,word_des,templ):
        self.templ=templ
        self.word_des=word_des

def get_words(word_descp):
    # word_descp=['Noun', 'Verb']
    print("Please provide following words")
    words=[]
    for desc in word_descp:
        user_input=input(desc+" ")
        words.append(user_input+" ")
    # print(words)
    return words

def build_story(template,words):
    # template = "I own a big {} , I like to {}"
    # words=get_words(['Noun','Verb'])
    story=template.format(*words)
    return story

def get_temp(name,path="templates"):
    fpath = os.path.join(".",path,name)
    # fpath="."+"\\"+path+"\\"+name
    print(os.path.exists(fpath))
    print(fpath)
    # with open(fpath , "r") as f:
    #     data=json.load(f)
    # print(data)

temp_name="aDayAtZoo.json"
get_temp(temp_name)

# template = "I own a big {} , I like to {}"
# words=get_words(['Noun','Verb'])
# story = build_story(template,words)
# print(story)