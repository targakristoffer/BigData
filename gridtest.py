try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

import os
import subprocess

from GUI.LeftTextView import LeftTextView
from GUI.RightTextView import RightTextView
from GUI.RightFrame import RightFrame
from GUI.MenuBar import MenuBar
from GUI.BasicButton import Button_run
from GUI.TweetButton import Button_tweet

from NLPHelper.Basic_NLP_Tasks import Basic_NLP_Tasks, POS_Retriever, NER_Retriever

from TwitterHelper.TwitterHelper import TwitterHelper

from LODHelper.connectHelper import ConnectHelper
from LODHelper.QueryAssistant import QueryAssistant

### ALL NAVIGATION BAR RELATED BEEZZWAX
##
#
class GUI(tk.Frame):

    lt = ''

    ## INIT MAIN FRAME FUNCTION
    #
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.ConnectHelper = ConnectHelper()
        self.TwitterHelper = TwitterHelper()
        self.parent = parent
        
        self['highlightthickness'] = 2
        self.parent['highlightthickness'] = 2
        self.parent['relief'] = 'groove'

        ### ALL NAVIGATION BAR RELATED BEEZZWAX
        ##
        #
        def hello():
            print('Hello')
        MenuBar(parent, hello)


        ### HEADER FRAME
        ## CONTAINS:
        #
        headerFrame = tk.Frame(parent)
        headerFrame['highlightthickness'] = 2
        headerFrame['relief'] = 'groove'
        totaltxt = ttk.Label(headerFrame, text="TEXT EXPLORER", font=("Times", 20))
        totaltxt.pack()
        headerFrame.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        

        ### TABS AND MAIN CONTENT
        ##
        #
        mainFrame = tk.Frame(parent)
        mainFrame.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)
        tabController = ttk.Notebook(mainFrame)

        rawTab = ttk.Frame(tabController)
        tabController.add(rawTab, text="Raw Text Tab")
  
        tweetTab = ttk.Frame(tabController)
        tabController.add(tweetTab, text="Get Tweets Tab")
        
        FacebookTab = ttk.Frame(tabController)
        tabController.add(FacebookTab, text="Facebook Tab")

        tabController.pack(expand=1, fill='both', padx=5, pady=5)



        ############################### EVERYTHING BELOW IS IN RAW TEXT TAB ###############################
        ### TREEVIEW
        ##
        #
        rawTreeTab = tk.Frame(rawTab)
        path = "C:/Users/Y/Desktop/ny_styr/skeptics-texts/skeptics-texts"
        self.nodes = dict()
        frame = tk.Frame(rawTreeTab)
        self.tree = ttk.Treeview(frame, height=7)

        ttk.Style().configure("Treeview", background="#383838", foreground="#FFF")

        ysb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text="SELECT FILE", anchor='center')

        self.tree.pack(fill='x')       
        frame.pack(fill='x')  


        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<Double-1>', self.OnDoubleClick)

        rawTreeTab['highlightthickness'] = 2
        rawTreeTab['relief'] = 'groove'
        rawTreeTab.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)



        rawLowerTab = tk.Frame(rawTab)
        ### LEFT VIEW
        ## 
        #
        lefttext = """
                LAST INN TEKSTER HER
        """
        self.rawleftscreen = self.initLeftTextView(rawLowerTab, lefttext, 20, 52)


        ### RUN-BUTTONS FRAME 
        ## 
        #
        buttonFrame = tk.Frame(rawLowerTab)

        self.POS = POS_Retriever()
        firstLabel = ttk.Label(buttonFrame, text="Finn POS", font=("Helvitca", 12))
        firstLabel.grid(row=0, column=0)
        def firstButton():
            result = self.POS.find_POS(self.rawleftscreen.getContent())
            print(result)
            self.loadRawTextRight(result)
        btn_one_row = 1
        btn_one_column = 0
        Button_run(buttonFrame, firstButton, btn_one_row, btn_one_column)


        self.NER = NER_Retriever()
        secondLabel = ttk.Label(buttonFrame, text="Finn NER", font=("Helvitca", 12))
        secondLabel.grid(row=2, column=0)
        def secondButton():
            content = self.rawleftscreen.getContent()
            result = self.NER.find_NER(content)
            self.loadRawTextRight(result)
        btn_two_row = 3
        btn_two_column = 0
        Button_run(buttonFrame, secondButton, btn_two_row, btn_two_column)


        thirdLabel = ttk.Label(buttonFrame, text="Finn Sentiment", font=("Helvitca", 12))
        thirdLabel.grid(row=4, column=0)
        def thirdButton():
            content = self.rawleftscreen.getContent()
            print(content)
            self.ConnectHelper.send_get_query()
            print('--'*15)
            self.ConnectHelper.send_ask_query()
            print('--'*15)
            self.ConnectHelper.send_desc_query()


        btn_three_row = 5
        btn_three_column = 0
        Button_run(buttonFrame, thirdButton, btn_three_row, btn_three_column)


        self.QueryAssistant = QueryAssistant()
        fourthLabel = ttk.Label(buttonFrame, text="Query", font=("Helvitca", 12))
        fourthLabel.grid(row=6, column=0)
        def fourthButton():
            content = self.rawleftscreen.getContent()
            print(content)
            primary_subj, other_subj = self.QueryAssistant.test(content)
            for thing in primary_subj:
                print("[+]---------- QUERY SESS STARTED ---------[+]")
                self.ConnectHelper.send_get_query(thing)
                print('--'*15)
                self.ConnectHelper.send_ask_query(thing)
                print('--'*15)
                self.ConnectHelper.send_desc_query(thing)

        btn_fourth_row = 7
        btn_fourth_column = 0
        Button_run(buttonFrame, fourthButton, btn_fourth_row, btn_fourth_column)

        buttonFrame.grid(row=1, column=1)




        ### RIGHT VIEW 
        ##  
        #
        righttext = """
                OUTPUT VISES HER
        """ 

        self.rawrightscreen = self.initRightTextView(rawLowerTab, righttext, 20, 52)

        rawLowerTab['highlightthickness'] = 2
        rawLowerTab['relief'] = 'groove'
        rawLowerTab.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

        ############################### EVERYTHING BELOW IS IN TWEET TAB ##################################
        ### TWEET TOP FRAME 
        ##  
        #
        tweetTopTab = tk.Frame(tweetTab)
        tweetTopTab['highlightthickness'] = 2
        tweetTopTab['relief'] = 'groove'

        tweetTopTab.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
       

        tweetInfoLabel = ttk.Label(tweetTopTab, text="Get Tweets", font=("Helvitca", 16))
        tweetInfoLabel.grid(row=0, column=0)

        keywordLabel = ttk.Label(tweetTopTab, text="Keyword:", font=("Helvitca", 12))
        keywordLabel.grid(row=1, column=0)
        keywordEntry = tk.Entry(tweetTopTab)
        keywordEntry.grid(row=2, column=0)

        amountLabel = ttk.Label(tweetTopTab, text="Amount:", font=("Helvitca", 12))
        amountLabel.grid(row=3, column=0)
        amountEntry = tk.Entry(tweetTopTab)
        amountEntry.grid(row=4, column=0)

        def getTweetButton():
            print('[+] Get tweet button working...')
            print('-----'*20)
            a = keywordEntry.get()
            self.TwitterHelper.get_tweet(a)


        btn_getTweet_row = 5
        btn_getTweet_column = 0
        Button_tweet(tweetTopTab, getTweetButton, btn_getTweet_row, btn_getTweet_column)





        tweetLowerTab = tk.Frame(tweetTab)
        tweetLowerTab['highlightthickness'] = 2
        tweetLowerTab['relief'] = 'groove'

        tweetLowerTab.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)
        ### TWEET LEFT TEXT VIEW
        ##  
        #
        self.tweetleftscreen = self.initLeftTextView(tweetLowerTab, lefttext, 21, 50)

        
        ### TWEET RUN-BUTTONS FRAME 
        ## 
        # 

        tweetButtonFrame = tk.Frame(tweetLowerTab)

        self.POS = POS_Retriever()
        tweetFirstLabel = ttk.Label(tweetButtonFrame, text="Finn POS", font=("Helvitca", 12))
        tweetFirstLabel.grid(row=0, column=0)
        def tweetFirstButton():
            content = self.tweetleftscreen.getContent()
            result = self.POS.find_POS(content)
            print(result)
            self.loadTweetTextRight(result)

        tweet_btn_one_row = 1
        tweet_btn_one_column = 0
        Button_run(tweetButtonFrame, tweetFirstButton, tweet_btn_one_row, tweet_btn_one_column)


        self.NER = NER_Retriever()
        tweetSecondLabel = ttk.Label(tweetButtonFrame, text="Finn NER", font=("Helvitca", 12))
        tweetSecondLabel.grid(row=2, column=0)
        def tweetSecondButton():
            content = self.tweetleftscreen.getContent()
            result = self.NER.find_NER(content)
            self.loadTweetTextRight(result)

        tweet_btn_two_row = 3
        tweet_btn_two_column = 0
        Button_run(tweetButtonFrame, tweetSecondButton, tweet_btn_two_row, tweet_btn_two_column)


        tweetThirdLabel = ttk.Label(tweetButtonFrame, text="Finn sentiment", font=("Helvitca", 12))
        tweetThirdLabel.grid(row=4, column=0)
        def tweetThirdButton():
            content = self.tweetleftscreen.getContent()
            print(content)
            
        tweet_btn_three_row = 5
        tweet_btn_three_column = 0
        Button_run(tweetButtonFrame, tweetThirdButton, tweet_btn_three_row, tweet_btn_three_column)


        tweetFourthLabel = ttk.Label(tweetButtonFrame, text="Query", font=("Helvitca", 12))
        tweetFourthLabel.grid(row=6, column=0)
        def tweetFourthButton():
            content = self.tweetleftscreen.getContent()
            print(content)

        tweet_btn_fourth_row = 7
        tweet_btn_fourth_column = 0
        Button_run(tweetButtonFrame, tweetFourthButton, tweet_btn_fourth_row, tweet_btn_fourth_column)

        tweetButtonFrame.grid(row=1, column=1)




        ### TWEET RIGHT VIEW 
        ## 
        #

        self.tweetrightscreen = self.initRightView(tweetLowerTab)
        


