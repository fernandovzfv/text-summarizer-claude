import reflex as rx
from . import styles

# Import pages explicitly
from .pages.index import index

app = rx.App(
    routes=[index],
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    html_lang="en",
    html_custom_attrs={"className": "!scroll-smooth"},
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        scaling="100%",
        radius="none",
        accent_color="violet",
    ),
)
