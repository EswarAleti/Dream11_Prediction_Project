import pandas as pd
import numpy as np
batsmanIndex=[]
IPLteams=['SRH','CSK','RCB','RR','KKR','KXIP','DD','MI']
team11=[]
def getTeam():

	team1=raw_input("1. SRH\n2. RCB\n3. KKR\n4. CSK\n5. DD\n6. KXIP\n7. RR\n8. MI\nEnter team1 (e.g. SRH): ")
	dfBat=pd.read_csv(team1+" Batting.csv")
	dfBall=pd.read_csv(team1+" Bowling.csv")
	team2=raw_input("1. SRH\n2. RCB\n3. KKR\n4. CSK\n5. DD\n6. KXIP\n7. RR\n8. MI\nEnter team2 (e.g. SRH): ")
	dfBat=dfBat.append(pd.read_csv(team2+" Batting.csv")).reset_index(drop=True)
	dfBall=dfBall.append(pd.read_csv(team2+" Bowling.csv")).reset_index(drop=True)
	
	wicket_keeper(team1,team2)
	#batsmen(team1,team2)
	#bowler(team1,team2)
	#allrounder(team1,team2)
	
	print team11
	
def wicket_keeper(team1,team2):

	dfBat=pd.read_csv(team1+" Batting.csv")
	dfBat=dfBat.append(pd.read_csv(team2+" Batting.csv")).reset_index(drop=True)
	
	print dfBat['player']
	wk1=input('Enter index of wicket keeper1: ')
	wk2=input('Enter index of wicket keeper2: ')
	if dfBat.loc[wk1,'performanceIndex'] > dfBat.loc[wk2,'performanceIndex']:
		team11.append(dfBat.loc[wk1,'player'])
	else:
		team11.append(dfBat.loc[wk2,'player'])
	
def batsmen(team1,team2):

	dfBat=pd.read_csv(team1+" Batting.csv")
	dfBat=dfBat.append(pd.read_csv(team2+" Batting.csv")).reset_index(drop=True)
	
	print dfBat['player']
	x=raw_input("Enter batsman indices ")
	batsmanIndex.extend(int(i) for i in x.split())
	dfBat = dfBat[dfBat.index.isin(batsmanIndex)]
	l = list(dfBat.performanceIndex.nlargest(5))
	dfBat = dfBat[dfBat['performanceIndex'].isin(l)]
	team11.append(list(dfBat['player']))	
		
def bowler(team1,team2):

	dfBall=pd.read_csv(team1+" Bowling.csv")
	dfBall=dfBall.append(pd.read_csv(team2+" Bowling.csv")).reset_index(drop=True)
	
	print dfBall['player']
	x=raw_input("Enter bowler indices ")
	batsmanIndex.extend(int(i) for i in x.split())
	dfBall = dfBall[dfBall.index.isin(batsmanIndex)]
	l = list(dfBall.performanceIndex.nlargest(3))
	dfBall = dfBall[dfBall['performanceIndex'].isin(l)]
	team11.append(list(dfBall['player']))
	
	
def allrounder(team1,team2):
	
	dfBat=pd.read_csv(team1+" Batting.csv")
	dfBat=dfBat.append(pd.read_csv(team2+" Batting.csv")).reset_index(drop=True)
	
	dfBall=pd.read_csv(team1+" Bowling.csv")
	dfBall=dfBall.append(pd.read_csv(team2+" Bowling.csv")).reset_index(drop=True)
	
	df = dfBall.merge(dfBat,how='inner',on=['player'])
	df['ar']=  df['performanceIndex_x'] + df['performanceIndex_y']
	print df['player']
	
	x=raw_input("Enter Allrounder indices: ")
	batsmanIndex.extend(int(i) for i in x.split())
	df = df[df.index.isin(batsmanIndex)]
	l = list(df.ar.nlargest(3))
	df = df[df['ar'].isin(l)]
	team11.append(list(df['player']))
	
def main():
	getTeam()
if __name__ == "__main__": main()
