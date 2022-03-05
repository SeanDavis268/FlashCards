

from tkinter import *
import pickle

class mainWindow():
    def __init__(self):


        self.createMenu()



    #####
    def openSet(self,setName,setDict,root):
        """ when a set button is clicked this clears the screen and creates
            1. return arrow 2. title of set, 3. plus and minus to create and
            remove cards from the current set 4. a flip button 5. two arrows
            to navigate the current set."""
        ######################################
        self.setQuestions = list(setDict.keys())
        #print(self.setQuestions)
        #for each in self.setQuestions:
            #print(each) #this grabs the question
            #print(setDict[each]) #this grabs the answers from a set

        for widget in root.winfo_children(): #this clears the window
            widget.destroy()

        topFrame= Frame(root).grid()
        midFrame= Frame(root).grid()#frames seem useless with grid, will delete
        backBTN=Button(topFrame, text="Return",command= lambda:self.createMenu(root)).grid(column=0,row=0,ipadx=25) #return to start screen
        setTitle=Label(topFrame,text=setName,width=30).grid(column=1,row=0) #maybe add the card number/total here
        addBTN=Button(topFrame, text="+").grid(column=2,row=0) #add a card to the list
        subBTN=Button(topFrame, text="-").grid(column=3,row=0) #cause pop up asking if user is sure card should be deleted

        self.QAtext.set(self.setQuestions[0])
        self.QAlabel=Label(midFrame,text=self.QAtext.get(),width=40)
        self.QAlabel.grid(column=1,row=1,pady=30)

        flipBTN=Button(midFrame,text="FLIP",width=15,command= lambda:self.flipFN(setDict))
        flipBTN.grid(column=0,row=2)
        leftBTN=Button(midFrame,text="<-",command= lambda:self.decKey()).grid(column=2,row=2)
        rightBTN=Button(midFrame,text="->", command= lambda:self.incKey() ).grid(column=3,row=2)

        #here is where i left do the requirements for above ^
    ####




    def populate(self,root):
        """This method will get the sets from another file and is called on init.
            OpenSet needs to be here as it needs to be defined before use"""

        ##actual code
        with open('setCollectionFile', 'rb') as f:
            try:
            self.masterDict = pickle.load(f)
            #print("unpickled", loadedSets)
            for set in self.masterDict:  #this grabs the cardSet

                Button(root, text=set, bd=5, command= lambda set=set:self.openSet(set,self.masterDict[set],root) ).pack(anchor=N,side=BOTTOM,expand=YES,fill=BOTH)
            #except #TODO add catch for when the file is empty  

    def incKey(self):
        self.cardNumber+=1
        print("incrementing",self.cardNumber)
        self.setCard()

    def decKey(self):
        self.cardNumber-=1
        print("incrementing",self.cardNumber)
        self.setCard()
    def setCard(self):
        #gonna need protections against list out of bounds
        self.QAtext.set(self.setQuestions[self.cardNumber])
        self.QAlabel["text"]=self.QAtext.get()
        self.flipped=False
        print(self.QAtext.get())

    def flipFN(self,dict):
        """flips the card. ie replaces the text with either the answer or the
            question"""
        if self.flipped==False: #flip from question to answer
            self.flipped=True
            #self.QAtext.set(dict)
            self.QAtext.set(dict[self.setQuestions[self.cardNumber]])
            self.QAlabel["text"]=self.QAtext.get()
            print(dict[self.setQuestions[self.cardNumber]]) #set the card to the proper string
        else:
            self.flipped=False
            self.QAtext.set(self.setQuestions[self.cardNumber])
            self.QAlabel["text"]=self.QAtext.get()

    def createMenu(self,origin=False):
        #this will hold the info currently in the init
        self.cardNumber=0
        self.flipped=False

        self.workingTitle=""
        self.masterDict= {} #{ "Set1":{"s1q1":"s1a1"}, "Set2":{"s2q1":"s2a1"}     }

        if origin==False:
            win=Tk() ##upon initiation make the start screen
            win.geometry("500x500+300+300")
            win.update()
            win.title("Flash Cards")
        else:
            for widget in origin.winfo_children(): #this clears the window
                widget.destroy()
            win=origin
        #this stuff below should be in a mthod so it can be used later
        #NOTE also need anchored
        self.QAtext=StringVar(win,"oof")
        headerTxt = Label(win, text="Flash Cards").pack(side=TOP)
        newSetBTN = Button(win, text="create new set", command= lambda:self.createSet(win)).pack(anchor=N,side=TOP,expand=YES,fill=X)


        self.populate(win)
        win.mainloop()

    class addCard():

        def __init__(self,root,Q,A,dict):
            #then adds QA into a cardList for easy viewing
            self.dict=dict
            self.root=root
            self.question=Q
            self.answer=A
            self.newCardFrame=Frame(root, bg="white",bd=3)
            self.newCardCanvas=Canvas(self.newCardFrame, bg="lightblue")
            self.newCardText=Label(self.newCardCanvas,text="Question:"+Q, bg="lightblue",padx=10)
            self.newCardText.grid(column=0,row=0)
            self.newCardText=Label(self.newCardCanvas,text="Answer:"+A, bg="lightblue",padx=10)
            self.newCardText.grid(column=0,row=1)
            self.newCardViewBTN=Button(self.newCardCanvas,text="View")
            self.newCardViewBTN.grid(column=1,row=0)
            self.newCardDelBTN=Button(self.newCardCanvas,text="Del",command= lambda:self.killself())
            self.newCardDelBTN.grid(column=1,row=1)

            self.newCardCanvas.pack()
            self.newCardFrame.pack()
        def killself(self):
            #clear data and remove from list
            for each in self.newCardFrame.winfo_children():
                each.destroy()

            self.newCardFrame.pack_forget()
            del self.dict[self.question] #removes entry from dict




    def subCard(self):
        #same as above needs to work in both card view and creating sets
        pass

    def viewCard(self):
        pass

    def saveReturn(self,root):
        #saves the set and returns to the menu
        self.masterDict[self.workingTitle]=self.workingDict
        print(self.masterDict)
        with open('setCollectionFile', 'wb') as f:
            pickle.dump(self.masterDict, f, pickle.HIGHEST_PROTOCOL)
            print("pickling")

        self.createMenu(root)


    def createSet(self,root):

        self.workingQ=""
        self.workingA=""
        self.workingDict={}

        """clears screen and provides two entry boxes (question/answer) along with
           a button to add them to the set. Along with a button to return to menu """
        for widget in root.winfo_children(): #this clears the window
            widget.destroy()

        #now create the entry boxes with labels
        backBTN=Button(text="Return",command= lambda:self.createMenu(root)).grid(column=0,row=0,ipadx=25)

        if self.workingTitle=="":
            print("first phase")
            #if a title has not been made
            titleEntryLabel= Label(text="Enter Title of Set Here:")
            titleEntryLabel.grid(column=1,row=1)

            def getTitle():
                #check if empty or if just whiteSpace
                if titleEntry.get().strip()!="":
                    self.workingTitle=titleEntry.get().strip()
                    print(self.workingTitle)
                    self.createSet(root)

            titleEntry= Entry()
            titleEntry.grid(column=2,row=1)
            titleEntry.bind("<Return>",(lambda event: getTitle()))

            enterBTN=Button(text="Enter", command= getTitle) #will need command
            enterBTN.grid(column=3,row=1)

        else:
            #after the title has been chosen
            titleLabel= Label(text= "Set Title: "+ self.workingTitle)
            titleLabel.grid(column=1,row=1)
            Qlabel= Label(text="Question:")
            Qlabel.grid(column=0,row=3,ipady=20)
            Qinput= Entry()
            Qinput.grid(column=1,row=3)

            Alabel=Label(text="Answer:")
            Alabel.grid(column=2,row=3,ipady=20, ipadx=10)
            Ainput= Entry()
            Ainput.grid(column=3,row=3)

            #grab,record,pack
            def grabQA():
                 #enters QA into the workingDict
                 if Qinput.get().strip()!= "" and Ainput.get().strip():
                     questionStrip= Qinput.get().strip()
                     answerStrip=Ainput.get().strip()

                     if questionStrip not in self.workingDict:
                         self.workingDict[questionStrip]= answerStrip
                         self.addCard(cardSubFrame,questionStrip,answerStrip,self.workingDict)

                         cardSubFrame.update_idletasks()
                         cardCanvas.config(scrollregion=cardCanvas.bbox("all"))
                         print("valid", self.workingDict)
                         #now make new key/value card and add it to a scrollable view


            ############
            QAEnterBTN= Button(text="Enter", command=grabQA)
            QAEnterBTN.grid(column=3,row=4)
            QAEnterBTN.bind("<Return>",(lambda event: grabQA() ))


            cardFrame= Frame(root)
            cardFrame.grid(column=1,row=5,columnspan = 4,sticky="nw")
            cardFrame.grid_rowconfigure(0, weight=1)
            cardFrame.grid_columnconfigure(0, weight=1)

            cardCanvas=Canvas(cardFrame)
            cardCanvas.grid(column=0,row=0, sticky="nw")

            scroll= Scrollbar(cardFrame, orient="vertical", command=cardCanvas.yview)
            scroll.grid(column=0,row=1,stick="ns")
            cardCanvas.configure(yscrollcommand=scroll.set)

            saveBTN= Button(text="Save set \n and return", command=lambda:self.saveReturn(root))
            saveBTN.grid(column=3,row=5)

            cardSubFrame=Frame(cardFrame,bg="white")
            cardCanvas.create_window((0,0), window=cardSubFrame, anchor="nw")


            cardSubFrame.update_idletasks()
            cardFrame.config(width=200,height=200)
            cardCanvas.config(scrollregion=cardCanvas.bbox("all"))





if __name__ == "__main__":
    mainWindow()
