import sys
from blessings import Terminal
import random
import string
from time import sleep  # <- boy, does this sound tempting a.t.m. >= <= <-> < - > => <=> 

from pynput.keyboard import Listener


class GameTyper:
    def __init__(self, length_of_main_string):
        self.game_string = ''.join(self.__generate_char() for _ in range(length_of_main_string))
        self.score = 0
        self.__t = Terminal()
        self.__rewrite_correct(False)

    @staticmethod
    def __generate_char():
        letters = string.ascii_lowercase
        letters += ' '
        return random.choice(string.ascii_lowercase)

    def game_step(self, key):
        
        if key == self.game_string[0]:
            self.__rewrite_correct()
            self.score += 1
        else:
            self.__rewrite_incorrect()
            self.score -= 2

    def __rewrite_incorrect(self, with_up=True):
        # print(self.__t.clear())
            
        if with_up:
            print(self.__t.move_up*2, end="")
        print(f'Score: {self.score}')
        print(self.__t.red(self.game_string[0]) + self.game_string[1:])

    def __rewrite_correct(self, with_up=True):
        # print(self.__t.clear())
        self.game_string = self.game_string[1:] + self.__generate_char()
        if with_up:
            print(self.__t.move_up*2, end="")
        print(f'Score: {self.score}')
        print(self.game_string)


if __name__ == "__main__":
    t = Terminal()
