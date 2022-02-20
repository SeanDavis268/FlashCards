

from tkinter import *
import pickle

class mainWindow():
    def __init__(self):
        nestedDict = {"does this work?":"I hope so", "yeet":"endSet1"}
        setCollection = { "Set1":nestedDict, "Set2":"A2"     }

        with open('setCollectionFile', 'wb') as f:
            pickle.dump(setCollection, f, pickle.HIGHEST_PROTOCOL)
            print("pickling")

        win=Tk() ##upon initiation make the start screen
        win.geometry("500x500+300+300")
        win.update()
        win.title("Flash Cards")

        #this stuff below should be in a mthod so it can be used later
        #NOTE also need anchored
        headerTxt = Label(win, text="Flash Cards").pack(side=TOP)
        newSetBTN = Button(win, text="create new set").pack(anchor=N,side=TOP,expand=YES,fill=X)
        self.populate(win)
        win.mainloop()



    #####
    def openSet(self,setName,setDict,root):
        """ when a set button is clicked this clears the screen and creates
            1. return arrow 2. title of set, 3. plus and minus to create and
            remove cards from the current set 4. a flip button 5. two arrows
            to navigate the current set."""
        ######################################

        for each in setDict:
            print(setDict)
            print(setDict[each]) #this grabs the answers from a set

        for widget in root.winfo_children(): #this clears the window
            widget.destroy()

        backBTN=Button(root, text="Return").pack(anchor=NW,side=LEFT,expand=YES,ipadx=25)
        setTitle=Label(root,text=setName,width=50).pack(anchor=NW,side=LEFT,expand=YES,fill=X)
        addBTN=Button(root, text="+").pack(anchor=NW,side=LEFT,expand=YES,ipadx=15)
        subBTN=Button(root, text="-").pack(anchor=NW,side=LEFT,expand=YES,ipadx=15)

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


if __name__ == "__main__":
    mainWindow()
