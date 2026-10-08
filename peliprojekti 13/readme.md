Vegetable Farm (Growing seeds)
A simple Python farming game where you buy seeds, plant vegetables, water them, harvest them, and sell them to earn money.
Features
Buy carrot, tomato, and potato seeds
Plant seeds in your garden
Water vegetables to increase their growth
Check vegetable growth
Harvest fully grown vegetables
Sell harvested vegetables
View your inventory
Check your balance
Save the game
Win when your balance reaches €50
Requirements
You need:

How to Run
Open a terminal in the project folder and run:
python main.py

On some systems, you may need:
python3 main.py

How to Play
When the game starts, enter your name and age.
You start with €20.

Your goal is to reach €50.

first intro.txt and instructions.txt will display first

Main Menu
1.Buy seed
2.Plant
3.Water
4.Check growth
5.Harvest
6.Sell
7.Inventory
8.Balance
9.Save
10.Exit

1.Buy Seed
Choose a seed from the shop:
Seed    Price
Carrot  €3
Tomato  €5
Potato  €4

The seed is added to your inventory and the price is removed from your balance.
2.Plant
Choose one of the seeds in your inventory.
Only one vegetable can grow in the garden at a time.

3.Water
Watering increases the vegetable's growth by 25%.
For example:

Growth: 25%

After four successful waterings:
Growth: 100%

The vegetable is then ready to harvest.
4.Check Growth
Shows the current growth of the vegetable.
Example:

Carrot growth: 50%
Keep watering.

5.Harvest
A vegetable can only be harvested when it reaches 100% growth.
After harvesting, the vegetable is placed in your inventory.

6.Sell
Sell your harvested vegetables to receive money.
The selling price is twice the original seed price:

Vegetable   Selling Price
Carrot  €6
Tomato  €10
Potato  €8

7.Inventory
Displays all seeds and vegetables currently in your inventory.
8.Balance
Displays your current amount of money.
Example:

Balance: €32

9.Save
Saves basic game information to:
save1.json

10.Exit
Closes the game.
Winning
You win when your balance reaches €50 or more.
The game displays:

If you have save game, in the next game will ask your name and ask you resume the previous game or not.

if yes, you previous game reloaded and continue.

if no, start new game.

you won!
You reached €50!

