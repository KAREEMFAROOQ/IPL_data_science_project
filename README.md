Performed Exploratory Data Analysis and Data Visualization on IPL Match


Objective :

* To find the team that won most number of matches 
* To find the frequency of most Man of the Match awards and top 10 man of the match awards
* To find those who win man of the match in top 5
* To find the frequency of results
* Finding the most number of tosses win by each team
* Extracting the records where as teams who won batting first and batting second
* Finding match win by number of wickets and match win by number of runs
* Describing number of matches played each season and number of matches played in each city
* Finding out how many times team won the match after winning toss
* Describing number of runs scored by team as per match

Data Source Extracted From :https://www.kaggle.com/raghu07/ipl-data-till-2017

Libraries used in this EDA are Numpy,Pandas,Matpotlib and plots used are barplot,piechart,histogram,Lineplot


Dataset Information : 

* Number of attributes in dataset Match.csv are 17 
* Match_SK	
* match_id	
* Team1	
* Team2	
* match_date	
* Season_Year	
* Venue_Name	
* City_Name	
* Country_Name	
* Toss_Winner	
* match_winner	
* Toss_Name	
* Win_Type	
* Outcome_Type	
* ManOfMach	
* Win_Margin	
* Country_id
* Number of attributes in dataset Ball_By_Ball.csv are 48  
* MatcH_id	 
* Over_id	
* Ball_id	
* Innings_No	
* Team_Batting	
* Team_Bowling	
* Striker_Batting_Position	
* Extra_Type	
* Runs_Scored	
* Extra_runs	
* Wides	
* Legbyes	
* Byes	
* Noballs	
* Penalty	
* Bowler_Extras	
* Out_type	
* Caught	
* Bowled	
* Run_out	
* LBW	
* Retired_hurt	
* Stumped	
* caught_and_bowled	
* hit_wicket	
* ObstructingFeild	
* Bowler_Wicket	
* Match_Date	
* Season		
* Striker	
* Non_Striker	
* Bowler	
* Player_Out	
* Fielders	
* Striker_match_SK	
* StrikerSK	
* NonStriker_match_SK	
* NONStriker_SK	
* Fielder_match_SK	
* Fielder_SK	
* Bowler_match_SK	
* BOWLER_SK	
* PlayerOut_match_SK	
* BattingTeam_SK	
* BowlingTeam_SK	
* Keeper_Catch	
* Player_out_sk	
* MatchDateSK

Observation :
 
* As we observed most of the toss winned team was "Mumbai Indians"
* Out of 637,626 matches played normally and 6 matches played superovers,1 match was tied,1 match was abandoned and 3 matches had no results
* 100 most of matches are won by runs in between 0 to 20
* 70 most matches are won by wickets are 7 
* And highest of the matches won by "Mumbai Indians" by batting first innings,that are 47 matches
* And highest of the matches won by "Kolkata Knight Riders" by batting second innings,that are 46 matches 
* In IPL matches most of the matches won by "Mumbai Indians" are 91 matches
* In IPL top 3 teams are :
	1.Mumbai Indians
	2.Chennai Super Kings
	3.Kolkata Knight Riders
* Hightest IPL matches played in the year 2013 are 76 matches amd least matches played in the year 2009 are 57 matches
* Highest IPL matches played in the city Mumbai are 85 matches and least matches in Bloemfontein are 2 matches
* There are 50% chances are to win match those who won toss
* Number of matches won by team by winning toss are 324
* As per Match_id:598028 Rajasthan Royals won the match on Royal Challengers Banglorer by 10 runs 
