from pathlib import Path

from flask import Flask
from jinja2 import ChainableUndefined, ChoiceLoader, FileSystemLoader

DESIGN_SYSTEM_TEMPLATES = Path(__file__).parent / "design_system"


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)
    if config:
        app.config.update(config)

    # The app's own templates come first. Then Jinja looks in the
    # ONS Design System templates, for example "components/button/_macro.njk".
    app.jinja_loader = ChoiceLoader(
        [app.jinja_loader, FileSystemLoader(DESIGN_SYSTEM_TEMPLATES)]
    )
    # The Design System macros read optional parameters that can be missing,
    # for example "params.button.url". ChainableUndefined lets them do this.
    app.jinja_env.undefined = ChainableUndefined
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    from survey import routes

    app.register_blueprint(routes.bp)

    return app
