import numpy as np
import pandas as pd

def batsmanNewRecord():

	team=raw_input("1. SRH\n2. RCB\n3. KKR\n4. CSK\n5. DD\n6. KXIP\n7. RR\n8. MI\nEnter your team (e.g. SRH): ")
	df=pd.read_csv(team+" Batting.csv")
	
	while True:
		print df['player']
		playerIndex=input("\nEnter index of player to enter score or -1 to exit or -2 to place a new player: ")
		if playerIndex==-1:
			break;
		elif playerIndex==-2:
			z=df.columns
			x={}
			x['player']=[raw_input("Enter player name: ")]
			for i in z[1:]:
				x[i]=[np.nan]
			df=df.append(pd.DataFrame(x)).reset_index(drop=True)
			df=df[z]
		else:	
			runs=input("Enter runs scored: ")
			balls=input("Enter number of balls defended: ")
			if not np.isnan(df.iloc[playerIndex,20]):
				for i in range(1,18,2):
					df.iloc[playerIndex,i],df.iloc[playerIndex,i+1]=df.iloc[playerIndex,i+2],df.iloc[playerIndex,i+3]
				df.iloc[playerIndex,19]=runs
				df.iloc[playerIndex,20]=balls
			else:
				for i in range(1,20,2):
					if np.isnan(df.iloc[playerIndex,i]):
						df.iloc[playerIndex,i]=runs
						df.iloc[playerIndex,i+1]=balls
						break
	df.to_csv(team+" Batting.csv",index=False);
	
def bowlerNewRecord():

	team=raw_input("1. SRH\n2. RCB\n3. KKR\n4. CSK\n5. DD\n6. KXIP\n7. RR\n8. MI\nEnter your team (e.g. SRH): ")
	df=pd.read_csv(team+" Bowling.csv");
	while True:
		print df['player']
		playerIndex=input("\nEnter index of player to enter score or -1 to exit or -2 to place a new player: ")
		if playerIndex==-1:
			break;
		elif playerIndex==-2:
			z=df.columns
			x={}
			x['player']=[raw_input("Enter player name: ")]
			for i in z[1:]:
				x[i]=[np.nan]
			df=df.append(pd.DataFrame(x)).reset_index(drop=True)
			df=df[z]
		else:	
			overs=input("Enter number of Overs: ")
			runs=input("Enter runs Given: ")
			wickets=input("Enter number of Wickets picked: ")
			if not np.isnan(df.iloc[playerIndex,30]):
				for i in range(1,27,3):
					df.iloc[playerIndex,i],df.iloc[playerIndex,i+1],df.iloc[playerIndex,i+2]=df.iloc[playerIndex,i+3],df.iloc[playerIndex,i+4],df.iloc[playerIndex,i+5]
				df.iloc[playerIndex,28]=runs
				df.iloc[playerIndex,29]=overs
				df.iloc[playerIndex,30]=wickets
			else:
				for i in range(1,30,3):
					if np.isnan(df.iloc[playerIndex,i]):
						df.iloc[playerIndex,i]=runs
						df.iloc[playerIndex,i+1]=overs
						df.iloc[playerIndex,i+2]=wickets
						break
	df.to_csv(team+" Bowling.csv",index=False);
	
def main():
	print '-----------------Innings 1 Batting------------------'
	batsmanNewRecord();
	print '-----------------Innings 2 Batting------------------'
	batsmanNewRecord();
	print '-----------------Innings 1 Bowling------------------'
	bowlerNewRecord();
	print '-----------------Innings 2 Bowling------------------'
	bowlerNewRecord();
if __name__ == "__main__": main()
