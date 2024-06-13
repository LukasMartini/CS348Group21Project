from server import get_db_connection
from convert_history import parse_hand_history
import psycopg2 as pg2

def testQuery():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # parse_hand_history('hand_histories/poker_stars/handHistory-126997.txt')

    try:
        with open('backend/sql/create_tables.sql') as ct:
            cur.execute(ct.read())
    except pg2.errors.DuplicateTable:
        cur.execute('ROLLBACK;')

    try:
        cur.execute('''INSERT INTO poker_hand(id, site_hand_id,  tournament_id, game_type, small_blind, big_blind, currency, 
                                          total_pot, rake, played_at, table_name, max_players) 
                    VALUES (1, 1, 1, \'Cash\', 0.1, 0.1, \'CAD\', 0.1, 0.1, \'January 8 04:05:06 1999 PST\', \'Gaussia\', 6);''')
        cur.execute('''INSERT INTO player(id, name) VALUES (1, \'Ted\');''')
        cur.execute('''INSERT INTO player_action(id, player_id, hand_id, seat_number, action_type, amount) 
                       VALUES (1, 1, 1, 1, \'folds\', 0.01);''')
        cur.execute('''INSERT INTO player_cards(id, player_id, hand_id, hole_card1, hole_card2, position, stack_size)
                VALUES (1, 1, 1, \'AC\', \'AS\', 1, 0.1);''')
        cur.execute('''INSERT INTO board_cards(id, hand_id, flop_card1, flop_card2, flop_card3, turn_card, river_card)
                       VALUES (1, 1, \'AC\', \'2C\', \'3C\', \'4C\', \'TC\');''')
        
    except pg2.errors.UniqueViolation:
        # pass
        cur.execute('ROLLBACK;')
        with open('backend/sql/fetchHandQueryTemplate.sql') as q:
            hand_id = 1
            player_id = 'Ted'
            cur.execute(q.read())
            cur.execute(f'EXECUTE handData({hand_id}, \'{player_id}\')')
            print(cur.fetchall())

    # cur.execute('DROP TABLE poker_hand, player, player_action, player_cards, board_cards;')
    # with open('backend/sql/create_tables.sql') as ct:
    #     cur.execute(ct.read())

    # with open('backend/sql/fetchHandQueryTemplate.sql') as q:
    #     cur.execute(q.read())
    #     # print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()

testQuery()
