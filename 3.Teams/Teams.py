import numpy as n
import pandas as pd
df1=pd.read_csv('IPL_2017.csv')

teams=[['Sunrisers Hyderabad'],['Royal Challengers Bangalore'],['Mumbai Indians'],['Rising Pune Supergiant'],['Gujarat Lions'],['Kolkata Knight Riders'],['Kings XI Punjab'],['Delhi Daredevils']]

def generate_team_players():
        for i in range(0,df1.shape[0]):
                for j in range(0,8):
                        if(df1['batting_team'][i] == teams[j][0]):
                                   if(df1['batsman'][i] not in teams[j]):
                                        teams[j].append(df1['batsman'][i])
                for j in range(0,8):
                        if(df1['bowling_team'][i] == teams[j][0]):
                                   if(df1['bowler'][i] not in teams[j]):
                                        teams[j].append(df1['bowler'][i])

def show_teams():
        for i in range(0,8):
        	print teams[i]
        	print 
                #print '************',teams[i][0],'*************'
                #for j in range(1,len(teams[i])):
                #       print teams[i][j]

def main():
        generate_team_players()
        show_teams()

if __name__ == "__main__": main()                              
