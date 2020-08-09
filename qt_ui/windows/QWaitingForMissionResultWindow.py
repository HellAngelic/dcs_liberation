import json
import os

from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QMovie, QIcon, QPixmap
from PySide2.QtWidgets import QLabel, QDialog, QGroupBox, QGridLayout, QPushButton, QFileDialog, QMessageBox, QTextEdit, \
    QHBoxLayout

from game.game import Event, Game
from qt_ui.windows.GameUpdateSignal import GameUpdateSignal
from userdata.debriefing import wait_for_debriefing, Debriefing
from userdata.persistency import base_path


class DebriefingFileWrittenSignal(QObject):

    instance = None
    debriefingReceived = Signal(Debriefing)

    def __init__(self):
        super(DebriefingFileWrittenSignal, self).__init__()
        DebriefingFileWrittenSignal.instance = self

    def sendDebriefing(self, debriefing: Debriefing):
        self.debriefingReceived.emit(debriefing)

    @staticmethod
    def get_instance():
        return DebriefingFileWrittenSignal.instance

DebriefingFileWrittenSignal()

class QWaitingForMissionResultWindow(QDialog):

    def __init__(self, gameEvent: Event, game: Game):
        super(QWaitingForMissionResultWindow, self).__init__()
        self.setModal(True)
        self.gameEvent = gameEvent
        self.game = game
        self.setWindowTitle("Waiting for mission completion.")
        self.setWindowIcon(QIcon("./resources/icon.png"))
        self.setMinimumHeight(570)

        self.initUi()
        DebriefingFileWrittenSignal.get_instance().debriefingReceived.connect(self.updateLayout)
        self.wait_thread = wait_for_debriefing(lambda debriefing: self.on_debriefing_udpate(debriefing), self.game)

    def initUi(self):
        self.layout = QGridLayout()

        header = QLabel(self)
        header.setGeometry(0, 0, 655, 106)
        pixmap = QPixmap("./resources/ui/conflict.png")
        header.setPixmap(pixmap)
        self.layout.addWidget(header, 0, 0)

        self.gridLayout = QGridLayout()
        TEXT = "" + \
                "<b>You are clear for takeoff</b>" + \
                "" + \
                "<h2>For Singleplayer :</h2>\n" + \
                "In DCS, open the Mission Editor, and load the file : \n" + \
                "<i>liberation_nextturn</i>\n" + \
                "<p>Then once the mission is loaded in ME, in menu \"Flight\",\n" + \
                "click on FLY Mission to launch.</p>\n" + \
                "" + \
                "<h2>For Multiplayer :</h2>" + \
                "In DCS, open the Mission Editor, and load the file : " + \
                "<i>liberation_nextturn</i>" + \
                "<p>Click on File/Save. Then exit the mission editor, and go to Multiplayer.</p>" + \
                "<p>Then host a server with the mission, and tell your friends to join !</p>" + \
                "<i>(The step in the mission editor is important, and fix a game breaking bug.)</i>" + \
                "<h2>Finishing</h2>" + \
                "<p>Once you have played the mission, click on the \"Accept Results\" button.</p>" + \
                "<p>If DCS Liberation does not detect mission end, use the manually submit button, and choose the state.json file.</p>"

        self.instructions_text = QTextEdit(TEXT)
        self.instructions_text.setReadOnly(True)
        self.gridLayout.addWidget(self.instructions_text, 1, 0)

        progress = QLabel("")
        progress.setAlignment(QtCore.Qt.AlignCenter)
        progress_bar = QMovie("./resources/ui/loader.gif")
        progress.setMovie(progress_bar)

        self.actions = QGroupBox("Actions :")
        self.actions_layout = QHBoxLayout()
        self.actions.setLayout(self.actions_layout)

        self.manually_submit = QPushButton("Manually Submit [Advanced users]")
        self.manually_submit.clicked.connect(self.submit_manually)
        self.actions_layout.addWidget(self.manually_submit)
        self.cancel = QPushButton("Abort mission")
        self.cancel.clicked.connect(self.close)
        self.actions_layout.addWidget(self.cancel)
        self.gridLayout.addWidget(self.actions, 2, 0)

        progress_bar.start()
        self.layout.addLayout(self.gridLayout, 1, 0)
        self.setLayout(self.layout)

    def updateLayout(self, debriefing):
        updateBox = QGroupBox("Mission status")
        updateLayout = QGridLayout()
        updateBox.setLayout(updateLayout)

        updateLayout.addWidget(QLabel("<b>Aircrafts destroyed</b>"), 0, 0)
        updateLayout.addWidget(QLabel(str(len(debriefing.killed_aircrafts))), 0, 1)

        updateLayout.addWidget(QLabel("<b>Ground units destroyed</b>"), 1, 0)
        updateLayout.addWidget(QLabel(str(len(debriefing.killed_ground_units))), 1, 1)

        #updateLayout.addWidget(QLabel("<b>Weapons fired</b>"), 2, 0)
        #updateLayout.addWidget(QLabel(str(len(debriefing.weapons_fired))), 2, 1)

        updateLayout.addWidget(QLabel("<b>Base Capture Events</b>"), 2, 0)
        updateLayout.addWidget(QLabel(str(len(debriefing.base_capture_events))), 2, 1)

        # Clear previous content of the window
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        # Set new window content
        self.gridLayout.addWidget(updateBox, 0, 0)

        if not debriefing.mission_ended:
            self.gridLayout.addWidget(QLabel("<b>Mission is being played</b>"), 1, 0)
            self.gridLayout.addWidget(self.actions, 2, 0)
        else:
            bottom_layout = QHBoxLayout()
            #self.gridLayout.addWidget(QLabel("<b>Mission is over !</b>"), 1, 0)
            proceed = QPushButton("Accept results")
            proceed.setProperty("style", "btn-success")
            proceed.clicked.connect(lambda: self.process_debriefing(debriefing))
            bottom_layout.addWidget(self.manually_submit)
            bottom_layout.addWidget(self.cancel)
            bottom_layout.addWidget(proceed)
            self.gridLayout.addLayout(bottom_layout, 1, 0)

    def on_debriefing_udpate(self, debriefing):
        print("On Debriefing update")
        print(debriefing)
        DebriefingFileWrittenSignal.get_instance().sendDebriefing(debriefing)

        if not debriefing.mission_ended:
            self.wait_thread = wait_for_debriefing(lambda debriefing: self.on_debriefing_udpate(debriefing), self.game)

    def process_debriefing(self, debriefing: Debriefing):
        self.game.finish_event(event=self.gameEvent, debriefing=debriefing)
        self.game.pass_turn(ignored_cps=[self.gameEvent.to_cp, ])

        GameUpdateSignal.get_instance().sendDebriefing(self.game, self.gameEvent, debriefing)
        self.close()

    def debriefing_directory_location(self) -> str:
        return os.path.join(base_path(), "liberation_debriefings")

    def closeEvent(self, evt):
        super(QWaitingForMissionResultWindow, self).closeEvent(evt)
        if self.wait_thread is not None:
            self.wait_thread.stop()

    def submit_manually(self):
        file = str(QFileDialog.getOpenFileName(self, "Select game file to open", filter="json(*.json)"))
        print(file)
        try:
            with open("state.json", "r") as json_file:
                json_data = json.load(json_file)
                json_data["mission_ended"] = True
                debriefing = Debriefing(json_data, self.game)
                self.on_debriefing_udpate(debriefing)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Invalid file : " + file)
            msg.setWindowTitle("Invalid file.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec_()
            return

