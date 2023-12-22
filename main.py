import pygame
from config.game_config import *
from src.game_manager import GameManager
from src.utils.app_network import Net
from PyQt5 import QtCore, QtGui, QtWidgets
from src.components.home import Home_ui
from src.components.play_ai import Ui_frameMapAI
from src.components.play_player import Ui_frameMapPlayer

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("2D CAR RACING")

game_manager = GameManager(screen)
# setup game
game_manager.mode = 0
game_manager.map_id = "01"
game_manager.level = 0
game_manager.is_trainning = False

class HomeUI(QtWidgets.QMainWindow):
    def __init__(self, net: Net):
        super(HomeUI, self).__init__()
        self.ui = Home_ui()
        self.ui.setupUi(self)
        self.net = net
        self.mode = 0 # 0: AI, 1: Multiplayer

        # choose car
        self.ui.nextBtn.clicked.connect(self.show_green_car)
        self.ui.preBtn.clicked.connect(self.show_yellow_car)

        # choose mode
        self.ui.playWithHuman.clicked.connect(lambda: self.on_button_choose_mode(1))
        self.ui.playWithAI.clicked.connect(lambda: self.on_button_choose_mode(0))
        self.ui.playGame.clicked.connect(self.show_confirmation)
        self.ui.playGame.clicked.connect(self.close)

    def on_button_choose_mode(self, mode):
        self.mode = mode
        game_manager.mode = mode

    def show_confirmation(self):
            if self.mode == 0:
                self.openWindow_AI()
            elif self.mode == 1:
                self.openWindow_Human()

    def show_green_car(self):
        self.ui.car.setPixmap(QtGui.QPixmap(":/images/car101.png"))
        game_manager.car_id = "001"

    def show_yellow_car(self):
        self.ui.car.setPixmap(QtGui.QPixmap(":/images/car102.png"))
        game_manager.car_id = "102"

    def openWindow_AI(self):
        self.frame_map_ai.show()
    
    def openWindow_Human(self):
        self.frame_map_player.show()

class FrameMapAI(QtWidgets.QMainWindow):
    def __init__(self, net: Net):
        super(FrameMapAI, self).__init__()
        self.ui = Ui_frameMapAI()
        self.ui.setupUi(self)
        self.net = net
        self.level = 0

        self.ui.backBtn.clicked.connect(lambda: self.openWindow())
        self.ui.easyMode.clicked.connect(lambda: self.on_button_choose_level(0))
        self.ui.hardMode.clicked.connect(lambda: self.on_button_choose_level(1))
        self.ui.startBtn.clicked.connect(lambda: self.startGame())
    
    def on_button_choose_level(self, level):
        self.level = level
        game_manager.level = level

    def openWindow(self):
        self.home.show()

    def startGame(self):
        if not game_manager.is_playing:
            game_manager.start_game()

class FrameMapPlayer(QtWidgets.QMainWindow):
    def __init__(self, net: Net):
        super(FrameMapPlayer, self).__init__()
        self.ui = Ui_frameMapPlayer()
        self.ui.setupUi(self)
        self.net = net
        
        self.ui.backBtn.clicked.connect(lambda: self.openWindow())

    def openWindow(self):
        self.home.show()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    net = Net()

    home = HomeUI(net)
    frame_map_ai = FrameMapAI(net)
    frame_map_player = FrameMapPlayer(net)

    home.frame_map_ai = frame_map_ai
    home.frame_map_player = frame_map_player
    frame_map_ai.home = home
    frame_map_player.home = home

    home.show()
    sys.exit(app.exec_())

# net = Net()
# net.connect_to_server()

# net.send_to_server("0010", "dvc")
# while(True):
#     amount = net.receive_from_server()
#     if amount == 2:
#         break
# net.send_to_server()


# net.send_to_server("0011", "dvc|hello")

# Run the game
# game_manager.start_game()
# while(True):
#     pass