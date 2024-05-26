from scripts import PyEng


class Game(PyEng.Game):
    """Main Game Class"""
    def load_data(self):
        PyEng.init(
            window_size=(960, 630),
            caption="My Specific Game",
            bg_colour=(100, 0, 0),
            assets_folder="assets/data"
        )
        for key, value in self.components_manager.items():
            setattr(self, key, value)
            self.__dict__[key] = value

        # print(self.assets)

    def game_loop(self):
        
        # updates
        dt = self.window.get_dt()
        self.components_manager.update()
        
        self.window.clear()
        # this is where the game should render
        # render.render
        self.window.swap_buffers()




if __name__ == "__main__":
    Game().run()

