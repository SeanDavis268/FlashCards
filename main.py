

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
        win.title("Flash Cards")
        headerTxt = Label(win, text="Flash Cards").pack(side=TOP)
        newSetBTN = Button(win, text="create new set").pack(side=TOP,expand=YES,fill=X)
        self.populate(win)
        win.mainloop()




    def populate(self,root):
        """This method will get the sets from another file and is called on init.
            OpenSet needs to be here as it needs to be defined before use"""

        #####
        def openSet(self,set):
            """ when a set button is clicked this clears the screen and creates
                1. return arrow 2. title of set, 3. plus and minus to create and
                remove cards from the current set 4. a flip button 5. two arrows
                to navigate the current set."""
            ######################################
            print("opening set:", loadedSets[set])
            #here is where i left do the requirements for above ^
        ####

        ##actual code
        with open('setCollectionFile', 'rb') as f:
            loadedSets = pickle.load(f)
            #print("unpickled", loadedSets)
            for set in loadedSets:  #this grabs the cardSet

                Button(root, text=set, command= lambda set=set:openSet(self,set) ).pack(side=BOTTOM,expand=YES,fill=X)


if __name__ == "__main__":
    mainWindow()
