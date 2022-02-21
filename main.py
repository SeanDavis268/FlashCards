

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
            loadedSets = pickle.load(f)
            #print("unpickled", loadedSets)
            for set in loadedSets:  #this grabs the cardSet

                Button(root, text=set, bd=5, command= lambda set=set:self.openSet(set,loadedSets[set],root) ).pack(anchor=N,side=BOTTOM,expand=YES,fill=BOTH)


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

        #these are only temporary
        nestedDict = {"does this work?":"I hope so", "yeet":"endSet1"}
        setCollection = { "Set1":nestedDict, "Set2":{"sq1":"sa1"}     }

        with open('setCollectionFile', 'wb') as f:
            pickle.dump(setCollection, f, pickle.HIGHEST_PROTOCOL)
            print("pickling")

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
        newSetBTN = Button(win, text="create new set").pack(anchor=N,side=TOP,expand=YES,fill=X)


        self.populate(win)
        win.mainloop()

    def addCard(self):
        #needs to function both in card view and when creating new sets
        pass
    def subCard(self):
        #same as above needs to work in both card view and creating sets
        pass



if __name__ == "__main__":
    mainWindow()
