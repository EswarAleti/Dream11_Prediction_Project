import pandas as pd
import numpy as np
import math
from StringIO import StringIO
minimum_runs= 25
minimum_wickets= [1,2,3]
IPLteams=['SRH','CSK','RCB','RR','KKR','KXIP','DD','MI']

def batting_analysis(teamFile):
	df = pd.read_csv(teamFile)
	columns =df.columns[1:]
	df2 = df.copy()
	df.fillna(-1,inplace=True)
	csvstr ="player,match,balls,runs\n"
	for i,row in df.iterrows():
		for k in range(1,11):
			csvstr+=row['player']+","+str(k)+","+str(df['m'+str(k)+"b"].iloc[i])+","+str(df['m'+str(k)+"r"].iloc[i])+"\n"
	csvstr = csvstr.replace(",-1.0",",")
	df = pd.read_csv(StringIO(csvstr))
	df['cf']=0
	df2['cf']=0
	df2['avg']=0
	df2['srate']=0
	df['srate'] = df['runs']/df['balls'].astype(float)
	for i in df.player.unique():
		d = df[df['player']==i]
		l = d.runs.count()
		if l==0:
			continue
		cf = 0
		k = list(d.runs.dropna())
		b = list(d.balls.dropna())
		runsum,ballssum = sum(k),sum(b)
		list1 = k[0:int(l/2)]
		list2 = k[int(l/2):]
		for j in list1:
			cf+=1 if j >= minimum_runs and not np.isnan(j) else 0
		for j in list2:
			cf+=2 if j>= minimum_runs and  not np.isnan(j) else 0
		df.loc[df['player']==i,'cf']=math.ceil(cf/float(l)*100)/100
		df2.loc[df2['player']==i,'cf']= math.ceil(cf/float(l)*100)/100
		df2.loc[df2['player']==i,'avg']= math.ceil(runsum/float(l)*100)/100 
		df2.loc[df2['player']==i,'srate']= math.ceil((runsum/float(ballssum))*100*100)/100
	df2['performanceIndex']=df2['cf']*0.4 + df2['avg']/10*0.4 + df2['srate']/100*0.2
	df2.to_csv(teamFile,index=False)
def bowling_analysis(teamFile):
	df = pd.read_csv(teamFile)
	columns =df.columns[1:]
	df2 = df.copy()
	df.fillna(-1,inplace=True)
	csvstr ="player,match,runs,overs,wickets\n"
	for i,row in df.iterrows():
		for k in range(1,11):
			csvstr+=row['player']+","+str(k)+","+str(df['m'+str(k)+"r"].iloc[i])+","+str(df['m'+str(k)+"o"].iloc[i])+","+str(df['m'+str(k)+"w"].iloc[i])+"\n"
	csvstr = csvstr.replace(",-1.0",",")
	df = pd.read_csv(StringIO(csvstr))
	df['cf']=0
	df2['cf']=0
	for i in df.player.unique():
		d = df[df['player']==i]
		l = d.overs.count()
		if l==0:
			continue
		cf = 0
		k = list(d.wickets.dropna())
		o = list(d.overs.dropna())
		r = list(d.runs.dropna())
		runsum,overssumm = sum(r),sum(o)
		list1 = k[0:int(l/2)]
		list2 = k[int(l/2):]
		for j in list1:
			if not np.isnan(j):
				if int(j) == minimum_wickets[0]:
					cf+=1
				elif int(j) == minimum_wickets[1]:
					cf+=2
				elif int(j) >= minimum_wickets[2]:
					cf+=3
		for j in list2:
			if not np.isnan(j):
				if int(j) == minimum_wickets[0]:
					cf+=2
				elif int(j) == minimum_wickets[1]:
					cf+=4
				elif int(j) >= minimum_wickets[2]:
					cf+=6	

		df.loc[df['player']==i,'cf']=math.ceil(cf/float(l)*100)/100
		df2.loc[df2['player']==i,'cf']= math.ceil(cf/float(l)*100)/100
		df2.loc[df2['player']==i,'econamy']= math.ceil(runsum/float(overssumm)*100)/100
	df2['performanceIndex']=df2['cf']*0.8 + (1-df2['econamy']/10)*0.2
	df2.to_csv(teamFile,index=False)

def main():
	for i in range(0,len(IPLteams)):
		batting_analysis(IPLteams[i]+' Batting.csv')
		bowling_analysis(IPLteams[i]+' Bowling.csv')
if __name__ == "__main__": main()
