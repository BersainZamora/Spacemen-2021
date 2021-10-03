# from _typeshed import Self
import tkinter as tk
import os
import random
from tkinter import *
from tkinter import font
from typing import Sized
 
os.system('cls')
print("Program Begins!")
 
root = tk.Tk()
 
#Theme
#Fit to Screen
 
root.attributes('-fullscreen', True)
 
#Classes
 
class card:
 
    def __init__(self,cad_num,sut,val):
        self.suit = sut
        self.card_num = cad_num
        self.value = val
    def get_val(self):
        return self.value
    def get_card_num(self):
        return self.card_num
    def get_suit(self):
        return self.suit 
    def set_val(self,val):
        self.value = val   
 
class deck:
    cards = []
    suits = [["heart"], ["diamond"], ["club"], ["spade"]]
    val = 0
    def __init__(self):
        for i in range(2,15):
            for k in self.suits:
                if i == 14:
                    self.cards.append(card(i,k,11))
                elif i >=10 and i != 14:
                    self.cards.append(card(i,k,10))
                else:
                    self.cards.append(card(i,k,i))
 
    def shuffle(self):
        cards = random.shuffle(self.cards)
    
    def get_cards(self):
        return self.cards
 
class hand:
    cardes = []
    def __init__(self, card1, card2):
        self.cardes.append(card1)
        self.cardes.append(card2)
    
    def get_tot_val(self):
        val = 0
        for i in range(len(self.cardes)):
            val = val + self.cardes[i].get_val()
        return val
 
    def setcds(self, card1, card2):
        self.cardes.pop(0)
        self.cardes.pop(0)
        self.add_card(card1)
        self.add_card(card2)
 
    def add_card(self, card):
        self.cardes.append(card)   
    def get_num_cards(self):
        return len(self.cardes)
    def get_card(self, pos):
        return self.cardes[pos]
    def set_card(self,card,pos):
        self.cardes[pos] = card
 
class hand2:
    cards = []
    def __init__(self, card1, card2):
        self.cards.append(card1)
        self.cards.append(card2)
    
    def get_tot_val(self):
        val = 0
        for i in range(len(self.cards)):
            new_card = self.cards[i]
            val = val + new_card.get_val()
        return val
 
    def setcds(self, card1, card2):
        self.cards.pop(0)
        self.cards.pop(0)
        self.add_card(card1)
        self.add_card(card2)
 
    def add_card(self,card):
        self.cards.append(card)   
    def get_num_cards(self):
        return len(self.cards)
    def get_card(self, pos):
        return self.cards[pos]
    def set_card(self,card,pos):
        self.cards[pos] = card
                                                                                                                                    #Images are hell
 
