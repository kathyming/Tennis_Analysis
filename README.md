# Tennis_Analysis

## Overview/Purpose
Using historical data from the Association of Tennis Professionals (ATP), the goal of this project is to determine probability of a player winning future matches. We selected tennis as a topic of interest because we're interested in Roger Federer's professional career statistics. We want to show which factors determine the match outcome, such as: points at net, number of aces during match, first serve percentage, points won at first serve, or number of double faults. Our dashboard will have options to filter by different players for easy comparison. For example, does a players points won at first serve influence if that player will win the overall match? 

In order to complete this analysis, we began by importing the csv files from our data source, github.com/JeffSackmann/tennis_atp. These contained massive amounts of information that we needed to narrow down, modify and clean to make it into usable data for our question. 

We combined multiple years of csv files, from 1998-2022, split rach match into two rows. One row for the winner's data, and one row for the loser's data. We removed null values as well as unwanted zeros to get the most comprehensive data. 

We dropped a majority of the columns from the original csvs to create a streamlined dataframe. We loaded this into pgadmin, and created the required tables. We have three tables, match_data, player_index & player_ranking, linking them based on the player id. 

Using these tables we will pull relevant information onto our tableau dashboard to craft visuals that show the correlation between our remaining columns. 

We have also incorporated a machine learning model into this project in order to try to best predict winning or losing a match based on the same remaining columns. Luckily, we have plenty of data rows to work with, so using the standard 80/20 test and train split has been very straightforward and we've avoided overfitting. We've so far opted to use logistical regression and random forest classifier models to get a higher accuracy but will continue searching for a best fit model. 

## Live links

*link to Tableau dashboard will go here for next submission.

Our Google Slide presentation draft can be found at the link below:
https://docs.google.com/presentation/d/1ntsYoUsov1nqJ6KO4gsVQClm7v3vvNwA2rq4yy1OXmo/edit?usp=sharing

