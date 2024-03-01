#USU Mens Basketball Game Predictor 
## Rough Outline
---

### Step 1: Get the data (Team)

We are going to use all the team data from 2008-2024 from this website https://barttorvik.com/trank.php#. If you go to the data section under FAQs etc. it has instructions for the URL to download all team data from 2008 - 2024

A list of all the teams that the above website has are in the teams.txt file. We should check that the teams from the link below are in the team list in teams.txt and spelled the same way so there is no confusion when training the AI model. Some teams that we play don't have stats, but its only a few, usually exibition games.

We will also use the data from https://www.usustats.com/seasons/2023-24 from season 2008-2024. This data holds the opponent and the outcome(win/loss) for every USU mens basketball game. 

### Step 2: Format the Data (Team)

The final format of the data needs to be the following CSV format:

USU Stats, Opponent Name, Opponent Stats, Season, Home/Away, Win/Loss

This is a combination of the info from both websites and is vital for the model training process. If we want to predict games, we need to know the outcomes of previous games so we can evaulate the accuracy of our model.

We can get Opponent Stats and USU stats from the first link in CSV format. 
We get the win/loss and home/away data from the second link.

Once we get the csvs from both websites, we should be able to write a script that combines it into one csv.

### Step 3a: Perform Data Analysis for Machine Learning (Joe)

Should be pretty straight forward, will do in a Jupyter Notebook environment.

### Step 3b: Perform Data Visualizations for  website. (Hayden and Sophia)

This is up to you guys, you know more about this than I do. 

A few ideas that I had, but this isn't necessary and we could totally go in different directions.

 - compare USU stats accross years. (ie comparing the teams from 2008 - 2024)
 - comparing USU to the champions from each year
 - comparing USU to top 25 teams
 - ... and anythging else you guys think of.

 ### Step 4: Train the ML model
 ### Step 5: Tune the ML model
 ### Step 6: Serialize the ML model
Use `Joblib`
### Step 7: Build React + Django app
### Step 8: Incorporate AI model into Web App
### Step 8b: Add Data Visualizations to Web App
### Step 9: Host the web app on the cloud 
(nice to have but might have to save for later)
