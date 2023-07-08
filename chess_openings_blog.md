<p align="center">
  <img src="images/Analyzing_Chess_Opening_Systems.jpg?raw=true"/>
</p>

# Chess Openings: How often they are played and what are their success rates?

I am a chess player. I used to play a lot but when I was younger but then lost
contact to the game due to lack of playing partners. A couple of
years ago I discovered [Lichess.org](https://lichess.org) and got back into playing. This
re-boosted my playing level and so I thought I use their free data
for this data science project on chess openings.

[Lichess.org](https://lichess.org) is a free online chess server that provides an extensive
data set on all games that have been played between Jan 2013 until
today at the [Lichess.org open database](https://database.lichess.org/). At the time of writing, this
data comprises almost 1.5TB.

Lichess data provides information about the players' skill (in terms of their [ELO](https://en.wikipedia.org/wiki/Elo_rating_system) points), the result
of the game and, most importantly for the purposes of this article, the opening that was played. I ran
a data science study and investigated three key questions.

## The Data

Lichess free data is in PGN format. It provides metadata on the games,
the moves made in the games plus timing and scoring information. It
is tailored for chess engines to replay and analyze games. I was interested only
in the metadata.  

<p align="center">
  <img alt="image" src="images/metadata.png">
</p>

For this article, I picked a sample file containing the metadata of 121,322 Lichess games
with 9 attribute each:

eco: the [ECO code](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)of the opening
opening: the opening name
opening_base: the opening system (see above)
winner: the winner of the game as one of ['White', 'Black', 'Draw'].
timestamp: when the game was played
time_control: Time limit plus seconds added per move
termination: Reason for terminating the game as one of ['Normal', Time forfait'].

The original PGN data also contained the playesr's Lichess user names. I stripped them for privacy reasons.

## 1. What are the most frequently used opening systems?

## 2. What are the most frequently used opening systems in different skill levels?

## 3. What are the most succeessful opening systems for White and Black per skill level?

## Key takeaways
