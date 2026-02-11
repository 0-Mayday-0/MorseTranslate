
from abc import ABC
import string
from icecream import ic

class Character(ABC):
    def __init__(self, morse: str, alpha: str) -> None:
        self._morse = morse
        self._alpha = alpha

    def to_alpha(self):
        pass

    def to_morse(self):
        pass

class MorseCharacter(Character):
    def __init__(self, morse: str, alpha: str) -> None:
        super().__init__(morse, alpha)

    def __str__(self) -> str:
        return self._morse

    def __repr__(self) -> str:
        return f'MC({self._morse}, {self._alpha})'

    @property
    def to_alpha(self) -> str:
        return self._alpha

    @property
    def to_morse(self) -> str:
        return self._morse



class Translator:
    def __init__(self, morse: str = '', alpha: str = '') -> None:
        self._alpha: list[str] = list(string.ascii_uppercase)
        self._alpha.append('/')
        self._alpha.append(' ')
        self._alpha.append('')
        self._morse: list[str] = ['.-', '-...', '-.-.', '-..', '.', '..-.',
                                  '--.', '....', '..', '.---', '-.-', '.-..',
                                  '--', '-.', '---', '.--.', '--.-', '.-.',
                                  '...', '-', '..-', '...-', '.--', '-..-',
                                  '-.--', '--..', '/', ' ', '']

        self._alpha_to_morse: dict[str, MorseCharacter] = {a: MorseCharacter(m, a) for a, m in zip(self._alpha, self._morse)}
        self._morse_to_alpha: dict[str, MorseCharacter] = {m: MorseCharacter(m, a) for a, m in zip(self._alpha, self._morse)}

        ic(self._alpha_to_morse)
        ic(self._morse_to_alpha)

        self.morse = morse
        self.alpha = alpha

    def parse_morse(self) -> list[str]:
        parsed: list[str] = []
        current_character: list[str] = []

        for i, v in enumerate(self.morse):
            if v != '/' and v != ' ':
                current_character.append(v)

            elif v == ' ':
                parsed.append(''.join(current_character))
                parsed.append(v)
                current_character.clear()

            else:
                parsed.append(''.join(current_character))
                current_character.clear()

        parsed.append(''.join(current_character))

        return parsed


    def to_alpha(self) -> str:
        try:
            return ''.join([self._morse_to_alpha[k].to_alpha for k in self.parse_morse()])

        except KeyError as e:
            print(f"ERROR: Invalid character '{e.args[0]}'")
            return ''


    def to_morse(self) -> str:
        try:
            return ''.join([f'{self._alpha_to_morse[k.upper()].to_morse}/' for k in self.alpha])

        except KeyError as e:
            print(f"ERROR: Invalid character '{e.args[0]}'")
            return ''


def main() -> None:
    test: Translator = Translator(alpha="Hello world")

    ic(test.to_morse())

if __name__ == '__main__':
    main()