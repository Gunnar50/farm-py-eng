import json
import pathlib
from typing import Any

data_path = pathlib.Path('data/config').resolve()
game_mappings_path = data_path / 'game_mappings.json'
editor_mappings_path = data_path / 'level_editor_mappings.json'
output_path = pathlib.Path('src/shared/key_mappings.py')


def load_json(file_path):
  with open(file_path, 'r') as f:
    return json.load(f)


# Function to generate enum class from JSON mapping
def generate_class(class_name: str, key_mapping: list[dict[str, Any]]):
  lines = [f'class {class_name}(MappingBase):']
  for mapping in key_mapping:
    label = mapping.get('label')
    if label is None:
      print('WARNING: Mapping does not have "label" attribute. Skipping...')
      continue
    # Enum member name in uppercase, value as the original key
    lines.append(f"  {label.upper()} = '{label.lower()}'")
  return '\n'.join(lines)


def main():
  game_mapping = load_json(game_mappings_path)
  editor_mapping = load_json(editor_mappings_path)

  # Generate the enum classes as a string
  game_mapping_class = generate_class('GameMapping', game_mapping.get('config'))
  editor_mapping_class = generate_class('EditorMapping',
                                        editor_mapping.get('config'))
  base_class = 'class MappingBase(enum.Enum):\n  pass'

  updated_content = '\n'.join([
      '# Auto generated from config files',
      '# Do not modify this file manually, instead update the mappings config file',
      '# Located at: data/config/*.json',
      'import enum',
  ])
  updated_content += f'\n\n\n{base_class}\n'
  updated_content += f'\n\n{game_mapping_class}\n'
  updated_content += f'\n\n{editor_mapping_class}\n'

  output_path.parent.mkdir(parents=True, exist_ok=True)
  with open(output_path, 'w') as f:
    f.write(updated_content)

  print(f'Key mappings classes created in {output_path}')


if __name__ == '__main__':
  main()
