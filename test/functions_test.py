# -*- coding: utf-8 -*-
"""
>>> from penney.functions import *
>>> import random
>>> line(10,"*")
**********
>>> line()
###########
>>> random.seed(2)
>>> seq_generator()
'T'
>>> random.seed(5)
>>> seq_generator()
'H'
>>> find_winner("HTTTHH",{"Player1":"HTT","Player2":"TTH"})
'Player1'
>>> find_winner("TTTTTTT",{"Player1":"HTT","Player2":"TTH"})
>>> find_winner("TTTTTTTH",{"Player1":"HTT","Player2":"TTH"})
'Player2'
>>> random.seed(246)
>>> result = game({"Player1":"HTT","Player2":"TTH"},iter=1)
>>> result['Player1']
1
>>> result['Player2']
0
>>> random.seed(250)
>>> result = game({"Player1":"HTT","Player2":"TTH"},iter=1,print_status=True)
Round 1
HHTT
Point for -->Player1
###########
>>> result['Player1']
1
>>> result['Player2']
0
>>> random.seed(260)
>>> result = game({"Player1":"HTT","Player2":"TTH"},iter=3,print_status=True)
Round 1
TTH
Point for -->Player2
###########
Round 2
HTT
Point for -->Player1
###########
Round 3
HHTHTT
Point for -->Player1
###########
>>> result['Player1']
2
>>> result['Player2']
1
>>> check_seq(seq="HTHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
True
>>> check_seq(seq="HTHH",seq_len=3,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HTHA",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_seq(seq="HHHH",seq_len=4,seq_dict={1:"HTTT",2:"HHHH"})
False
>>> check_name("Name1",["Name2"])
True
>>> check_name("Name1",["Name1","Name2"])
False
>>> print_result(scores={"Player1":30,"Player2":32},seq_dict={"Player1":"HHT","Player2":"HTH"})
Scores Table :
Player2     32     HTH
Player1     30     HHT
Winner : Player2
>>> random.seed(300)
>>> computer_seq("HTH")
'HHT'
>>> player_filter(num=1,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 2
2
>>> player_filter(num=3,seq_len=3,print_status=True)
3
>>> player_filter(num=9,seq_len=3,print_status=True)
[Warning] Number of players automatically set to 8
8
"""