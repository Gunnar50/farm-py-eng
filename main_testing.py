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

        print(self.components_manager["Assets"].assets)

    def game_loop(self):
        self.components_manager["Window"].clear()
        dt = self.components_manager["Window"].get_dt()
        self.components_manager.update()

        # render.render



if __name__ == "__main__":
    Game().run()


