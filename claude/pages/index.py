import reflex as rx
from ..views.sidebar import sidebar
from ..views.mobile_ui import mobile_ui
from ..components.options_ui import mobile_header
from ..backend.generation import GeneratorState, CopyLocalState, copy_script
from .. import styles


def _upscale_button() -> rx.Component:
    return rx.cond(
        ~GeneratorState.is_upscaling,  # The ~ operator is a logical NOT operator that negates the boolean valueatorState.is_upscaling
        rx.button(
            rx.icon("scaling", size=20),
            "Upscale",
            **styles.button_props,
            on_click=print("upscale"),
        ),
        rx.button(
            rx.spinner(size="3"),
            "Cancel",
            **styles.button_props,
            color_scheme="tomato",
            on_click=print("cancel"),
        ),
    )


def _download_button():
    return rx.cond(
        GeneratorState.is_downloading,
        rx.icon_button(
            rx.spinner(size="3"),
            **styles.button_props,
            color_scheme="blue",
        ),
        rx.icon_button(
            rx.icon("download", size=20),
            **styles.button_props,
            color_scheme="gray",
            on_click=print("download"),
        ),
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
            on_click=[copy_script(), GeneratorState.copy_image],
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
                    _upscale_button(),
                    _download_button(),
                    _copy_button(),
                    justify="end",
                    align="center",
                    width="100%",
                ),
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
        width="100%",
        height="100%",
        bg=rx.color("gray", 1),
    )
