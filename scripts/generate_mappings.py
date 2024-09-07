import json
import re
from typing import Any

json_file_path = 'assets/config/key_mappings.json'
output_file_path = 'PyEng/shared/api.py'


def load_json(file_path):
  with open(file_path, 'r') as f:
    return json.load(f)


# Function to generate enum class from JSON mapping
def generate_enum_class(class_name: str, key_mapping: list[dict[str, Any]]):
  lines = [f"class {class_name}(enum.Enum):"]
  for mapping in key_mapping:
    label = mapping.get('label')
    if label is None:
      print('WARNING: Mapping does not have "label" attribute. Skipping...')
      continue
    # Enum member name in uppercase, value as the original key
    lines.append(f"  {label.upper()} = '{label}'")
  return "\n".join(lines)


# Function to check if class already exists and remove it if found
def remove_existing_enum_class(class_name: str, content: str) -> str:
  # Regex pattern to find the class definition and its body (members)
  class_pattern = rf"(\n{{0,2}})class {class_name}\(enum\.Enum\):\n((  .+\n)+)"

  # Use re.sub to replace the class definition and its body with an empty string
  updated_content = re.sub(class_pattern, "", content, flags=re.MULTILINE)

  return updated_content


def main():
  key_mapping = load_json(json_file_path)

  # Generate the enum class code as a string
  enum_class_code = generate_enum_class("KeyMapping", key_mapping)

  # Read the current content of the output file
  with open(output_file_path, 'r') as f:
    content = f.read()

  updated_content = remove_existing_enum_class("KeyMapping", content)
  updated_content += "\n\n" + enum_class_code + "\n"

  with open(output_file_path, 'w') as f:
    f.write(updated_content)

  print(f"Enum class has been updated in {output_file_path}")


if __name__ == "__main__":
  main()
