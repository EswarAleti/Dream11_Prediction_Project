import numpy as np
import pandas as pd
ipl=pd.read_csv('IPL_2017.csv')

teams=[['Sunrisers Hyderabad'],['Royal Challengers Bangalore'],['Mumbai Indians'],['Rising Pune Supergiant'],['Gujarat Lions'],['Kolkata Knight Riders'],['Kings XI Punjab'],['Delhi Daredevils']]

def generate_team_players():

        for i in range(0,ipl.shape[0]):
                for j in range(0,8):
                        if(ipl['batting_team'][i] == teams[j][0]):
                                   if(ipl['batsman'][i] not in teams[j]):
                                        teams[j].append(ipl['batsman'][i])
                for j in range(0,8):
                        if(ipl['bowling_team'][i] == teams[j][0]):
                                   if(ipl['bowler'][i] not in teams[j]):
                                        teams[j].append(ipl['bowler'][i])                                        

def show_teams():

        for i in range(0,8):
                print '************',teams[i][0],'*************'
                for j in range(1,len(teams[i])):
                        print teams[i][j]
                        
def create_files():
                        
        for i in range(0,8):
                single_team=teams[i][1:]
                single_team=[[x] for x in  single_team] #converting 1D list into 2D
                for j in range(0,len(single_team)):
                        for k in range(0,54):
                                single_team[j].append('\0')
                labels = ['player']
                for match_no in range(1,19):
                	labels.append('m'+str(match_no)+'r')
                	labels.append('m'+str(match_no)+'o')
                	labels.append('m'+str(match_no)+'w')
                df = pd.DataFrame.from_records(single_team, columns=labels)
                df.to_csv(teams[i][0]+'.csv',index=False)
def scores(team_name):
	teamDF=pd.read_csv(team_name+'.csv')
	teamDF.set_index("player", inplace=True)
	match=1
	i=0
	dismissals=['caught','bowled','hit wicket','lbw','stumped']
	while(i<ipl.shape[0]):
		if(ipl['bowling_team'][i]==team_name):
			if not np.isnan(teamDF.loc[ipl['bowler'][i],'m'+str(match)+'o']):
				teamDF.loc[ipl['bowler'][i],'m'+str(match)+'r']=int(teamDF.loc[ipl['bowler'][i],'m'+str(match)+'r'])+int(ipl['wide_runs'][i])+int(ipl['noball_runs'][i])+int(ipl['batsman_runs'][i])
				if int(ipl['wide_runs'][i])==0 and int(ipl['noball_runs'][i])==0:
					teamDF.loc[ipl['bowler'][i],'m'+str(match)+'o']=int(teamDF.loc[ipl['bowler'][i],'m'+str(match)+'o'])+1
			else:
				teamDF.loc[ipl['bowler'][i],'m'+str(match)+'r']=int(ipl['wide_runs'][i])+int(ipl['noball_runs'][i])+int(ipl['batsman_runs'][i])
				if int(ipl['wide_runs'][i])==0 and int(ipl['noball_runs'][i])==0:
					teamDF.loc[ipl['bowler'][i],'m'+str(match)+'o']=1
					teamDF.loc[ipl['bowler'][i],'m'+str(match)+'w']=0
			
			if ipl.loc[i,'dismissal_kind'] in dismissals:
				if not np.isnan(teamDF.loc[ipl['bowler'][i],'m'+str(match)+'w']):
					teamDF.loc[ipl['bowler'][i],'m'+str(match)+'w']=int(teamDF.loc[ipl['bowler'][i],'m'+str(match)+'w'])+1
				else:
					teamDF.loc[ipl['bowler'][i],'m'+str(match)+'w']=1
				
			if i<ipl.shape[0]-1 and ipl['batting_team'][i]!=ipl['batting_team'][i+1]:
				match=match+1
			elif i<ipl.shape[0]-1 and ipl['match_id'][i]!=ipl['match_id'][i+1]:
				match=match+1
		i=i+1
	teamDF.to_csv(team_name+' Bowl.csv',index=True)

def main():
        generate_team_players()
        create_files()
        for i in range(0,8):
        	scores(teams[i][0]);

if __name__ == "__main__": main()                              
