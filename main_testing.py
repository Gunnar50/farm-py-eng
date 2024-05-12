from scripts import PyEng


class Game(PyEng.Game):
    def load_data(self):
        PyEng.init(
            window_size=(960, 630),
            caption="My Specific Game",
            bg_colour=(100, 0, 0),
            assets_folder="assets/data",
            game_type="isometric",
        )

        print(self.components_manager.get_item("system", "Assets").assets)

    def game_loop(self):
        self.components_manager.get_item("system", "Window").clear()
        dt = self.components_manager.get_item("system", "Window").get_dt()
        self.components_manager.update()

        # render.render




Game().run()


