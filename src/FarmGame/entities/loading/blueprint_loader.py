import pathlib
from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.PyEng.utils.io import load_json
from src.shared.hash_registry import HashRegistry, Id

# Create pydantic model for the blueprint file info.
# use that to load the reader and the blueprint settings


class BlueprintLoader:

  def __init__(self, component_types: HashRegistry[ComponentType]) -> None:
    self.component_types = component_types

  def load_blueprint(self, folder: pathlib.Path) -> Blueprint:
    id = Id.gen(folder.name)
    info_file = self.get_info_file(folder)
    return self.load_info_file(id, folder, info_file)

  def load_info_file(self, id: 'Id', entity_folder: pathlib.Path,
                     info_file: pathlib.Path) -> Blueprint:
    reader = load_json(info_file)
    save_enabled = self.load_blueprint_settings(reader)
    components = CompBlueprintBundle(entity_folder)
    for component_id, component_data in reader.items():
      components.add_component(
          self.load_component(component_id, component_data, components))
    return Blueprint(id, save_enabled, components.get_components())

  def load_component(self, component_id: str, component_data: dict,
                     components: CompBlueprintBundle) -> ComponentBlueprint:
    loader = self.component_types.get(component_id).get_loader()
    if loader is None:
      raise ProgramError(
          f'Tried to load unknown component type: {component_id}')
    return loader.load(component_data, components)

  def load_blueprint_settings(self, reader: dict) -> bool:
    return reader.get('save', False)

  def get_info_file(self, folder: pathlib.Path) -> pathlib.Path:
    for file in folder.iterdir():
      if file.name.startswith(self.ENTITY_INFO_FILE):
        return file
    raise ProgramError(f'No entity info file found for {folder.name}')
