from main import load_data, validate_schema

file = load_data("error.yaml")
validate_schema(file, "schema.json")
