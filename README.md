# FIFAYouthBot
This is a discord bot created to assist in FIFA Leagues in a discord server.
The bot is hosted using replit and uptimebot. 
## Functions
It has simple functions include $youth and $retire. It provides outputs as embeds in discord channels. 
#### $scout
$scout(followed by team, position, continent) (example: $scout Tolouse FWD Europe) generates a scouted player based off of team ratings. First, it takes in a random age between 18 and 25, then it uses the input features obtained to predict the rating of such a player based off previously trained data, lastly it generates potential between 5 and 15 to display the final player output as an embed. XgBoost was used for this model. 
#### $youth
$youth(followed by tier) (example: $youth Elite) creates a random youth player with the given tier's rating ranges. It gives player position, rating, potential, age, trait and versatile subtrait.
The bot also sends a selected image for certain types of players. 
#### $retire
$retire(followed by threshold) (example: $retire 55, retired if random number <= 55). $retire generates a random number from 1-100 to decide if your player retires or not.
