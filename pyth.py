#python mini project
from tkinter import *
from tkinter import simpledialog
#import numpy as np
welcome = Tk(className='welcome-New Match')
welcome.configure(background='lightgreen')
RWidth=welcome.winfo_screenwidth()
RHeight=welcome.winfo_screenheight()
welcome.geometry(("%dx%d")%(RWidth,RHeight))
s2= Tk(className='LIVE')
s2.configure(background='#EECFA1')
scorecard= Tk(className='SCORECARD')
scorecard.configure(background='grey')
batsman11=[[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]
batsman11name=[['','','','','','','','','','',''],['','','','','','','','','','','']]
bowler11=[[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]
bowler11name=[['','','','','','','','','','',''],['','','','','','','','','','','']]
tm1=''
tm2=''
twb=''
opt=''
now=''
inning=0
TotalRuns=[0,0]
TotalWickets=[0,0]
totalOvers=0.0
oversBowled=0.0
batsman1='player1'
batsman2='player2'
bowler1=''
to=['','','','','','','','','','','','']
bat1=[0,0,0,0,0]
bat2=[0,0,0,0,0]
bowl1=[0.0,0,0,0,0.0]
ballcount=0
legalballcount=0
strike=1
ballsleft=0
target=0
def changestrike():
    global strike
    if strike==1:
        strike=2
    else:
        strike=1
def batsmanstats():
    global s2,to,ballcount,bat1,bat2,bowl1,strike
    if strike==1:
        Label(s2,text=bat1[0],fg='#008080',bg='#EECFA1').grid(row=4,column=1)
        Label(s2,text=bat1[1],fg='#008080',bg='#EECFA1').grid(row=4,column=2)
        Label(s2,text=bat1[2],fg='#008080',bg='#EECFA1').grid(row=4,column=3)
        Label(s2,text=bat1[3],fg='#008080',bg='#EECFA1').grid(row=4,column=4)
        Label(s2,text=('%.1f'%(bat1[4])),fg='#008080',bg='#EECFA1',width=6,anchor=W,justify=LEFT).grid(row=4,column=5)
    else:
        Label(s2,text=bat2[0],fg='#008080',bg='#EECFA1').grid(row=5,column=1)
        Label(s2,text=bat2[1],fg='#008080',bg='#EECFA1').grid(row=5,column=2)
        Label(s2,text=bat2[2],fg='#008080',bg='#EECFA1').grid(row=5,column=3)
        Label(s2,text=bat2[3],fg='#008080',bg='#EECFA1').grid(row=5,column=4)
        Label(s2,text=('%.1f'%(bat2[4])),fg='#008080',bg='#EECFA1',width=6,anchor=W,justify=LEFT).grid(row=5,column=5)
def bowlerstats():
    global s2,bowl1
    Label(s2,text=bowl1[0],fg='#008080',bg='#EECFA1').grid(row=7,column=1)
    Label(s2,text=bowl1[1],fg='#008080',bg='#EECFA1').grid(row=7,column=2)
    Label(s2,text=bowl1[2],fg='#008080',bg='#EECFA1').grid(row=7,column=3)
    Label(s2,text=bowl1[3],fg='#008080',bg='#EECFA1').grid(row=7,column=4)
    Label(s2,text=('%.1f'%(bowl1[4])),fg='#008080',bg='#EECFA1',anchor=W,justify=LEFT).grid(row=7,column=5)
def click0():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+0
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+0
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+0
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+0
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+0
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+0
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=0
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        if checkmaiden():
            bowl1[1]=bowl1[1]+1
            bowlerstats()
        changestrike()
        changeover()    
def click1():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+1
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+1
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+1
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    changestrike()    
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+1
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+1
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+1
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=1
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()
def click1D():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+1
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+1
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+1
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+1
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+1
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+1
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=1
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()        
def click2():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+2
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+2
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+2
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+2
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+2
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+2
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=2
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()
def click3():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+3
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+3
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+3
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    changestrike()    
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+3
    bowl1[4]=bowl1[2]/(bowl1[0]*1.655)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+3
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+3
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=3
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()        
def click4():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+4
        bat1[2]=bat1[2]+1
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+4
        bat2[2]=bat2[2]+1
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+4
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][2]=batsman11[inning][i][2]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100       
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+4
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+4
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+4
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=4
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()
def click5():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+5
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+5
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+5
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    
    
    changestrike()    
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+5
    bowl1[4]=bowl1[2]/(bowl1[0]*1.655)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+5
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+5
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=5
    
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()        
def click6():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+6
        bat1[3]=bat1[3]+1
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+6
        bat2[3]=bat2[3]+1
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+6
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][3]=batsman11[inning][i][3]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+6
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+6
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+6
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]=6
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()
def wide():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    ballcount=ballcount+1
    bowl1[2]=bowl1[2]+1
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][2]=bowler11[inning][i][2]+1
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+1
    
    totalScore()          
    to[ballcount-1]='WD'
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()        
        
        

        
def changeover():
    global s2,bowler1,to,TotalRuns,inning,totalOvers,oversBowled,bowl1,ballsleft,target,now
    i=(int)(checkbowler())
    if bowler11[inning][i][0]==0.6:
        bowler11[inning][i][0]=1
    else:
        bowler11[inning][i][0]=bowler11[inning][i][0]+0.4
    if oversBowled==0.6:
        oversBowled=1
    else:
        oversBowled=oversBowled+0.4
    askNextBowlerName()    
    Label(s2, text=bowler1,fg='green',width=20,bg='#EECFA1').grid(row=7,column=0)
    to=['','','','','','','','','','','','']
    bowl1=[0.0,0,0,0,0.0]
    
    if oversBowled==now:
        target=TotalRuns[inning]+1
        inning=1
        ballsleft=6*totalOvers
        changeinning()
