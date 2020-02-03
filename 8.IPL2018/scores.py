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

def ipl2018TeamBat(team):
	team=[[i] for i in team]
	for i in range(0,len(team)):
		for j in range(0,len(batsmen)):
			if team[i][0] in batsmen[j]:
				team[i].extend(batsmen[j][1:])
	return team
def ipl2018TeamBall(team):
	team=[[i] for i in team]
	for i in range(0,len(team)):
		for j in range(0,len(bowlers)):
			if team[i][0] in bowlers[j]:
				team[i].extend(bowlers[j][1:])
	return team	

def createNewBatCSV(team,teamName):
	lable=['player']
        for i in range(1,11):
        	lable.append("m"+str(i)+"r")
        	lable.append("m"+str(i)+"b")
        df = pd.DataFrame.from_records(team, columns=lable)
        df.to_csv(teamName+' Batting.csv',index=False)
        
def createNewBallCSV(team,teamName):
	lable=['player']
        for i in range(1,11):
        	lable.append("m"+str(i)+"r")
        	lable.append("m"+str(i)+"o")
        	lable.append("m"+str(i)+"w")
        df = pd.DataFrame.from_records(team, columns=lable)
        df.to_csv(teamName+' Bowling.csv',index=False)
        
def main():
        for i in range(0,8):
        	creatBatsmenList(teams[i][0]+" Bat");
        
        for i in range(0,8):
        	creatBowlersList(teams[i][0]+" Bowl");
        
        for i in range(0,len(bowlers)):
        	for j in range(2,len(bowlers[i]),3):
        		bowlers[i][j]=int(bowlers[i][j]/6)+float(bowlers[i][j]%6)/10
        	
        SRH=['DA Warner','B Kumar','S Dhawan','Shakib Al Hasan','KS Williamson','MK Pandey','CR Brathwaite','YK Pathan','WP Saha','Rashid Khan','DJ Hooda','S Kaul','T Natarajan','Mohammad Nabi','Basil Thampi','Sandeep Sharma','Sachin Baby','CJ Jordan','B Stanlake','Bipul Sharma']
	RCB=['V Kohli','AB de Villiers','BB McCullum','CR Woakes','C de Grandhomme','UT Yadav','YS Chahal','M Vohra','A Choudhary','Mandeep Singh','Washington Sundar','P Negi','Mohammed Siraj','PA Patel','TG Southee','CJ Anderson']                       
	CSK=['MS Dhoni','SK Raina','RA Jadeja','F du Plessis','Harbhajan Singh','DM Bravo','SR Watson','AT Rayudu','DL Chahar','M Vijay','SW Billings','M Wood','Imran Tahir','KV Sharma','SN Thakur',]
	DD=['SS Iyer','CH Morris','RR Pant','GJ Maxwell','G Gambhir','JJ Roy','C Munro','V Shankar','DT Christian','NV Ojha','Mohammed Shami','A Mishra','R Tewatia','AR Patel','Avesh Khan','S Nadeem','TA Boult']
	KKR=['KD Karthik','CA Lynn','N Rana','PP Chawla','RV Uthappa','SP Narine','MG Johnson','Kuldeep Yadav','R Vinay Kumar']
	RR=['SPD Smith','RA Tripathi','AM Rahane','STR Binny','BA Stokes','SV Samson','JC Buttler','DS Kulkarni','JD Unadkat','Ankit Sharma','Anureet Singh']
	MI=['RG Sharma','JJ Bumrah','HH Pandya','KA Pollard','Mustafizur Rahman','SA Yadav','KH Pandya','Ishan Kishan','RD Chahar','SS Tiwary','BCJ Cutting','PJ Sangwan','AP Tare','AF Milne','MJ McClenaghan']
	KXIP=['AR Patel','Yuvraj Singh','KK Nair','CH Gayle','DA Miller','AJ Finch','MP Stoinis','MA Agarwal','AS Rajpoot','MK Tiwary','MM Sharma','BB Sran','AJ Tye','AD Nath','']
       	
        createNewBatCSV(ipl2018TeamBat(SRH),"SRH")
        createNewBallCSV(ipl2018TeamBall(SRH),"SRH")
        createNewBatCSV(ipl2018TeamBat(RR),"RR")
        createNewBallCSV(ipl2018TeamBall(RR),"RR")
        createNewBatCSV(ipl2018TeamBat(RCB),"RCB")
        createNewBallCSV(ipl2018TeamBall(RCB),"RCB")
        createNewBatCSV(ipl2018TeamBat(CSK),"CSK")
        createNewBallCSV(ipl2018TeamBall(CSK),"CSK")
        createNewBatCSV(ipl2018TeamBat(KXIP),"KXIP")
        createNewBallCSV(ipl2018TeamBall(KXIP),"KXIP")
        createNewBatCSV(ipl2018TeamBat(KKR),"KKR")
        createNewBallCSV(ipl2018TeamBall(KKR),"KKR")
        createNewBatCSV(ipl2018TeamBat(DD),"DD")
        createNewBallCSV(ipl2018TeamBall(DD),"DD")
        createNewBatCSV(ipl2018TeamBat(MI),"MI")
        createNewBallCSV(ipl2018TeamBall(MI),"MI")
       	
	
if __name__ == "__main__": main()                              
