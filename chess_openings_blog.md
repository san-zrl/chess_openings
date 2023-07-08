<p align="center">
  <img src="https://github.com/san-zrl/chess_openings/blob/main/images/Queens_Gambit_Declined.png" width="320" height="320"/>
</p>

# Chess Openings: How often they are played and what are their success rates?

I am a chess player. I used to play a lot but when I was younger but then lost
contact to the game due to lack of playing partners. A couple of
years ago I discovered [Lichess.org](https://lichess.org) and got back into playing. This
re-boosted my playing level and so I thought I use their free data
for this data science project on chess openings.

[Lichess.org](https://lichess.org) is a free online chess server that provides an extensive
data set on all games that have been played between January 2013 until
today at the [Lichess.org open database](https://database.lichess.org/). At the time of writing, this
data comprises almost 1.5TB.

Lichess data provides information about the players\' skill (in terms of their [ELO](https://en.wikipedia.org/wiki/Elo_rating_system) points), the result
of the game and, most importantly for the purposes of this article, the opening that was played. I ran
a data science study and investigated three key questions.

1. **What are the most frequently used opening systems?**
2. **What are the most frequently used opening systems in different skill levels?**
3. **What are the most successful opening systems for White and Black per skill level?**

## The Data

Lichess free data is in PGN format. It provides metadata on the games,
the moves made in the games plus timing and scoring information. It
is tailored for chess engines to replay and analyze games. I was interested only
in the metadata.  

[[https://github.com/san-zrl/chess_openings/blob/main/images/metadata.png]]

I added an `opening_base` column that generalizes the particular opening to the root opening system.
Chess openings are classified in a tree-like fashion. The tree starts at the opening system (e.g.,
Queen\'s Pawn Game) and then names the variants and sub-variants (e.g., Queen's Pawn Game: Colle
System, Anti-Colle). There are complex openings with lots of variants for which a lot of theoretical 
research has been done, and less complex openings. In order to get reasonably sized classes, I decided
to map the individual opening to its opening system which is stored in a separate column.

For this article, I picked a sample file containing the metadata of 121,322 Lichess games
with 9 attributes each:

- `eco`: the [ECO code](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)of the opening
- `opening`: the opening name
- `opening_base`: the opening system (see above)
- `winner`: the winner of the game as one of ['White', 'Black', 'Draw'].
- `timestamp`: when the game was played
- `time_control`: Time limit plus seconds added per move
- `termination`: Reason for terminating the game as one of ['Normal', Time forfait'].

The original PGN data also contained the player\'s Lichess user names. I stripped them for privacy reasons.

## Q1: What are the most frequently used opening systems?

This is the easiest of all questions to answer. We only have to count the unique opening systems. The top-10
of this list is shown below. We see a mix of rare and complex opening systems
which is due to the fact that the analysis was performed across all
games independent of the players skill levels.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Total_Distribution_of_Opening_Systems.jpg]]

The first three ranks contain complex systems with many variants that
are probably used by more experienced players. The King\'s Pawn Game
is a special case since it is both a system that beginners learn first
as well as a system that is sometimes used by experienced players.
Rank 5 and 6 are examples of rare openings probably used by beginners.

## Q2: What are the most frequently used opening systems in different skill levels?

Players have different skill level indicated by their ELO points. I grouped the players into four different
groups according to the ELO points

1. Beginners: ELO &le; 1200
2. Intermediate: 1200 &lt; ELO &le; 1600
3. Advanced: 1600 &lt; ELO &le; 2000
4. Expert: ELO &gt; 2000

In order to classify games I computed the average of the ELO of the two opponents to get
a classification of games. When we look at the distribution of opening systems in the different
game classes we see some changes.

In the beginners level, the King\'s Pawn Game dominates. In addition, we see rare and aggressive
openings such as Scandinavian, Van\'t Kruijs, Hungarian and Kadas.
These openings aim to outsmart the opponent quickly or luring him into
a trap and can thus hardly be seen on tournament level. As we move
on to intermediate players, the Sicilian Defense begins to dominate
and keeps doing so in the higher layers. The King\'s Pawn Game is on
a decline.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Distribution_of_Opening_Systems.jpg]]

Intermediate players apparently pick more sophisticated
openings and we can see the rise of the Queen\'s Pawn Game and the
French Defense. In the advanced level this evolution continues.
The King\'s Pawn Game has completely disappeared from the top-10 list
and common openings such as Sicilian, French, Queen\'s Pawn Game or
the Caro-Cann system can be seen. In the top-10 list of openings on
expert level, Sicilian advances its lead to more than 33%, leading by
far over French with 15%. English and the Caro-Cann system got
stronger and the Queen's Gambit Declined shows up.

## Q3: What are the most successful opening systems for White and Black per skill level?

In the beginner level, for both Black and White King\'s Pawn Game
or Van\'t Kruijs seem to be the recommended choice since White won
in more than 20% and 17% of all cases, respectively, which is better
than for any other opening.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Games_won_per_opening_system_[Beginners].jpg]]

At intermediate level, the ranking up to rank 4 is the same for
Black and White with Sicilian Defense, King\'s Pawn Game, French
Defense, and Queen\'s Pawn Game being the most promising choices.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Games_won_per_opening_system_[Intermediate].jpg]]

At advanced level, King\'s Pawn is not successful anymore for White
while Sicilian, French, and Queen\'s Pawn keep their strong positions.
Sicilian seems very successful for Black.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Games_won_per_opening_system_[Advanced].jpg]]

For expert level players, Sicilian seems to be the opening base of
choice both for White and Black. White won in 21% of all cases,
clearly ahead of French. For Black the numbers are very clear.
Black won with Sicilian in 35% or all cases, almost three times as
often as with the runner-up French.

[[https://github.com/san-zrl/chess_openings/blob/main/images/Games_won_per_opening_system_[Experts].jpg]]

## Key Takeaways

The overall distribution of opening systems show the mixture of preferred system
across all levels.

When we break down per skill level the picture becomes clearer. The King'\s Pawn Game
dominates in the beginner group, declines for intermediate players and finally disappears
from the top-10 list to be replaces by more sophisticated opening like Sicilian and French.

The most successful opening systems at beginner level seem to be King\'s Pawn Game
or Van\'t Kruijs for both Black and White. As intermediate level, players have success with
Sicilian Defense, King\'s Pawn Game, French Defense, and Queen\'s Pawn Game without much
difference between Black and White. At advanced level, King\'s Pawn is not successful anymore for White
while Sicilian, French, and Queen\'s Pawn keep their strong positions.
Sicilian seems very successful for Black. For expert level players, Sicilian seems to be the opening base of
choice both for White and Black.

As a player you should build up a repertoire of your favourite openings from the open, half-open, and closed
systems, study them well and practise them repeatedly against stronger players. As you become stronger you
should switch to more complex systems.
