#!/usr/bin/env python

from packages.automata import Automaton
from packages.lab1 import STTDispatcher, TTRDispatcher

with open('input.txt', 'r') as fp:
    s = fp.read()

with open('output.txt', 'w') as fp:
    STTD = STTDispatcher()
    # лексер
    A = Automaton('packages/lab1/c_stt.xml', STTD)

    if A.parse(s):
        token_stream = STTD.token_stream
        token_pos = STTD.token_pos
        # добавить EOF к позициям лексем       
        token_pos.append(STTD.last_char_pos)

        TTRD = TTRDispatcher()
        B = Automaton('packages/lab1/c_ttr.xml', TTRD)
        if B.parse(token_stream):
            fp.write('CORRECT\n')
        else:
            err_tok = TTRD.err_tok
            err_pos = token_pos[err_tok]
            if not TTRD.duplicate:
                fp.write(f'INCORRECT {err_pos[0]}:{err_pos[1]}\n')
            else:
                fp.write('DUPLICATE '
                         f'{TTRD.duplicate} '
                         f'{err_pos[0]}:{err_pos[1]}\n')
    else:
        err_pos = STTD.last_char_pos
        fp.write(f'INCORRECT {err_pos[0]}:{err_pos[1]}\n')
