import reflex as rx
import random
from ..components.paragraph_list import paragraph_list


class OptionsState(rx.State):
    summary_length: int = 10
    text: str = ""

    def set_summary_length(self, value: int):
        self.summary_length = value[0]

    def randomize_text(self):
        self.text = random.choice(paragraph_list)

    @rx.var
    def words_str(self) -> str:
        return f"Create a summary of {self.summary_length} words"
