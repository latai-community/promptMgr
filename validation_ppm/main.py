import json
import yaml
from jsonschema import validate, ValidationError


# Function to load data via file
def load_data(file_url: str) -> dict | None:
    """
    Loads a YAML file.

    Args:
        file_url: Path to the YAML file.

    Returns:
        Parsed content, or None if parsing fails.
    """
    try:
        with open(file_url, "r") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print("❌ The file is not a valid YAML.")
        print(e)


# Function to validate a schema
def validate_schema(ppm_config: dict, schema_url: str) -> None:
    """
    Validates a config against a JSON schema.

    Args:
        ppm_config: Parsed YAML content.
        schema_url: Path to the JSON schema file.
    """
    try:
        with open(schema_url, "r") as f:
            loaded_schema = json.load(f)
    except json.JSONDecodeError as e:
        print("❌ The schema file is not valid JSON.")
        print(e)
        return

    try:
        validate(instance=ppm_config, schema=loaded_schema)
        print("✅ ppm.yaml is valid")
    except ValidationError as e:
        field = ".".join([str(x) for x in e.path])
        print(f"❌ Error in field '{field}': {e.message}")
