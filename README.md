# P_A_project_2_Tic_Tac_Toe
Python Academy project 2 - Tic Tac Toe

Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač).

Program bude obsahovat:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
Ukázka kódu2
ZKOPÍROVAT KÓD
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...
Program pozdraví uživatele
Vypíše v krátkosti pravidla hry
Zobrazí hrací plochu
Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.
