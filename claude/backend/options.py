import reflex as rx
import random
from ..components.paragraph_list import paragraph_list


class OptionsState(rx.State):
    selected_dimensions: int = 50
    hover: bool = False
    selected_style: str = "Cinematic"
    advanced_options_open: bool = False
    # Generation options
    prompt: str = ""
    negative_prompt: str = (
        "deformed, distorted, disfigured, poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, mutated hands and fingers, disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, text, watermark, signature"
    )
    num_outputs: int = 1
    seed: int = 0
    steps: int = 4
    scheduler: str = "K_EULER"
    guidance_scale: float = 0

    def set_tick(self, value: int):
        self.slider_tick = value[0]
        self.selected_dimensions = self.dimensions[self.slider_tick]

    def set_hover(self, value: bool):
        self.hover = value

    def set_num_outputs(self, value: int):
        self.num_outputs = value[0]

    def set_steps(self, value: int):
        self.steps = value[0]

    def set_guidance_scale(self, value: float):
        self.guidance_scale = value[0]

    def randomize_text(self):
        self.prompt = random.choice(paragraph_list)

    @rx.var
    def dimensions_str(self) -> str:
        width, height = self.selected_dimensions
        return f"{width} × {height}"
