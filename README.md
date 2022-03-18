# BlukalkaLaba4_5
This is a repository for a game.
Module main.py is a cycle of the game, and game.py contains classes for main module.

The plot of the game is to visit rooms, meet enemies, collect items that will help to fight all enemies.
Supports inputs from a user, with given possible options.

Gives user information about the current state of affairs by printing.

Written classes in game.py:
    Room -  supports linking between rooms and giving the room info;                
    Character - basic class for living creatures to be inherited;               
    Enemy(Character) - has weakness, can talk and fight;            
    Friend(Character) -  shell for friendly classes;                
    Item - contains info about the item.                

A game can look like this:                  


![Знімок екрана 2022-03-18 о 12 44 48](https://user-images.githubusercontent.com/92575094/158989149-41ad6665-593b-4996-9ad5-ef2c8a0a53a6.png)