class application: 
 
    def __init__(self):
        #Main Menu
        Header = Label(root, text=("Spacemen"), font= ("Times New Roman", 45, "italic", ))
        Title = Label(root, text=("BlackJack"), font=("Times New Roman",95), relief="solid")
        StartButton = Button(root, text="Start", height=10, width=48, command= self.Start)
        ExitButton = Button(root, text=("Exit"), height=10, width=48, command=quit)
 
        #Deck Stuff 
        self.Hope = deck()
        self.dealer_hand = hand(card(1,"heart",1),card(1,"heart",1))
        self.player_hand = hand2(card(1,"heart",1),card(1,"heart",1))
        self.cards = []
        self.Gamescreen = tk
        self.lable2 = Label
        self.lable3 = Label
        self.lable_output = ""
        self.player_val = 0
 
        Header.pack()
        Title.pack()
        StartButton.pack()
        ExitButton.pack()
 
        Title.place(relx=(.39),rely=(.3), anchor="w")
        StartButton.place(relx=(.35), rely=(.75), anchor="s")
        ExitButton.place(relx=(.7), rely=(.75), anchor="s")
        
        #Event Handlers
        root.mainloop()
    #Functions
    def Start(self):
        
        # image1 = Image.open("Backofcards.png")
        # test = ImageTK.PhotoImage(image1)
        self.GameScreen = Toplevel(master= root)
 
        label1 = Label(self.GameScreen,text="test", height=10, width=48)
        label1.pack()
        self.GameScreen.attributes('-fullscreen', True)
        
        #Buttons
 
        Hit = Button(self.GameScreen, text="Hit",  height= 3, width= 24, command= self.hit)
        Stay = Button(self.GameScreen, text="Stay", height= 3, width= 24, command= self.stay)
        
        Hit.pack()
        Stay.pack()
 
        Hit.place(relx=(.825),rely=(.95),anchor='se')
        Stay.place(relx=(.95),rely=(.95),anchor='se')
 
        self.Hope.shuffle()
 
        self.cards = self.Hope.get_cards()
 
        self.dealer_hand.setcds(self.cards.pop(0), self.cards.pop(0))#fills dealers starting hand
        self.player_hand.setcds(self.cards.pop(0), self.cards.pop(0))#fills player hand
 
        self.lable_output = ""
        for i in range(self.player_hand.get_num_cards()):
            new_card1 = self.player_hand.get_card(i)
            self.lable_output = self.lable_output + str(new_card1.get_card_num()) + " of " + str(new_card1.get_suit()) + "\t"
            self.player_val = self.player_val + new_card1.get_val()
        # print(lable_output)
        self.lable2 = Label(self.GameScreen, text = self.lable_output)
        self.lable2.place(relx = .5, rely = .95, anchor="s")
        self.label3 = Label(self.GameScreen, text=str(self.player_val))
        self.label3.place(relx = .5, rely = .85, anchor="s")
        # print(self.player_hand.get_card(1).get_card_num(), "\n" , self.dealer_hand.get_card(1).get_card_num())
    #Hit Function
    def hit(self):
        self.player_hand.add_card(self.cards.pop(0))
        #add card to gui output
        player_hand_val = self.player_hand.get_tot_val()
        new_card2 = self.player_hand.get_card(self.player_hand.get_num_cards()-1)
        self.lable_output = self.lable_output + str(new_card2.get_card_num()) + " of " + str(new_card2.get_suit()) + "\t"
        self.lable2 = Label(self.GameScreen, text = self.lable_output)
        self.lable2.place(relx = .5, rely = .95, anchor="s")
        if player_hand_val > 21:
            for i in range(self.player_hand.get_num_cards()):
                new_card = self.player_hand.get_card(i)
                if new_card.get_card_num() == 14:
                    new_card = self.player_hand.get_card(i)
                    new_card.set_val(1)
                    self.player_hand.set_card(new_card,i)
 
        self.player_val = self.player_val + new_card2.get_val()
        self.label3 = Label(self.GameScreen, text=str(self.player_val))
        self.label3.place(relx = .5, rely = .85, anchor="s")
 
        player_hand_val = self.player_hand.get_tot_val()
        if player_hand_val > 21:
            #code for brining up the game over page
            win = tk.Toplevel()
            win.wm_title("Game Ended")
 
            l = tk.Label(win, text="You Lost!")
            l.grid(row=0, column=0)
 
            b = tk.Button(win, text="Okay", command=win.destroy )
            b.grid(row=1, column=0)
            self.Gamescreen.DISABLED
 
    #Stay Functionality
    def stay(self):
        dealer_hand_val = self.dealer_hand.get_tot_val()
        while dealer_hand_val < 17:
            if dealer_hand_val <17:
                self.dealer_hand.add_card(self.cards.pop(0))
                dealer_hand_val = self.dealer_hand.get_tot_val()
            if dealer_hand_val > 21:
                for i in range(self.dealer_hand.get_num_cards()):
                    if self.dealer_hand.get_card(i).get_card_num() == 14:
                        new_card = self.dealer_hand.get_card(i)
                        new_card.set_val(1)
                        self.dealer_hand.set_card(new_card,i)
                        dealer_hand_val = self.dealer_hand.get_tot_val()           
 
        player_hand_val = self.player_hand.get_tot_val()
        dealer_output = ""
 
        for i in range(self.dealer_hand.get_num_cards()):
            new_card3 = self.dealer_hand.get_card(i)
            dealer_output = dealer_output + str(new_card3.get_card_num()) + " of " + str(new_card3.get_suit())
 
        lable3 = Label(self.GameScreen, text= dealer_output)
        lable3.place(relx = .5, rely = .05, anchor="n")
        label4 = Label(self.GameScreen, text= str(self.dealer_hand.get_tot_val()))
        label4.place(relx = .5, rely= .15, anchor= "n")
 
        if dealer_hand_val > 21:
            #you win pop up code
            win = tk.Toplevel()
            win.wm_title("Game Ended")
 
            l = tk.Label(win, text="You Won!")
            l.grid(row=0, column=0)
 
            b = tk.Button(win, text="Okay", command=win.destroy )
            b.grid(row=1, column=0)
            self.Gamescreen.DISABLED
 
        if dealer_hand_val > player_hand_val or dealer_hand_val == player_hand_val:
            #code for brining up the game over page
            win = tk.Toplevel()
            win.wm_title("Game Ended")
 
            l = tk.Label(win, text="You Lost!")
            l.grid(row=0, column=0)
 
            b = tk.Button(win, text="Okay", command=win.destroy )
            b.grid(row=1, column=0)
            self.Gamescreen.DISABLED
        else: 
            #you win pop up code
            win = tk.Toplevel()
            win.wm_title("Game Ended")
 
            l = tk.Label(win, text="You Won!")
            l.grid(row=0, column=0)
 
            b = tk.Button(win, text="Okay", command=win.destroy )
            b.grid(row=1, column=0)
            self.Gamescreen.DISABLED
 
app = application()
 
 
