# pronto-coding

This is a project for Pronto's software coding task. Waven Monopoly's solution.

To run the code:
Type in terminal and in the pronto-coding directory:
python3 solution.py *board json* *rolls json*

For example: 
python3 solution.py board.json rolls_1.json


I did a lot of manual testing with pen and paper but I did not use any automatic testing.

Some initiatives that I took for the project:
- Bankruptcy is when the players' money <= 0
- Winner and money owned by players at last were after deduction of the rent price.






**TC 1:**
python3 solution.py board.json rolls_1.json

**Output 1:**

Winner is  Peter

Money owned :  {'Peter': 38, 'Billy': 13, 'Charlotte': -2, 'Sweedal': 1}
Properties owned :  {'Peter': ['The Burvale', 'Fast Kebabs', 'Massizim', 'Gami Chicken', 'Lanzhou Beef Noodle'], 'Billy': ['The Grand Tofu', "Betty's Burgers"], 'Charlotte': [], 'Sweedal': []}
Players positions:  {'Peter': 8, 'Billy': 0, 'Charlotte': 7, 'Sweedal': 7}

**TC 2:**
python3 solution.py board.json rolls_2.json

**Output 2:**

Winner is  Charlotte

Money owned :  {'Peter': 3, 'Billy': 19, 'Charlotte': 30, 'Sweedal': -3}
Properties owned :  {'Peter': ["Betty's Burgers"], 'Billy': ['Fast Kebabs', 'The Grand Tofu', 'YOMG', 'Gami Chicken'], 'Charlotte': ['Lanzhou Beef Noodle', 'Massizim'], 'Sweedal': ['The Burvale']}
Players positions:  {'Peter': 4, 'Billy': 2, 'Charlotte': 0, 'Sweedal': 8}






Overall, this is a good challenge to ignite my coding skills. Thank you to the task master, Jeyganesh.

Best regards,

Vincent.
