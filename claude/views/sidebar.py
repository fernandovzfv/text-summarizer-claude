import reflex as rx
from .. import styles
from ..components.options_ui import (
    sidebar_header,
    prompt_input,
    size_selector,
    generate_button,
)


def sidebar():
    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.flex(
                rx.vstack(
                    prompt_input(),
                    rx.spacer(),
                    rx.divider(),
                    size_selector(),
                    width="100%",
                    overflow_y="auto",
                    align="start",
                    padding="1em",
                    spacing="6",
                ),
                overflow_y="auto",
                flex="1",
                height="100%",
                width="100%",
            ),
            generate_button(),
            width="100%",
            height="100%",
            spacing="0",
        ),
        display=["none", "none", "none", "block"],
        width=styles.sidebar_width,
        height="100vh",
        position="sticky",
        top="0px",
        left="0px",
        bg=styles.sidebar_bg,
        border_right=styles.border,
    )
