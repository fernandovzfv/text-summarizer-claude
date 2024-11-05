import reflex as rx
from .. import styles
from ..components.options_ui import prompt_input, size_selector, generate_button
from ..backend.generation import SummaryState


def _response_text():
    return rx.text(SummaryState.generated_text, size="3")


def mobile_ui():
    return rx.box(
        rx.vstack(
            rx.vstack(
                prompt_input(),
                size_selector(),
                width="100%",
                height="100%",
                align_items="flex-start",
                padding="1em",
                spacing="6",
            ),
            generate_button(),
            # _response_text(),
            width="100%",
            spacing="0",
        ),
        display=["block", "block", "block", "none"],
        width="100%",
        height="100%",
        bg=rx.color("gray", 2),
        border_top=styles.border,
    )
