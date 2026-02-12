from morseobj import Translator
from abc import ABC, abstractmethod
from collections.abc import Callable

class Menu(ABC):
    def __init__(self) -> None:
        self.valid_commands: dict[str, Callable]

    @abstractmethod
    def mainloop(self) -> None:
        pass


class AlphaToMorse(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.valid_commands: dict[str, Callable] = {'': lambda: None}

    def mainloop(self) -> None:
        user_input: str = ' '

        while user_input != '':
            user_input = input("Enter an alphabetic string, or leave empty to go back: ").upper()

            try:
                assert user_input in self.valid_commands or user_input.replace(' ', '').isalpha()
                trans_obj: Translator = Translator(alpha=user_input)
                print(trans_obj.to_morse())

            except AssertionError:
                print("Error: Invalid character found in string, use only English letters.")


class MorseToAlpha(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.valid_commands: dict[str, Callable] = {'': lambda: None}


    def mainloop(self) -> None:
        user_input: str = ' '

        while user_input != '':
            user_input = input("Enter a morse string, separating characters with a /. Leave blank to go back: ")

            trans_obj: Translator = Translator(morse=user_input)
            print(trans_obj.to_alpha())


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.valid_commands: dict[str, Callable] = {'a': self.trans_alpha, 'm': self.trans_morse, '': lambda: None}

    def mainloop(self) -> None:
        user_input: str = 'x'

        while user_input != '':
            user_input = input("[A]lpha to morse\n[M]orse to alpha\n[]Quit\n\nCommand: ").lower()

            try:
                assert user_input in self.valid_commands.keys()
                self.valid_commands[user_input]()

            except AssertionError:
                print("Command not found.")

    def trans_alpha(self):
        ATM_Menu: AlphaToMorse = AlphaToMorse()

        ATM_Menu.mainloop()

    def trans_morse(self):
        MTA_Menu: MorseToAlpha = MorseToAlpha()

        MTA_Menu.mainloop()

def main() -> None:
    m_menu: MainMenu = MainMenu()
    m_menu.mainloop()

if __name__ == '__main__':
    main()