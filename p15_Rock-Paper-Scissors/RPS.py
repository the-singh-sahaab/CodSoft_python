from tkinter import *
from PIL import Image,ImageTk
import random

userscore=0
pcscore=0


### Functions of the game
def enter(event):
    rock.config(bg='black',fg='white')
def enter1(event):
    paper.config(bg='black',fg='white')
def enter2(event):
    scissor.config(bg='black',fg='white')
    
def leave(event):
    rock.config(bg='white',fg='black')
def leave1(event):
    paper.config(bg='white',fg='black')
def leave2(event):
    scissor.config(bg='white',fg='black')

def entergame(event):
    maingame()

#Maingame Function will bring a new window of GUI and will provide a platform to play RPS:
def maingame():
    global userscore,pcscore
    global nameinp
    global rock,paper,scissor
    root.geometry('650x450')
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()
    
    #score:
    L2=Label(text=f"{nameinp.get()} Score: {userscore}",bg='#4834DF',fg='#ffffff',borderwidth=5,relief=RAISED,font='Rockwell 13 bold',padx=4,pady=2)
    L2.grid(row=5,column=0,pady=15)
    L3=Label(text=f"PC Score: {pcscore}",bg='#4834DF',fg='white',borderwidth=5,relief=RAISED,font='Rockwell 13 bold',padx=4,pady=2)
    L3.grid(row=6,column=0,pady=15)

    

    #Click Function Main Logic:
    def click(event):
        global userscore,pcscore  #These variable will get or count the scores of user and pc
        global L1       #We are using L1 Label 
        global pcchose   #we are using old pcchose label
        L1.grid_forget()    #We are forgetting or removing old label so that new text can come properly
        pcchose.destroy()   #We are deleting or removing old one so that new can come properly
        
        val=event.widget.cget('text') # This command will take the text of button

        #PC Logic (Pc will choose something randomly)
        x=random.randint(0,2)
        l1=['Rock','Paper','Scissor']
        pc_opt=l1[x] #PC Option

        
        #PC OPT (what PC opted will be shown as a label by this command):
        pcchose=Label(text=f'PC Opted: {pc_opt}',font='lucida 15 bold',bg='black',fg='red')
        pcchose.grid(row=5,column=1,pady=15)

        
        #Actual Game Logic
        if val=='Rock' and pc_opt=='Paper': #val means what user chose and pc_opt means what pc chose or opted
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Rock' and pc_opt=='Scissor':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val=='Paper' and pc_opt=='Scissor':
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Paper' and pc_opt=='Rock':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val=='Scissor' and pc_opt=='Rock':
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Scissor' and pc_opt=='Paper':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val==pc_opt:
            L1=Label(text=f"It's A Tie",font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            pcscore+=1
        maingame()

        
    
    # (Layout of RPS Game)

    head=Label(text='Rock Paper Scissor',font='arial 35 bold',bg='black',fg='white')
    head.grid(columnspan=2,row=0,ipadx=70,padx=33,pady=10)
    playerone=Label(text=f'Player 1 : {nameinp.get()}',font='lucida 16')
    playerone.grid(row=1,column=0)
    playertwo=Label(text=f'Player 2 : Computer',font='lucida 16')
    playertwo.grid(row=1,column=1)
    
    #Player 1 Buttons
    rock=Button(text='Rock',font='comicsansms 14 bold',height=1,width=7)
    rock.grid(row=2,column=0,pady=15)
    rock.bind('<Enter>',enter)
    rock.bind('<Leave>',leave)
    rock.bind('<Button-1>',click)
    paper=Button(text='Paper',font='comicsansms 14 bold',height=1,width=7)
    paper.grid(row=3,column=0)
    paper.bind('<Enter>',enter1)
    paper.bind('<Leave>',leave1)
    paper.bind('<Button-1>',click)
    scissor=Button(text='Scissor',font='comicsansms 14 bold',height=1,width=7)
    scissor.grid(row=4,column=0,pady=15)
    scissor.bind('<Enter>',enter2)
    scissor.bind('<Leave>',leave2)
    scissor.bind('<Button-1>',click)

    #Player 2:Computer Buttons
    rock1=Button(text='Rock',font='comicsansms 14 bold',height=1,width=7)
    rock1.grid(row=2,column=1,pady=15)
    paper1=Button(text='Paper',font='comicsansms 14 bold',height=1,width=7)
    paper1.grid(row=3,column=1)
    scissor1=Button(text='Scissor',font='comicsansms 14 bold',height=1,width=7)
    scissor1.grid(row=4,column=1,pady=15)

    #Close
    btnclose=Button(text='Close Game',command=root.destroy,bg='green',font='arial 10 bold')
    btnclose.place(x=300,y=410)

''' GUI Program Starting '''

#if __name__=='__main__':
root=Tk()
root.title('Rock Paper Scissor')
root.wm_iconbitmap("try_project\CodSoft\p15_Rock-Paper-Scissors\game.ico")
#Geometry or dimensions of game window
root.geometry('650x450')
root.maxsize(650,450)
root.minsize(650,450)

#Defining some widgets to use them in diff functions
rock=Button()
paper=Button()
scissor=Button()

#Defining Label to use it later in the program
L1=Label()          #This Label will show the who won pc or user
pcchose=Label()     #This Label will show what pc opted or chose


#Frame for first window of game
f1=Frame(root)
img=Image.open('try_project\CodSoft\p15_Rock-Paper-Scissors\rps.png')
img=img.resize((650,450),Image.ANTIALIAS)
pic=ImageTk.PhotoImage(img)
Lab=Label(f1,image=pic)
Lab.pack()
f1.pack()

#Create some widgets and placed them above the image that's why used place geometry method
name=Label(root,text='Enter Your Name :',font='arial 15 bold')
name.place(x=262,y=20)
nameinp=StringVar() #This variable will store the name of user
inpname=Entry(root,textvar=nameinp,font='arial 10 bold')
inpname.bind('<Return>',entergame)  #We binded Return event with inpname entry widget i.e. if enter key is pressed then entergame function will be called
inpname.place(x=275,y=60)

sub=Button(root,text="Let's Play",font='lucida 10 bold',bg='black',fg='white',command=maingame)
sub.place(x=305,y=88)

root.mainloop()