def lb():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+0
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+0
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    changestrike()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+0
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+0
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+0
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+1
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]='LB1'
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()        
def nb():
    global s2,to,ballcount,bat1,bat2,bowl1,strike,TotalRuns,inning,totalOvers,oversBowled,legalballcount
    if strike==1:
        bat1[0]=bat1[0]+1
        bat1[1]=bat1[1]+1
        bat1[4]=(bat1[0]/bat1[1])*100
        
    else:
        bat2[0]=bat2[0]+1
        bat2[1]=bat2[1]+1
        bat2[4]=(bat2[0]/bat2[1])*100
    batsmanstats()
    changestrike()
    i=(int)(checkbatsman())
    batsman11[inning][i][0]=batsman11[inning][i][0]+1
    batsman11[inning][i][1]=batsman11[inning][i][1]+1
    batsman11[inning][i][4]=(batsman11[inning][i][0]/batsman11[inning][i][1])*100
    ballcount=ballcount+1
    bowl1[2]=bowl1[2]+2
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    i=(int)(checkbowler())
    bowler11[inning][i][2]=bowler11[inning][i][2]+2
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    TotalRuns[inning]=TotalRuns[inning]+2
    totalScore()          
    to[ballcount-1]='NB1'
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        #if checkmaiden():
         #   bowl1[1]=bowl1[1]+1
        #    bowlerstats()
        changestrike()
        changeover()    
    
def checkmaiden():
    global s2,to,legalballcount
    for legalballcount in range (0,12):
       if to[legalballcount]==0:
           flag=1
       else:
           flag=0
    return flag       

    
def askBatsman1Name():
    global s2,batsman1,batsman11name
    batsman1 = simpledialog.askstring("Input", "Enter name of the batsman1:",
                                parent=s2)
    batsman11name[inning][0]=batsman1
    
def askBatsman2Name():
    global s2,batsman2,batsman11name
    batsman2 = simpledialog.askstring("Input", "Enter name of the batsman2:",
                                parent=s2)
    batsman11name[inning][1]=batsman2
