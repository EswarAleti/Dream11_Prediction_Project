import numpy as np
import pandas as pd

teams=[['Sunrisers Hyderabad'],['Royal Challengers Bangalore'],['Mumbai Indians'],['Rising Pune Supergiant'],['Gujarat Lions'],['Kolkata Knight Riders'],['Kings XI Punjab'],['Delhi Daredevils']]
batsmen=[]
bowlers=[]
                        
def creatBatsmenList(team_name):
	teamDF=pd.read_csv(team_name+'.csv')
	teamDF.set_index("player", drop = False)
	i=0
	li=(teamDF.values.tolist())
	while(i<teamDF.shape[0]):
		cleanedList = [x for x in li[i] if str(x) != 'nan']
		length=len(cleanedList)
		if length>21:
			cleanedList=cleanedList[:1] + cleanedList[length-20:]
		if length>1:
			batsmen.append(cleanedList)
		i=i+1

def creatBowlersList(team_name):
	teamDF=pd.read_csv(team_name+'.csv')
	teamDF.set_index("player", drop = False)
	i=0
	li=(teamDF.values.tolist())
	while(i<teamDF.shape[0]):
		cleanedList = [x for x in li[i] if str(x) != 'nan']
		length=len(cleanedList)
		if length>31:
			cleanedList=cleanedList[:1] + cleanedList[length-30:]
		if length>1:
			bowlers.append(cleanedList)
		i=i+1
			
def main():
        for i in range(0,8):
        	creatBatsmenList(teams[i][0]+" Bat");
        
        for i in range(0,8):
        	creatBowlersList(teams[i][0]+" Bowl");
        
        for i in range(0,len(batsmen)):
		print batsmen[i]
		print
	
	for i in range(0,len(bowlers)):
		print bowlers[i]
		print

if __name__ == "__main__": main()                              
