"""Download the ONS Design System Jinja templates into the app.

Usage: uv run python scripts/update_design_system.py <version>

The script gets templates.zip from the GitHub release of the given version.
It copies only the macros and the page layout. It doesn't copy the examples,
the tests, the SCSS or the JavaScript, because the app gets the CSS and the
JavaScript from the ONS CDN.
"""

import io
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

RELEASE_URL = "https://github.com/ONSdigital/design-system/releases/download/{version}/templates.zip"
TARGET = Path(__file__).resolve().parent.parent / "survey" / "design_system"


def wanted(name: str) -> bool:
    filename = name.rsplit("/", 1)[-1]
    return (
        name.startswith("templates/")
        and filename.endswith(".njk")
        and not filename.startswith("example-")
    )


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    version = sys.argv[1]

    with urllib.request.urlopen(RELEASE_URL.format(version=version)) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))

    shutil.rmtree(TARGET, ignore_errors=True)
    for name in filter(wanted, archive.namelist()):
        path = TARGET / name.removeprefix("templates/")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(archive.read(name))

    print(f"Design System {version} templates are in {TARGET}")


if __name__ == "__main__":
    main()