def askNextBatsmanName():
    global s2,batsman2,batsman1,batsman11name,inning,TotalWickets,bat2,bat1
    newbatsman = simpledialog.askstring("Input", "Enter name of the next batsman:",
                                parent=s2)
    if strike==1:
        batsman1=newbatsman
        bat1=[0,0,0,0,0]
        Label(s2, text=batsman1,fg='green',bg='#EECFA1').grid(row=4,column=0)
    else:
        batsman2=newbatsman
        bat2=[0,0,0,0,0]
        Label(s2, text=batsman2,fg='green',bg='#EECFA1').grid(row=5,column=0)
    i=TotalWickets[inning]+2
    batsman11name[inning][i]=newbatsman    
def askBowler1Name():
    global s2,bowler1,bowler11name,inning
    bowler1 = simpledialog.askstring("Input", "Enter name of the first bowler:",
                                parent=s2)
    bowler11name[inning][0]=bowler1
def askNextBowlerName():
    global s2,bowler1,bowler11name,inning
    i=0
    bowler1 = simpledialog.askstring("Input", "Enter name of the next bowler:",
                                parent=s2)
    bowler11name[inning][i+1]=bowler1
def checkbowler():
    global bowler1,bowler11name,inning
    for i in range(0,11):
        if bowler1==bowler11name[inning][i]:
            return (int)(i)
def checkbatsman():
    global batsman2,batsman1,batsman11name,inning,TotalWickets
    for i in range(0,11):
        if strike==1:
            if batsman1==batsman11name[inning][i]:
                return (int)(i)
        else:
            if batsman2==batsman11name[inning][i]:
                return (int)(i)
def wicket():
    global batsman2,batsman1,batsman11name,inning,TotalWickets,legalballcount,ballcount,oversBowled
    TotalWickets[inning]=TotalWickets[inning]+1
    batsmanstats()
    bowl1[3]=bowl1[3]+1
    
    i=checkbowler()
    
    ballcount=ballcount+1
    legalballcount=legalballcount+1
    bowl1[0]=(ballcount)/10
    bowl1[2]=bowl1[2]+0
    bowl1[4]=bowl1[2]/(bowl1[0]*1.65)
    bowlerstats()
    bowler11[inning][i][3]=bowler11[inning][i][3]+1
    bowler11[inning][i][0]=bowler11[inning][i][0]+((legalballcount)/10)
    bowler11[inning][i][2]=bowler11[inning][i][2]+0
    bowler11[inning][i][4]=bowler11[inning][i][2]/(bowler11[inning][i][0]*1.65)
    oversBowled=oversBowled+0.1
    totalScore()          
    to[ballcount-1]='W'
    if legalballcount==6:
        ballcount=0
        legalballcount=0
        if checkmaiden():
            bowl1[1]=bowl1[1]+1
            bowlerstats()
        changestrike()
        changeover()
    askNextBatsmanName()
