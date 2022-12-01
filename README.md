# Election Analysis

## Overview of Election Audit 

The purpose of this election audit is to record the vote counts and percentages for each candidate and by each county from the provided data. Additionally, the county with the highest vote count and the candidate with the highest number of votes will be highlighted with the total percentage of votes received. The audit will provide transparency into the data and can be used to confirm the results of any hand counting or other questions that may arise in regards to the vote totals by candidate or by county

## Election Audit Results

Below is a summary of several important data points found by the election audit:

* 369,711 total votes were cast in the congressional election
* The breakout for vote by county is as follows:
  * Jefferson: 10.5% (38,855 votes)
  * Denver: 82.8% (306,055 votes)
  * Arapahoe: 6.7% (24,801 votes)
* Denver county had the largest number of votes cast
* Votes received per candidate in order of appearance on the election results sheet are as follows:
  * Charles Casper Stockham: 23.0% (85,213 votes)
  * Diana DeGette: 73.8% (272,892 votes)
  * Raymon Anthony Doane: 3.1% (11,606)
* As visible above, the winner of the election was Diana DeGette with 73.8% of the vote and 272,892 total votes.

Results of the election by candidate and county can be viewed below:

![Election Audit Results](https://github.com/UnBearAble1/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Election Audit Summary

This script utilizes code that enable it to be used for elections of any size including many more candidates and many more counties. By avoiding hard coding any candidate or county names and instead being populated by the data from the provided spreadsheet, if there were additional names or additional counties, those data points would immediately be added to the list. The audit could also be expanded to include more districts with relatively little additional code. If a new column was added to include the number of the district and the data sheet populated with information from each district, a few lines of code identifying each district and then pulling out the candidate and voter information for each district would enable an audit for the entire state.

A second potential addition could be to break out the votes per county per candidate. This would require a few more lines of coding but can show how each county voted.

Another potential adjustment could be including the amount of registered voters for each county to show the percentage of registered voters that voted and provide more insight into voter turnout. This may require a second database, but could easily be incorporated in the same way the election results csv file was used.


