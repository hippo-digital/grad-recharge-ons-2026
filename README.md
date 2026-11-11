# ONS Well-being Survey

This is a starter template for the ONS Well-being Survey project. It is a small Flask app. It uses the page layout of the [ONS Design System](https://service-manual.ons.gov.uk/design-system).

The template contains:

- A Flask app factory.
- The ONS Design System page layout, with a header, a footer and one example page.
- One test.

Change this README as you build your app. A new developer must be able to use it to install, run and test the app.

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/). uv installs the correct Python version for you.
- An internet connection. The pages get the ONS CSS, JavaScript and fonts from the ONS CDN.

## Install

```sh
uv sync
```

## Run the app

```sh
uv run flask --app survey run --debug
```

Open <http://127.0.0.1:5000> in a browser.

The `--debug` option reloads the app when you change the code. Use it only on your computer.

## Run the tests

```sh
uv run pytest
```

## Project structure

| Path | Contents |
|---|---|
| `survey/__init__.py` | The app factory, `create_app()`. |
| `survey/routes.py` | The pages of the app. |
| `survey/templates/base.html` | The base layout. All pages extend it. |
| `survey/templates/index.html` | The example page. |
| `survey/design_system/` | The ONS Design System templates. Don't edit these files. |
| `scripts/update_design_system.py` | Downloads a different version of the Design System templates. |
| `tests/` | The tests. `conftest.py` has the `app` and `client` fixtures. |
| `.github/workflows/` | Put your GitHub Actions workflows here. |

## Add a page

1. Add a route to `survey/routes.py`.
2. Add a template to `survey/templates/`. The template extends `base.html`, sets `page_title` and puts the page content in the `main` block.
3. Add a test to `tests/`.

## Use the ONS Design System

The Design System components are Jinja macros. Each component has a page in the [Design System documentation](https://service-manual.ons.gov.uk/design-system), with examples. There are also pages which document [patterns](https://service-manual.ons.gov.uk/design-system/patterns) of how components can be used together.

To use a component, import its macro from `components/<name>/_macro.njk`. For example, [`index.html`](survey/templates/index.html) uses the [panel](https://service-manual.ons.gov.uk/design-system/components/panel) component:

```jinja
{% from "components/panel/_macro.njk" import onsPanel %}

{% call onsPanel({ "variant": "info" }) %}
    <p>Some information.</p>
{% endcall %}
```

The documentation shows the examples in Nunjucks. The syntax is almost the same as Jinja, so you can usually copy the examples.

### Change the Design System version

The app uses Design System version 73.13.1. The version is in two places: the templates in `survey/design_system/`, and the CSS and JavaScript from the CDN. The templates set the CDN version, so the two versions are always the same.

To change the version, run this command with a version from the [Design System releases](https://github.com/ONSdigital/design-system/releases):

```sh
uv run python scripts/update_design_system.py <version>
```

Then run the tests and look at the pages. A new version can change the macro parameters.