def sc():
    global scorecard,batsman11,batsman11name,inning,bowler11,bowaler11name
    buttoninning1 = Button(scorecard, text = 'INNING 1', fg ='white',bg='#BF3EFF',width=30,command=sc).grid(row=1,column=0)
    button4inning2 = Button(scorecard, text = 'INNING 2', fg ='white',bg='#00EEEE',width=30,command=inning2).grid(row=1,column=1)
    Label(scorecard, text='BATSMAN:',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=0)
    Label(scorecard, text='RUNS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=1)
    Label(scorecard, text='BALLS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=2)
    Label(scorecard, text='FOURS',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=3)
    Label(scorecard, text='SIXES',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=4)
    Label(scorecard, text='SR.',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=5)
    row=4
    for i in range(0,11):
        Label(scorecard, text=batsman11name[0][i],fg='green',width=20).grid(row=row,column=0)
        Label(scorecard, text=batsman11[0][i][0],fg='black',width=20).grid(row=row,column=1)
        Label(scorecard, text=batsman11[0][i][1],fg='black',width=20).grid(row=row,column=2)
        Label(scorecard, text=batsman11[0][i][2],fg='black',width=20).grid(row=row,column=3)
        Label(scorecard, text=batsman11[0][i][3],fg='black',width=20).grid(row=row,column=4)
        Label(scorecard, text=('%.1f'%(batsman11[0][i][4])),fg='black',width=20,anchor=W,justify=LEFT).grid(row=row,column=5)
        row=row+1
    Label(scorecard,text='BOWLER:',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=0)
    Label(scorecard, text='OVERS',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=1)
    Label(scorecard, text='MAIDEN',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=2)
    Label(scorecard, text='RUNS',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=3)
    Label(scorecard, text='WICKETS',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=4)
    Label(scorecard, text='ER.',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=5)
    row=17
    for i in range(0,11):
        Label(scorecard, text=bowler11name[0][i],fg='green',width=20).grid(row=row,column=0)
        Label(scorecard, text=('%.1f'%(bowler11[0][i][0])),fg='black',width=20).grid(row=row,column=1)
        Label(scorecard, text=bowler11[0][i][1],fg='black',width=20).grid(row=row,column=2)
        Label(scorecard, text=bowler11[0][i][2],fg='black',width=20).grid(row=row,column=3)
        Label(scorecard, text=bowler11[0][i][3],fg='black',width=20).grid(row=row,column=4)
        Label(scorecard, text=('%.1f'%(bowler11[0][i][4])),fg='black',width=20,anchor=W,justify=LEFT).grid(row=row,column=5)
        row=row+1
def inning2():
    global scorecard,batsman11,batsman11name,inning,bowler11,bowaler11name
    
    
    buttoninning1 = Button(scorecard, text = 'INNING 1', fg ='white',bg='#BF3EFF',width=30,command=scorecard).grid(row=1,column=0)
    button4inning2 = Button(scorecard, text = 'INNING 2', fg ='white',bg='#00EEEE',width=30,command=inning2).grid(row=1,column=1)
    Label(scorecard, text='BATSMAN:',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=0)
    Label(scorecard, text='RUNS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=1)
    Label(scorecard, text='BALLS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=2)
    Label(scorecard, text='FOURS',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=3)
    Label(scorecard, text='SIXES',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=4)
    Label(scorecard, text='SR.',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=5)
    row=4
    for i in range(0,11):
        Label(scorecard, text=batsman11name[1][i],fg='green',width=20).grid(row=row,column=0)
        Label(scorecard, text=batsman11[1][i][0],fg='black',width=20).grid(row=row,column=1)
        Label(scorecard, text=batsman11[1][i][1],fg='black',width=20).grid(row=row,column=2)
        Label(scorecard, text=batsman11[1][i][2],fg='black',width=20).grid(row=row,column=3)
        Label(scorecard, text=batsman11[1][i][3],fg='black',width=20).grid(row=row,column=4)
        Label(scorecard, text=('%.1f'%(batsman11[1][i][4])),fg='black',width=20,anchor=W,justify=LEFT).grid(row=row,column=5)
        row=row+1
    Label(scorecard,text='BOWLER:',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=0)
    Label(scorecard, text='OVERS',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=1)
    Label(scorecard, text='MAIDEN',fg='black',bg='#ADFF2F',width=20).grid(row=16,column=2)
    Label(scorecard, text='RUNS',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=3)
    Label(scorecard, text='WICKETS',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=4)
    Label(scorecard, text='ER.',fg='black',width=20,bg='#ADFF2F').grid(row=16,column=5)
    row=17
    for i in range(0,11):
        Label(scorecard, text=bowler11name[1][i],fg='green',width=20).grid(row=row,column=0)
        Label(scorecard, text=('%.1f'%(bowler11[1][i][0])),fg='black',width=20).grid(row=row,column=1)
        Label(scorecard, text=bowler11[1][i][1],fg='black',width=20).grid(row=row,column=2)
        Label(scorecard, text=bowler11[1][i][2],fg='black',width=20).grid(row=row,column=3)
        Label(scorecard, text=bowler11[1][i][3],fg='black',width=20).grid(row=row,column=4)
        Label(scorecard, text=('%.1f'%(bowler11[1][i][4])),fg='black',width=20,anchor=W,justify=LEFT).grid(row=row,column=5)
        row=row+1
def changeinning():
    global TotalRuns,TotalWickets,totalOvers,oversBowled,batsman1,batsman2,bowler1,to,bat1,bat2,bowl1,ballcount,legalballcount,strike
    
    totalOvers=0.0
    oversBowled=0.0
    batsman1='player1'
    batsman2='player2'
    bowler1=''
    to=['','','','','','','','','','','','']
    bat1=[0,0,0,0,0]
    bat2=[0,0,0,0,0]
    bowl1=[0.0,0,0,0,0]
    ballcount=0
    legalballcount=0
    strike=1
    secondscreen()
    
def batsman():
    global s2,batsman1,batsman2
    Label(s2, text='BATSMAN:',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=0)
    Label(s2, text='RUNS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=1)
    Label(s2, text='BALLS',fg='black',bg='#6C7B8B',width=20).grid(row=3,column=2)
    Label(s2, text='FOURS',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=3)
    Label(s2, text='SIXES',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=4)
    Label(s2, text='SR.',fg='black',width=20,bg='#6C7B8B').grid(row=3,column=5)
    askBatsman1Name()
    askBatsman2Name()
    Label(s2, text=batsman1,fg='green',bg='#EECFA1').grid(row=4,column=0)
    Label(s2, text=batsman2,fg='green',bg='#EECFA1').grid(row=5,column=0)
def bowler():
    global s2,bowler
    Label(s2,text='BOWLER:',fg='black',bg='#ADFF2F',width=20).grid(row=6,column=0)
    Label(s2, text='OVERS',fg='black',bg='#ADFF2F',width=20).grid(row=6,column=1)
    Label(s2, text='MAIDEN',fg='black',bg='#ADFF2F',width=20).grid(row=6,column=2)
    Label(s2, text='RUNS',fg='black',width=20,bg='#ADFF2F').grid(row=6,column=3)
    Label(s2, text='WICKETS',fg='black',width=20,bg='#ADFF2F').grid(row=6,column=4)
    Label(s2, text='ER.',fg='black',width=20,bg='#ADFF2F').grid(row=6,column=5)
    askBowler1Name()
    Label(s2, text=bowler1,fg='green',width=20,bg='#EECFA1').grid(row=7,column=0)
def thisOver():
    global to
    Thisover = Tk(className='This Over:')
    Thisover.configure(background='#33A1C9')
    for i in range(0,12):
        Label(Thisover, text=to[i],fg='blue',bg='#EECFA1',width=10).grid(row=1,column=i)
    
def scoreButtons():
    global s2
    buttonthisover=Button(s2,text='THIS OVER:',fg='black',bg='#EECFA1',command=thisOver).grid(row=8,column=0)
    Label(s2,bg='#EECFA1').grid(row=9)
    Label(s2,bg='#EECFA1').grid(row=10)
    button2 = Button(s2, text = '2', fg ='white',bg='grey',width=30,command=click2).grid(row=11,column=0)
    button5 = Button(s2, text = '5', fg ='white',bg='grey',width=28,command=click5).grid(row=11,column=1)
    button6 = Button(s2, text = '6', fg ='white',bg='#BF3EFF',width=30,command=click6).grid(row=11,column=2)
    button4 = Button(s2, text = '4', fg ='white',bg='#00EEEE',width=20,command=click4).grid(row=11,column=3)
    button1 = Button(s2, text = '1', fg ='white',bg='grey',width=20,command=click1).grid(row=11,column=4)
    buttonScore = Button(s2, text = 'SCORECARD', fg ='white',bg='black',width=30,command=sc).grid(row=12,column=0)
    button3 = Button(s2, text = '3', fg ='white',bg='grey',width=28,command=click3).grid(row=12,column=1)
    button1d = Button(s2, text = '1D', fg ='white',bg='grey',width=30,command=click1D).grid(row=12,column=2)
    buttoninfo = Button(s2, text = 'INFO', fg ='white',bg='black',width=20).grid(row=12,column=4)
    button0 = Button(s2, text = '0', fg ='white',bg='grey',width=20,command=click0).grid(row=12,column=3)
    buttonW = Button(s2, text = 'WICKET', fg ='white',bg='red',width=30,command=wicket).grid(row=13,column=0)
    buttonlb = Button(s2, text = 'LB', fg ='white',bg='#008080',width=28,command=lb).grid(row=13,column=1)
    buttonb = Button(s2, text = 'B', fg ='white',bg='#6C7B8B',width=30,command=lb).grid(row=13,column=2)
    buttonnb = Button(s2, text = 'NB', fg ='white',bg='red',width=20,command=nb).grid(row=13,column=3)
    buttonwd = Button(s2, text = 'WD', fg ='white',bg='#006400',width=20,command=wide).grid(row=13,column=4)
    
    
    
def totalScore():
    global s2,TotalRuns,inning,TotalWickets,totalOvers,oversBowled,now
    totalOvers=now
    Label(s2, text=(TotalRuns[inning],"/",TotalWickets[inning]),fg='green',width=8,bg='#EECFA1').grid(row=2,column=1)
    Label(s2, text=(('%.1f'%(oversBowled)),"/",totalOvers),fg='green',width=8,bg='#EECFA1',anchor=W,justify=LEFT).grid(row=2,column=2)
def secondscreen():
    global tm1,tm2,twb,opt,now,inning
    global s2
    l1= Label(s2, text=tm1.upper(),width=20,fg='red',bg='#EECFA1').grid(row=0,column=0)
    l2= Label(s2, text='            VS             ',fg='red',bg='#EECFA1').grid(row=0,column=1)
    l3= Label(s2, text=tm2.upper(),width=20,fg='red',bg='#EECFA1').grid(row=0,column=2)
    if inning==0:
        Label(s2,bg='#EECFA1').grid(row=1)
        if (opt=='bat' and twb==tm1) or (opt=='bowl' and twb==tm2):
           Label(s2,text=tm1.upper(),width=20,fg='green',bg='#EECFA1').grid(row=2,column=0)
        else:
           Label(s2,text=tm2.upper(),width=20,fg='green',bg='#EECFA1').grid(row=2,column=0)
    else:
        Label(s2,text=('need',TotalRuns[0]-TotalRuns[1],'in',ballsleft),fg='red',bg='#EECFA1').grid(row=1)
        if (opt=='bat' and twb==tm1) or (opt=='bowl' and twb==tm2):
           Label(s2,text=tm2.upper(),width=20,fg='green',bg='#EECFA1').grid(row=2,column=0)
        else:
           Label(s2,text=tm1.upper(),width=20,fg='green',bg='#EECFA1').grid(row=2,column=0)
    totalScore()
    batsman()
    bowler()
    scoreButtons()
    #bowlerstats()
    #batsmanstats()
    s2.mainloop()

def submit():
    global tm1,tm2,twb,opt,now
    tm1=FirstTeamName.get()
    tm2=SecondTeamName.get()
    twb=TossWonBy.get()
    opt=OptTo.get()
    now=NumberOfOvers.get()
    secondscreen()

l1 = Label(welcome, text='First Team Name:',width=19,bg='black',fg='green', font = ('Comic Sans MS',16)).grid(row=0) 
l2 = Label(welcome, text='Second Team Name:',width=19,bg='black',fg='green', font = ('Comic Sans MS',16)).grid(row=1)
l3 = Label(welcome, text='Toss won by:',width=19,bg='black',fg='green', font = ('Comic Sans MS',16)).grid(row=2) 
l4 = Label(welcome, text='Opt to:',width=19,bg='black',fg='green', font = ('Comic Sans MS',16)).grid(row=3) 
l5 = Label(welcome, text='Number of overs:',width=19,bg='black',fg='green', font = ('Comic Sans MS',16)).grid(row=4)
FirstTeamName = Entry(welcome) 
SecondTeamName = Entry(welcome)
TossWonBy = Entry(welcome) 
OptTo = Entry(welcome)
NumberOfOvers = Entry(welcome)
FirstTeamName.grid(row=0, column=1,columnspan=2)
SecondTeamName.grid(row=1, column=1)
TossWonBy.grid(row=2, column=1)
OptTo.grid(row=3, column=1)
NumberOfOvers.grid(row=4, column=1)
submit = Button(welcome, text='SUBMIT', width=30,bg='black',fg='light green', command=submit).grid(row=7,column=1)
welcome.mainloop()
