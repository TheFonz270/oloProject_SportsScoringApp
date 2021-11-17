

Intro
_____________________________________________________________________________________________

Hello, and welcome to my WIP Warhammer Sccoring App. This was my first solo project using python, flask, sql, html, and css. 

The purpose of the app is:

    1. to allow users to add players, pit them against each other in games, and track the wins and losses of each payer.

    2. given a field of players, the app will generate a "round" of games using the swiss pairinf=gs system (working limitations below.)

Brief
_____________________________________________________________________________________________

MVP: 
The app should allow the user to create, edit, & remove players.
The user should be able to create new games
There should be a way to display all the games for a player, and all the players in a game.
The app should display if a game was won or lost

Extension: 
Given a field of 8 players, the app should be able to gereate 4 games at random, 
then given the results of those 4 games should be able to generate the next round of games
using the Swiss pairings system.


limitations
_____________________________________________________________________________________________

The app does not track ties, if one of your game's results in a tie, you should resolve this outside of the app, 
and adjust the agreed upon's players by 1 so the app will recognise them as the winner.

The app uses a simplified version of the swiss pairings system and as currently only takes wins into account, not total points. 
This will hopefully be rectified in a future update.

If you have an odd number of players the generate round button will simply miss the last place player, 
so manual game creation will be necessary to cycle that player in.

Players can not be deleted from the app if they are present in existing games. their games would have to be deleted first. 

Please note that in it's current version deleting/updating games with different winners will not undo the players win/loss record automatically, it will add a result. 
You can update players manually to rectify this before generating further game rounds.

Players must have unique names for the swiss rounds to generate properly.

To Run
_____________________________________________________________________________________________

1. To run the app you will first need to create a database on your local machine called "swiss_tabletop"
2. you will then need to run /db/swiss_tabletop.sql to create your tables
3. then you'll need to run a local instance of flask to host the app. 

