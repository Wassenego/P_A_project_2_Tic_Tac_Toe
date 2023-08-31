# P_A_project_2_Tic_Tac_Toe
Python Academy project 2 - Tic Tac Toe - dobrovolný druhý (třetí celkem) projekt na Python akademii na Engeto.

## Popis projektu
V tomto projektu jsme měli za úkol vytvořit hru Tic Tac Toe neboli piškvorky. Hrát proti sobě měli mít možnost jak dva hráči, tak hráč proti počítač. Nechal jsem i variantu hry dvou počítačů proti sobě. Zvolená velikost mřížky byly 3x3 pole. 

## Instalace knihoven
Pro hru byly použity jen built-in knihovny, nebylo potřeba tvořit virtuální prostředí ani soubour requirements.txt

## Spuštění projektu
Spuštění projektu lze bez nutnosti vkládaní argumentů.

## Program obsahuje
- Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. 

- Program nejprve pozdraví uživatele.
    ```
    Welcome to Tic Tac Toe
    =========================
    ```
- Vypíše v krátkosti pravidla hry.
    ```
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row
    ==============================================
    ```
- Nechá vybrat, jaká kombinace hráčů bude zvolena (člověk - člověk, člověk x počítač, počítač x počítač). Volba se zadá vložením jména (hráč), případně odentrováním prázdného řádku (počítač).  
- Zobrazí hrací plochu včetně nápovědy očíslování políček.
    ```
    ===============================
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    ===============================
    ``` 
- Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene. V případě počítače je vše automatické. 
    - Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní. 
    - Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní. 
    - Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené. 
- Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy. 
    ```
    ==============================================================
    David | Please enter your move number (digit 1-9):4
    ==============================================================
    +---+---+---+
    |   |   |   |
    +---+---+---+
    | X | O | O |
    +---+---+---+
    | X |   |   |
    +---+---+---+
    ==============================================================   
    Marek | Please enter your move number (digit 1-9):1
    ==============================================================
    +---+---+---+
    | O |   |   |
    +---+---+---+
    | X | O | O |
    +---+---+---+
    | X |   |   |
    +---+---+---+
    ==============================================================
    David | Please enter your move number (digit 1-9):
    ```
- Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří.
    ```
    ==============================================================
    Congratulations, 'Marek' WON!
    ==============================================================
    ```
- Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.
    ```
    ==============================================================
    Nobody was able to place three marks in the row. It's a draw!
    ==============================================================  
    ```
