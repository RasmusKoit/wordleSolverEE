from colorama import Fore as Color, Style

WHITE = Color.WHITE
YELLOW = Color.YELLOW
GREEN = Color.GREEN
RST = Style.RESET_ALL


class Word:
    name: str
    frequency: int
    colored: str
    length: int

    def __init__(self, name: str, frequency: int = 0, feedback: str = ""):
        self.name = name
        self.frequency = frequency
        self.length = len(name)
        self.color(feedback)

    def description(self):
        if self.frequency is None:
            return f"{self.name}: length: {self.length}"
        else:
            return f"{self.name}: length: {self.length}, frequency: {self.frequency}"

    def set_frequency(self, freq: int):
        self.frequency = freq

    def get_name(self):
        return self.name

    def color(self, feedback: str):
        colored_output = ""
        colored_output += Style.RESET_ALL
        if len(feedback) > 1:
            for i in range(len(self.name)):
                if feedback[i] == "w":
                    colored_output += self.name[i] + RST
                elif feedback[i] == "y":
                    colored_output += YELLOW + self.name[i] + RST
                elif feedback[i] == "g":
                    colored_output += GREEN + self.name[i] + RST
                else:
                    colored_output += self.name[i] + RST
        else:
            colored_output += self.name
        colored_output += Style.RESET_ALL
        self.colored = colored_output
