import os
from game.models import Player, Enemy
from game.settings import PAPER, ROCK, SCISSORS
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_info(player: Player, enemy: Enemy, player_choice, enemy_choice) -> None:
   # clear_terminal()
   
   if player_choice == SCISSORS:
      player_choice = " SCISSORS"
   elif player_choice == PAPER:
      player_choice = " PAPER"
   elif player_choice == ROCK:
      player_choice = " ROCK"
      
   if enemy_choice == SCISSORS:
      enemy_choice = "SCISSORS"
   elif enemy_choice == PAPER:
      enemy_choice = "PAPER"
   elif enemy_choice == ROCK:
      enemy_choice = "ROCK"
    
   max_len_row = 50   
   lives = "lives"
   player_lives = lives  * player.lives
   enemy_lives = lives * enemy.lives
   spaces = " " * (42 - (len(player.name) + len("Enemy")))
   space_lives = " " * (42 - (player.lives + enemy.lives) - len("Enemy"))
   space_choice = " " * (41 - len('Enemy'))
   print(f"{player.name}{spaces}Enemy\n{player_lives}{space_lives}{enemy_lives}\n\n{player_choice}{space_choice}{enemy_choice}\n")
   
   
def center_word(word: str) -> str:
   return f"{round((50 - len(word)) / 2)}{word}{round((50 - len(word)) / 2)}"