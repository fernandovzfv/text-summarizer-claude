import reflex as rx
from .. import styles
from ..backend.options import OptionsState
from ..backend.generation import SummaryState


def sidebar_header() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg", height="1.15em", width="auto"),
                rx.image(src="/reflex_white.svg", height="1.15em", width="auto"),
            ),
            href="https://reflex.dev",
            is_external=True,
            padding="0",
        ),
        rx.spacer(),
        rx.color_mode.button(
            style={"padding": "0", "height": "1.15em", "width": "1.15em"},
        ),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def mobile_header() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg", height="1em", width="auto"),
                rx.image(src="/reflex_white.svg", height="1em", width="auto"),
            ),
            href="https://reflex.dev",
            is_external=True,
            padding="0",
        ),
        rx.spacer(),
        rx.color_mode.button(
            style={"padding": "0", "height": "1.25em", "width": "1.25em"},
        ),
        display=["flex", "flex", "flex", "none"],
        justify="end",
        id="mobile-header",
        border_bottom=styles.border,
        align="center",
        width="100%",
        padding="1em",
    )


def prompt_input() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("type", size=17, color=rx.color("green", 9)),
            rx.text("SUMMARIZER", size="3"),
            rx.spacer(),
            rx.hstack(
                rx.cond(
                    OptionsState.text,
                    rx.icon(
                        "eraser",
                        size=20,
                        color=rx.color("gray", 10),
                        cursor="pointer",
                        _hover={"opacity": "0.8"},
                        on_click=OptionsState.setvar("text", ""),
                    ),
                ),
                rx.tooltip(
                    rx.box(  # Without the box the tooltip is not visible
                        rx.icon(
                            "dices",
                            size=20,
                            color=rx.color("gray", 10),
                            cursor="pointer",
                            _hover={"opacity": "0.8"},
                            on_click=OptionsState.randomize_text,
                        ),
                    ),
                    content="Randomize text",
                ),
                spacing="4",
                align="center",
            ),
            spacing="2",
            align="center",
            width="100%",
        ),
        rx.text_area(
            placeholder="Insert text",
            width="100%",
            size="3",
            resize="vertical",
            value=OptionsState.text,
            on_change=OptionsState.set_text,
        ),
        width="100%",
    )


def size_selector() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("scan", size=17, color=rx.color("orange", 9)),
            rx.text("Words", size="3"),
            spacing="2",
            align="center",
            width="100%",
        ),
        rx.vstack(
            rx.slider(
                min=5,
                max=50,
                step=5,
                size="1",
                default_value=10,
                on_change=OptionsState.set_summary_length,
            ),
            rx.hstack(
                rx.icon("rectangle-horizontal", size=22, color=rx.color("gray", 9)),
                rx.text(
                    OptionsState.words_str,
                    size="2",
                    style={
                        "transition": "opacity 0.15s ease-out, visibility 0.15s ease-out",
                        "visibility": "visible",
                        "opacity": "1",
                    },
                ),
                rx.icon("rectangle-vertical", size=22, color=rx.color("gray", 9)),
                position="relative",
                justify="between",
                align="center",
                width="100%",
            ),
            width="100%",
        ),
        width="100%",
    )


def generate_button() -> rx.Component:
    return rx.box(
        rx.button(
            rx.icon("sparkles", size=17),
            "Generate",
            size="3",
            cursor="pointer",
            width="100%",
            on_click=SummaryState.generate_text,
        ),
        position="sticky",
        bottom="0",
        padding="1em",
        bg=rx.color("gray", 2),
        border_top=styles.border,
        width="100%",
    )
