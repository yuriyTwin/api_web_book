import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_DIR = (
    Path(__file__).resolve().parent.parent
    / "schemas"
)


def load_schema(schema_name: str) -> dict:
    """
    Load JSON schema by name.

    Example:
        load_schema("getPlayList")
    """

    schema_file = SCHEMA_DIR / f"{schema_name}.schema.json"

    with schema_file.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_json(data: dict, schema_name: str):
    """
    Validate JSON response against schema.
    """

    schema = load_schema(schema_name)

    validator = Draft202012Validator(schema)

    errors = sorted(
        validator.iter_errors(data),
        key=lambda e: list(e.path)
    )

    if errors:

        message = "\n".join(
            f"{'/'.join(map(str, error.path))}: {error.message}"
            for error in errors
        )

        raise AssertionError(
            f"JSON Schema validation failed:\n\n{message}"
        )
