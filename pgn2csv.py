import chess.pgn
import pandas as pd
import sys

from datetime import datetime

if len(sys.argv) < 2:
    print('python3 ./pgn2csv.py <your pgn input file with games data> <your csv output file>')
    sys.exit(1)

games = []
    
with open(sys.argv[1]) as pgn:
    while True:
        game = chess.pgn.read_game(pgn)
        if not game:
            break
        result = game.headers['Result']
        if result == '1-0':
            winner = 'White'
        elif result == '0-1':
            winner = 'Black'
        elif result == '1/2-1/2':
            winner = 'Draw'
        else:
            winner = None

        tstr = game.headers['UTCDate'] + ' ' + game.headers['UTCTime']
        ts = int((datetime.strptime(tstr, '%Y.%m.%d %H:%M:%S') - datetime(1970, 1, 1)).total_seconds())

        opening = game.headers['Opening']
        if ':' in opening:
            opening_base = opening.split(':')[0]
        elif ',' in opening:
            opening_base = opening.split(',')[0]
        else:
            opening_base = opening

        if game.headers['WhiteElo'] == '?':
            white_elo = None
        else:
            white_elo = int(game.headers['WhiteElo'])
        if game.headers['BlackElo'] == '?':
            black_elo = None
        else:
            black_elo = int(game.headers['BlackElo'])
                
        g = {
            'eco': game.headers['ECO'],
            'opening': opening,
            'opening_base': opening_base,
            'winner': winner,
            'timestamp': ts,
            #'white': game.headers['White'],
            'white_elo': white_elo,
            #'black': game.headers['Black'],
            'black_elo': black_elo,
            'time_control': game.headers['TimeControl'],
            'termination': game.headers['Termination'],
        }

        games.append(g)

df = pd.DataFrame.from_dict(games)
df.to_csv(sys.argv[2], na_rep=None, index=False)
