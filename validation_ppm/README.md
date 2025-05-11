# validation_ppm

`validation_ppm` is a set of Python scripts for testing and validating configurations based on a YAML file against a JSON schema.

## Requirements

Before running the scripts, make sure you have Python installed. This project also requires some dependencies, which are listed in the `requirements.txt` file.

### Steps to run the project 

1. **Clone the repository**:
   ```bash
   git clone <REPOSITORY_URL>
   cd validation_ppm
   ```

2. **Create a virtual environment**:
   If you don't have a virtual environment set up, you can create one with:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the validation

The `main.py` file contains two functions: `load_data` and `validate_schema`.

- **`load_data(file_url: str) -> dict | None`**: This function loads a YAML file and returns its parsed content. If the file cannot be parsed, it returns `None`.
  
- **`validate_schema(ppm_config: dict, schema_url: str) -> None`**: This function validates the parsed YAML configuration against a JSON schema.

### Example

The `test.py` file demonstrates how to use the functions in `main.py`:

```python
from main import load_data, validate_schema

file = load_data("error.yaml")
validate_schema(file, "schema.json")
```

This example loads the `error.yaml` file, then validates it against the `schema.json` schema.

### Notes

- Ensure that the `error.yaml` and `schema.json` files are correctly formatted and located in the appropriate paths.
