import pygame
from ..element_manager.components import SystemComponents
import os
import json


class Assets(SystemComponents):
    def __init__(self, assets_folder):
        SystemComponents.__init__(self)
        self.assets = {}
        self.load_assets(assets_folder)

    def load_assets(self, assets_folder):
        for file in os.listdir(assets_folder):
            if file.endswith(".json"):
                with open(os.path.join(assets_folder, file)) as f:
                    json_data = json.load(f)
                    for asset_name, asset_data in json_data.items():
                        if isinstance(asset_data["image"], str):
                            asset_data["image"] = [asset_data["image"]]
                        loaded_img = [pygame.image.load(img) for img in asset_data["image"]]
                        asset_data["image"] = loaded_img
                        self.assets[asset_name] = asset_data
