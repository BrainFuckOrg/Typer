from pynput.keyboard import Key, Listener
from typer import GameTyper


class Game:

    def __init__(self):
        self.gamemode = 0
        self.key_acceptors = [self.choose_path, self.ingame_readkey, self.show]
        self.typer = None

    @staticmethod
    def info():
        print('welcome to the typing enchancer')

    @staticmethod
    def menu():
        print('select action:\ng - start game\ns - settings')

    @staticmethod
    def main():
        Game.info()
        Game.menu()

    @staticmethod
    def show(key):
        print('\nYou Entered {0}'.format(key))

        if key == Key.delete:
            # Stop listener
            return False

    def choose_path(self, key):
        # menu()
        try:
            key_char = key.char
            if key_char == 'g':
                self.gamemode = 1
                self.typer = GameTyper(10)
            if key_char == 's':
                pass
        except AttributeError:
            pass
        return True

    def ingame_readkey(self, key):
        try:
            key_char = key.char
            self.typer.game_step(key_char)
            if self.typer.score > 10:
                return False
            if self.typer.score < -5:
                print('ну ти й лошара')
                return False
        except AttributeError:
            pass

    def process_key(self, key):
        return self.key_acceptors[self.gamemode](key)

    @staticmethod
    def end_game(score):
        print(f"Your score is {score}, {'congratulations'if score>0 else'you sucked'}!!!")


if __name__ == "__main__":
    typer_game = Game()
    Game.menu()
    with Listener(on_release=typer_game.process_key) as listener:
        listener.join()

    Game.end_game(typer_game.typer.score)
    # print("run.\nNOW")
