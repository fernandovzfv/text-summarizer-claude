import reflex as rx
from ..views.sidebar import sidebar
from ..views.mobile_ui import mobile_ui
from ..components.options_ui import mobile_header
from ..backend.generation import SummaryState, CopyLocalState, copy_script
from .. import styles


def _download_button():
    return rx.icon_button(
        rx.icon("download", size=20),
        **styles.button_props,
        color_scheme="gray",
        on_click=SummaryState.download_text,
    )


def _response_text():
    return rx.box(
        rx.text(
            SummaryState.generated_text,
            size="3",
        ),
        width="100%",
        height="100%",
        display="flex",
        align_items="center",
        justify_content="center",
        border=styles.border,
        bg=rx.color("gray", 2),
        padding="1em",
    )


def _copy_button():
    return rx.cond(
        CopyLocalState.value,
        rx.tooltip(
            rx.icon_button(
                rx.icon("clipboard-check", size=20),
                **styles.button_props,
                color_scheme="green",
            ),
            content="Copied",
            open=CopyLocalState.value,
            side="top",
        ),
        rx.icon_button(
            rx.icon("clipboard", size=20),
            **styles.button_props,
            color_scheme="gray",
            on_click=[copy_script(), SummaryState.copy_text],
        ),
    )


@rx.page(
    "/",
    title="Text Summarizer - Reflex",
    description="Generate a text summarize using AI with Reflex",
)
def index():
    return rx.flex(
        CopyLocalState,
        sidebar(),
        mobile_header(),
        rx.center(
            rx.vstack(
                rx.hstack(
                    _download_button(),
                    _copy_button(),
                    justify="end",
                    align="center",
                    width="100%",
                ),
                _response_text(),
                max_width=styles.content_max_width,
                height="100%",
                align="center",
                id="image-ui",
            ),
            width="100%",
            height="100%",
            padding=["1em", "1em", "1em", "3em"],
        ),
        mobile_ui(),
        flex_direction=["column", "column", "column", "row"],
        position="relative",
        width="85%",
        height="100%",
        bg=rx.color("gray", 1),
        margin="0 auto",  # Add margin auto to center horizontally
        justify_content="center",  # Center flex items horizontally
    )
