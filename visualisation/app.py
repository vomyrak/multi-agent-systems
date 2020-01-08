# app.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from gui import Ui_MainWindow
from zipfile import ZipFile
import sys
import os
from os import remove as DeleteFile
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from model import Model
from shutil import copyfileobj

class MainWindowUiClass(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.model = Model()

    def setupUi(self, mw):
        super().setupUi(mw)

    def runSimulationPressedSlot(self):
        self.runSimulation(runs, days, balanced, idealist, egotist, susceptible, idealistN, egotistN, suscpetibleN)

    def runSimulation(self, runs, days, balanced, idealist, egotist, susceptible, idealistN, egotistN, suscpetibleN):
        agent_init = f"from agent import *\n\nTotalProfiles = list(filter(lambda x: x[1] != 0, [(Balanced, {balanced}), (Egotist, {egotist}), (Idealist, {idealist}), (Susceptible, {susceptible}), (NotIdealist, {idealistN}), (NotEgotist, {egotistN}), (NotSusceptible, {suscpetibleN})]))"
        total_agents = balanced + idealist + egotist + susceptible + idealistN + egotistN + suscpetibleN
        num_profiles = len(list(filter(lambda x: x != 0, [balanced, idealist, egotist, susceptible, idealistN, egotistN, suscpetibleN])))
        cmd = f"cd ../multi-agent-systems/Agent-Config ; printf \"{agent_init}\" > total_profiles.py ; python3 agent_init.py ; cd ../bin/Debug/netcoreapp3.0/ ; ./multi-agent-systems  --number-days {days} --number-profiles {num_profiles} --number-agents {total_agents} --number-runs {runs}"
        os.system(cmd)

    def makeAgentProfiles(self, balanced, idealist, egotist, susceptible, idealistN, egotistN, susceptibleN):
        # make the json command bollocks happen
        pass

    def filterPrint(self, msg):
        self.filterBrowser.append(msg)

    def refreshAll(self):
        self.populateStandardPlotComboBox()
        self.saveCsvPushButton.setEnabled(True)
        self.standardPlotComboBox.setEnabled(True)
        self.selectCsvComboBox.setEnabled(True)
        self.addToCsvSelect()
        self.addAgentPushButton.setEnabled(True)
        self.saveAllPushButton.setEnabled(True)
        self.gifButton.setEnabled(True)
        self.daySpinBox.setEnabled(True)
        self.clearAgentsPushButton.setEnabled(True)
        self.plotTypeComboBox.setEnabled(True)
        self.colourComboBox.setEnabled(True)
        self.agentAverageRadio.setEnabled(True)
        self.timeAverageRadio.setEnabled(True)
        self.xComboBox.setEnabled(True)
        self.yComboBox.setEnabled(True)
        self.filterComboBox.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        self.xComboBox.clear()
        self.xComboBox.addItems(self.model.getColumns())
        self.yComboBox.clear()
        self.yComboBox.addItems(self.model.getColumns())
        self.comboBox.clear()
        self.comboBox.addItems(self.model.getColumns())
        self.filterComboBox.clear()
        self.filterComboBox.addItems(["greater than", "equal to", "less than"])
        self.plotTypeComboBox.clear()
        self.plotTypeComboBox.addItems(["line", "bar", "pie", "scatter", "histogram"])
        self.colourComboBox.clear()
        self.colourComboBox.addItems(self.model.getColumns())
        self.lineEdit.setText(self.model.getFileName())
        self.standardPlotWidget.clear()
        self.customPlotWidget.clear()

    def addToCsvSelect(self):
        self.selectCsvComboBox.clear()
        lst = []
        for x in self.model.csvFileSelection:
            lst.append(x[0])
        self.selectCsvComboBox.addItems(lst)

    def updateNumAgents(self):
        balanced = self.model.getBalancedAgents()
        idealist = self.model.getIdealistAgents()
        egotist = self.model.getEgotistAgents()
        susceptible = self.model.getSusceptibleAgents()
        idealistN = self.model.getIdealistNAgents()
        egotistN = self.model.getEgotistNAgents()
        susceptibleN = self.model.getSusceptibleNAgents()
        total = balanced + idealist + egotist + susceptible + idealistN + egotistN + susceptibleN
        self.numAgentsLabel.setText(str(total))
        if total > 0:
            self.runSimulationPushButton.setEnabled(True)
            self.simStatusLabel.setText("Ready!")
        else:
            self.runSimulationPushButton.setEnabled(False)
            self.simStatusLabel.setText("Waiting")
        self.simulationPlotWidget.agentDistribution(balanced, idealist, egotist, susceptible, idealistN, egotistN, susceptibleN, False)

    ######### slots ###########

    def runSimulationSlot(self):

        runs = self.model.getSimRuns()
        days = self.model.getSimDays()
        balanced = self.model.getBalancedAgents()
        idealist = self.model.getIdealistAgents()
        egotist = self.model.getEgotistAgents()
        susceptible = self.model.getSusceptibleAgents()
        idealistN = self.model.getIdealistNAgents()
        egotistN = self.model.getEgotistNAgents()
        susceptibleN = self.model.getSusceptibleNAgents()

        self.runSimulation(runs, days, balanced, idealist, egotist, susceptible, idealistN, egotistN, susceptibleN)
        self.model.clearLastSimulation()
        self.model.addCurrentSimulation(runs)
        self.simStatusLabel.setText("Done!")
        self.addToCsvSelect()
        self.selectCsvComboBox.setEnabled(True)

    def agentUpdateSlot(self):
        pass

    def csvSelectSlot(self, index):
        fileName = self.model.getCsvPath(index)
        self.model.setFileName(fileName, False)
        self.refreshAll()
        self.selectCsvComboBox.setCurrentIndex(index)

    def returnPressedSlot(self):
        #self.debugPrint("enter pressed in line edit")
        fileName = self.lineEdit.text()
        if self.model.setFileName(fileName, True):
            self.model.setFileName(fileName, True)
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified: " + fileName)

    def loadProfileSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Load Agent Setup",
                        "",
                        "Setup Files (*.setup);;All Files (*)",
                        options=options)
        
        with open(fileName, "r") as f:
            contents = f.readlines()
            runs = int(contents[0])
            days = int(contents[1])
            balanced = int(contents[2])
            idealist = int(contents[3])
            egotist = int(contents[4])
            susceptible = int(contents[5])
            idealistN = int(contents[6])
            egotistN = int(contents[7])
            susceptibleN = int(contents[8])

            self.model.updateSimRuns(runs)
            self.model.updateSimDays(days)
            self.model.updateBalancedAgents(balanced)
            self.model.updateIdealistAgents(idealist)
            self.model.updateEgotistAgents(egotist)
            self.model.updateSusceptibleAgents(susceptible)
            self.model.updateIdealistNAgents(idealistN)
            self.model.updateEgotistNAgents(egotistN)
            self.model.updateSusceptibleNAgents(susceptibleN)

            self.runSpinBox.setValue(runs)
            self.daySpinBox.setValue(days)
            self.balancedSpinBox.setValue(balanced)
            self.idealistSpinBox.setValue(idealist)
            self.egotistSpinBox.setValue(egotist)
            self.susceptibleSpinBox.setValue(susceptible)
            self.idealistNSpinBox.setValue(idealistN)
            self.egotistNSpinBox.setValue(egotistN)
            self.susceptibleNSpinBox.setValue(susceptibleN)

        self.updateNumAgents()


    def saveProfileSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,
                                                'Save Agent Setup',
                                                "",
                                                "Setup Files (*.setup);;All Files (*)",
                                                options=options)
        
        if not fileName.endswith(".setup"):
            fileName += ".setup"

        runs = self.model.getSimRuns()
        days = self.model.getSimDays()
        balanced = self.model.getBalancedAgents()
        idealist = self.model.getIdealistAgents()
        egotist = self.model.getEgotistAgents()
        susceptible = self.model.getSusceptibleAgents()
        idealistN = self.model.getIdealistNAgents()
        egotistN = self.model.getEgotistNAgents()
        susceptibleN = self.model.getSusceptibleNAgents()
        
        with open(fileName, "w+") as f:
            f.write(str(runs) + "\n")
            f.write(str(days) + "\n")
            f.write(str(balanced) + "\n")
            f.write(str(idealist) + "\n")
            f.write(str(egotist) + "\n")
            f.write(str(susceptible) + "\n")
            f.write(str(idealistN) + "\n")
            f.write(str(egotistN) + "\n")
            f.write(str(susceptibleN) + "\n")
            

    def loadCsvSlot(self):
        #self.debugPrint("browse button pressed")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Load CSV",
                        "",
                        "CSV Files (*.csv);;All Files (*)",
                        options=options)
        if fileName:
            self.model.setFileName(fileName, True)
            self.refreshAll()

    def saveCsvSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        saveFile, _ = QtWidgets.QFileDialog.getSaveFileName(None,
                                                'Save CSV',
                                                "",
                                                "CSV Files (*.csv);;All Files (*)",
                                                options=options)
        
        if not saveFile.endswith(".csv"):
            saveFile += ".csv"

        
        with open(saveFile, 'w+') as output, open(self.model.fileName, 'r') as input:
            copyfileobj(input, output)
            
    ####### simulation comboBoxes ##########

    def simRunUpdateSlot(self, int):
        self.model.updateSimRuns(int)

    def simDayUpdateSlot(self, int):
        self.model.updateSimDays(int)

    def balancedUpdateSlot(self, int):
        self.model.updateBalancedAgents(int)
        self.updateNumAgents()

    def egotistUpdateSlot(self, int):
        self.model.updateEgotistAgents(int)
        self.updateNumAgents()

    def egotistNUpdateSlot(self, int):
        self.model.updateEgotistNAgents(int)
        self.updateNumAgents()

    def idealistUpdateSlot(self, int):
        self.model.updateIdealistAgents(int)
        self.updateNumAgents()

    def idealistNUpdateSlot(self, int):
        self.model.updateIdealistNAgents(int)
        self.updateNumAgents()

    def susceptibleUpdateSlot(self, int):
        self.model.updateSusceptibleAgents(int)
        self.updateNumAgents()

    def susceptibleNUpdateSlot(self, int):
        self.model.updateSusceptibleNAgents(int)
        self.updateNumAgents()

    def dayChangedSlot(self, value):
        self.model.updateDay(value)

    def noneAverageSelected(self):
        # can do push button setEnabled(True/False)
        pass

    def agentAverageSelected(self):
        pass

    def timeAverageSelected(self):
        pass

    def addAgentSlot(self):
        pass

    def exportGifSlot(self):
        pass

    def saveAllSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,
                                                'Save Figures',
                                                "",
                                                "ZIP archive (*.zip);;All Files (*)",
                                                options=options)
        
        if not fileName.endswith(".zip"):
            fileName += ".zip"

        plotNames = self.standardPlotWidget.exportAll(self.model.fileContent, fileName)
        for plot in plotNames:
            DeleteFile(plot)

    def plotColourSlot(self):
        pass

    def plotTypeSlot(self):
        pass

    def xAxisSlot(self):
        pass

    def yAxisSlot(self):
        pass

    def addFilterSlot(self):
        # msg is the filter setting to print
        # pull values
        parameter = str(self.comboBox.currentText())
        dataType = getattr(self.model.fileContent, parameter)
        dataType = dataType.dtype
        msg = parameter
        if dataType == "object":
            value = str(self.filterComboBox.currentText())
            include = self.withRadioButton.isChecked()
            msg += " == " if include else " != "
            msg += value
            self.model.addFilter(parameter, include=include, value=value)

        else:
            num = int(self.filterNumSpinBox.value())
            greater = self.filterComboBox.currentIndex()
            if greater == 0:
                msg += " > "
            elif greater == 1:
                msg += " == "
            else:
                msg += " < " 
            self.model.addFilter(parameter, num=num, greater=greater)
        msg += "\n"
        self.filterPrint(msg)
        pass

    def removeAllFiltersSlot(self):
        self.textBrowser.clear()
        self.model.plotContent = self.model.getFileContents()

    def filterParameterSelectedSlot(self):
        parameter = str(self.comboBox.currentText())
        dataType = getattr(self.model.fileContent, parameter)
        dataType = dataType.dtype
        if dataType == "object":
            self.filterComboBox.clear()
            items = getattr(self.model.plotContent, parameter)
            items = items.unique()
            self.filterComboBox.addItems(items)
            self.filterComboBox.setEnabled(True)
            self.filterNumSpinBox.setEnabled(False)
        else:
            self.filterComboBox.clear()
            self.filterComboBox.addItems(["greater than", "equal to", "less than"])
            self.filterComboBox.setEnabled(True)
            self.filterNumSpinBox.setEnabled(True)


    ############# standard plots ###############

    def populateStandardPlotComboBox(self):
        self.standardPlotComboBox.clear()
        self.standardPlotComboBox.addItem("Average Energy and Agent Death")
        self.standardPlotComboBox.addItem("Energy Distribution")
        self.standardPlotComboBox.addItem("Idealism, Susceptibility and Egotism")
        self.standardPlotComboBox.addItem("Fairness Distribution")
        self.standardPlotComboBox.addItem("Average Infamy")
        self.standardPlotComboBox.addItem("Infamy Distribution")
        self.standardPlotComboBox.addItem("Crime Rate")
        self.standardPlotComboBox.addItem("Crimes Committed")
        self.standardPlotComboBox.addItem("Agent Activity")
        self.standardPlotComboBox.addItem("Maximum Punishment Timeline")
        self.standardPlotComboBox.addItem("Work Rule Timeline")
        self.standardPlotComboBox.addItem("Food Rule Timeline")
        self.standardPlotComboBox.addItem("Shelter Rule Timeline")
        self.standardPlotComboBox.addItem("Voting Rule Timeline")
        self.standardPlotComboBox.addItem("Maximum Punishment Distribution")
        self.standardPlotComboBox.addItem("Work Rule Distribution")
        self.standardPlotComboBox.addItem("Food Rule Distribution")
        self.standardPlotComboBox.addItem("Shelter Rule Distribution")
        self.standardPlotComboBox.addItem("Voting Rule Distribution")
        

    def standardPlotSelectSlot(self, plot):
        plot = str(plot)
        if plot == "Average Energy and Agent Death":
            self.standardPlotWidget.standardEnergy(self.model.fileContent, False)
        elif plot == "Energy Distribution":
            self.standardPlotWidget.standardEnergyDistribution(self.model.fileContent, False)
        elif plot == "Idealism, Susceptibility and Egotism":
            self.standardPlotWidget.standardISE(self.model.fileContent, False)
        elif plot == "Fairness Distribution":
            self.standardPlotWidget.standardFairness(self.model.fileContent, False)
        elif plot == "Average Infamy":
            self.standardPlotWidget.standardInfamy(self.model.fileContent, False)
        elif plot == "Infamy Distribution":
            self.standardPlotWidget.standardInfamyDistribution(self.model.fileContent, False)
        elif plot == "Crime Rate":
            self.standardPlotWidget.standardCrimeRate(self.model.fileContent, False)
        elif plot == "Crimes Committed":
            self.standardPlotWidget.standardCrimeRaw(self.model.fileContent, False)
        elif plot == "Agent Activity":
            self.standardPlotWidget.standardActivity(self.model.fileContent, False)
        elif plot == "Maximum Punishment Timeline":
            self.standardPlotWidget.standardPunishmentRule(self.model.fileContent, False)
        elif plot == "Work Rule Timeline":
            self.standardPlotWidget.standardWorkRule(self.model.fileContent, False)
        elif plot == "Food Rule Timeline":
            self.standardPlotWidget.standardFoodRule(self.model.fileContent, False)
        elif plot == "Shelter Rule Timeline":
            self.standardPlotWidget.standardShelterRule(self.model.fileContent, False)
        elif plot == "Voting Rule Timeline":
            self.standardPlotWidget.standardVotingRule(self.model.fileContent, False)
        elif plot == "Maximum Punishment Distribution":
            self.standardPlotWidget.standardPunishmentRulePie(self.model.fileContent, False)
        elif plot == "Work Rule Distribution":
            self.standardPlotWidget.standardWorkRulePie(self.model.fileContent, False)
        elif plot == "Food Rule Distribution":
            self.standardPlotWidget.standardFoodRulePie(self.model.fileContent, False)
        elif plot == "Shelter Rule Distribution":
            self.standardPlotWidget.standardShelterRulePie(self.model.fileContent, False)
        elif plot == "Voting Rule Distribution":
            self.standardPlotWidget.standardVotingRulePie(self.model.fileContent, False)

    def defaultEnergySlot(self):
        self.standardPlotWidget.defaultEnergyPlot(self.model.fileContent, False)

    def defaultShelterSlot(self):
        pass
        #self.standardPlotWidget.defaultShelterPlot(self.model.fileContent, False)

    def defaultFoodSlot(self):
        pass
        #self.standardPlotWidget.defaultFoodPlot(self.model.fileContent, False)

    def defaultEnergyBoxSlot(self):
        self.standardPlotWidget.defaultEnergyBoxPlot(self.model.fileContent, False)

    def defaultEgotismSlot(self):
        self.standardPlotWidget.defaultEgotismPlot(self.model.fileContent, False)

    def defaultSusceptibilitySlot(self):
        self.standardPlotWidget.defaultSusceptibilityPlot(self.model.fileContent, False)

    def defaultIdealismSlot(self):
        self.standardPlotWidget.defaultIdealismPlot(self.model.fileContent, False)

    def defaultFairnessSlot(self):
        self.standardPlotWidget.defaultFairnessPlot(self.model.fileContent, False)

    def defaultPlaceholderSlot(self):
        self.standardPlotWidget.defaultTestPlot(self.model.fileContent, False)

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("./build/icon.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUiClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
