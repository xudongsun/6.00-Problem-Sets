# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Xudong Sun
# Collaborators: NA
# Time: about 5:00

import feedparser
import string
import time
import threading
from project_util import translate_html
from tkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate = pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
        

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    # constructor function.no nore arguments to inherit from trigger
    def __init__(self, phrase):
        # change all imput phrase into the lower case
        self.phrase = phrase.lower()
     
    def is_phrase_in(self, text):
        # all punctuations that is going to be picked out from the text
        punc = string.punctuation
        t = text
        # check every punctuation and replace them with a space
        for char in punc:
            t = t.replace(char, ' ')
        # replace multiple spaces (punctuations) with one single space
        # add spaces to the beginning and the end of the phrase to make sure
        # each word is present in its entirety
        # also do the same to the text
        # in case that the phrase is at the beginning or the end of the text
        text_t = ' ' + ' '.join(t.split()) + ' '
        phrase_t = ' ' + self.phrase + ' ' 
        # check if the phrase is in the text
        if phrase_t in text_t.lower():
            return True
        else:
            return False
            
    
        

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    # overwrite the evaluate() method for TitleTrigger
    def evaluate(self, story):
        # get title from the story
        title = story.get_title()
        
        if self.is_phrase_in(title):
            return True
        else:
            return False

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    # evaluate method for DescriptionTrigger
    def evaluate(self, story):
        # get description with the get method
        desc = story.get_description()
        if self.is_phrase_in(desc):
            return True
        else:
            return False
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        # convert the string to datetime
        time = datetime.strptime(time,"%d %b %Y %H:%M:%S")
        # set the time in EST
        self.time = time.replace(tzinfo=pytz.timezone("EST"))



# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    # the evaluation method of BeforeTrigger    
    def evaluate(self, story):
        # get the time of the story
        time = story.get_pubdate()
        # trigger-time to be compared with
        trig_time = self.time
        # fire condition
        if time < trig_time:
            return True
        else:
            return False
        
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    # the same with BeforeTrigger    
    def evaluate(self, story):
        time = story.get_pubdate()
        trig_time = self.time
        if time > trig_time:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        # take a trigger as argument
        self.trigger = trigger
        
    def evaluate(self, story):
        # evaluate the trigger by its own evaluate method
        # return the opposite outcome
        if self.trigger.evaluate(story):
            return False
        else:
            return True
            
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        # take two trigger objects as argument
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        # evaluate the AndTrigger by trigger1 and trigger2
        if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True
        else:
            return False
        
        
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    # similar to AndTrigger
    def __init__(self, trigger1, trigger2):
        
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    # an empty list for stories that match the triggers
    story_tri = []
    # loop through all stories
    for story in stories:
        # for every story, check every trigger
        for trigger in triggerlist:
            if trigger.evaluate(story):
                story_tri.append(story)
                
    return story_tri



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    
    # helper function: map the name to the trigger
    def makeTrigger(name, args, dic):
        if name == 'DESCRIPTION':
            return DescriptionTrigger(args[0])
        if name == 'TITLE':
            return TitleTrigger(args[0])
            
        if name == 'BEFORE':
            return BeforeTrigger(args[0])
        if name == 'AFTER':
            return AfterTrigger(args[0])
            
        if name == 'AND':
            return AndTrigger(dic[args[0]], dic[args[1]])
            
        if name == 'OR':
            return OrTrigger(dic[args[0]], dic[args[1]])
        
        if name == 'NOT':
            return NotTrigger(dic[args[0]])
            
    
    # list of added triggers
    add_trig_l = []
    # a dictionary mapping trigger index to the trigger object
    d_trigger = {}
    
    # translate the line     
    for line in lines:
        word_l = line.split(',')
        # if the line does not start with ADD
        # make the trigger than add it into the dictionary
        if word_l[0] != 'ADD':
            d_trigger[word_l[0]] = makeTrigger(word_l[1], word_l[2:], d_trigger)
            
        # if it is an 'ADD' line
        # find the triggers with the indexes and put them into the add_trig_l
        elif word_l[0] == 'ADD':
            for word in word_l[1:]:
                add_trig_l.append(d_trigger[word])
     
    return add_trig_l

    
    # for now, print it so you see what it contains!

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('debate_triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