###################################################################################################################
###################################################################################################################
#################################################FUNCTIONS#########################################################
###################################################################################################################
###################################################################################################################


    ##
    #
    def initLeftTextView(self, parent, text, height, width):
        
        lt = LeftTextView(parent, height, width)
        lt.packself()
        lt.fill(text)

        return lt

    ##
    #
    def initRightTextView(self, parent, text, height, width):
        
        rt = RightTextView(parent, height, width)
        rt.packself()
        rt.fill(text)

        return rt
    
    def initRightView(self, parent):
        
        rt = RightFrame(parent)
        rt.packself()

        return rt

#########################################################################################################

    ##
    #
    def removeRawTextRight(self):
        self.rawrightscreen.remove()

    ##
    #
    def loadRawTextRight(self, text):
        self.removeRawTextRight()

        if(isinstance(text, dict)):
            for key, val in text.items():
                self.rawrightscreen.fill(key)
                if(len(val) >= 1):
                    self.rawrightscreen.fill('\n\n')
                    self.rawrightscreen.fill(val)
        elif(isinstance(text, list)):
            for a in text:
                self.rawrightscreen.fill(str(a))
        else:
            self.rawrightscreen.fill('[+] HOUSTON WE HAVE AN ERROR SOMEWHERE')


    ##
    #
    def removeRawTextLeft(self):
        self.rawleftscreen.remove()

    ##
    #
    def loadRawTextLeft(self, text):
        self.removeRawTextLeft()
        self.rawleftscreen.fill(text)

    #####################################################################################################

    ##
    #
    def removeTweetTextRight(self):
        self.tweetrightscreen.remove()

    ##
    #
    def loadTweetTextRight(self, text):
        self.removeTweetTextRight()

        if(isinstance(text, dict)):
            for key, val in text.items():
                self.tweetrightscreen.fill(key)
                if(len(val) >= 1):
                    self.tweetrightscreen.fill('\n\n')
                    self.tweetrightscreen.fill(val)
        elif(isinstance(text, list)):
            for a in text:
                self.tweetrightscreen.fill(str(a))
        else:
            self.tweetrightscreen.fill('[+] HOUSTON WE HAVE AN ERROR SOMEWHERE')


    ##
    #
    def removeTweetTextLeft(self):
        self.tweetleftscreen.remove()

    ##
    #
    def loadTweetTextLeft(self, text):
        self.removeTweetTextLeft()
        self.tweetleftscreen.fill(text)

    ###################################################################################################   

    ##
    #
    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')
    
    ##
    #           
    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))

    ##
    #
    def OnDoubleClick(self, event):
        click = self.tree.selection()[0]
        #print('----> ' + self.tree.item(click, 'text'))
        fileToOpen = self.tree.item(click, 'text')
        self.loadFile(fileToOpen)     

    ##
    #
    def loadFile(self, fileToOpen):
        folder = "C:/Users/Y/Desktop/ny_styr/skeptics-texts/skeptics-texts"
        openThus = folder + '/' + fileToOpen
        file = open(openThus, 'r')
        openFile = file.readline()
        self.loadRawTextLeft(openFile)




## MAIN LOOP
# - Starts the software
# - Initiates GUI parent
if __name__ == "__main__":
    root = tk.Tk()
    GUI(root).grid()
    root.mainloop()