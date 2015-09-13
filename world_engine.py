# -*- coding: utf-8 -*-
"""
/***************************************************************************
 world_engine
                                 A QGIS plugin
 chainage features
                             -------------------
        begin                : 2013-02-20
        copyright            : (C) 2014 by Werner Macho
        email                : werner.macho@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import QFileInfo, QSettings, QTranslator
from PyQt4.QtCore import QCoreApplication, qVersion
from PyQt4.QtGui import QAction, QIcon

from qgis.core import QgsApplication, QgsMapLayer, QGis

from PyQt4.QtGui import QProgressBar
from qgis.gui import QgsMessageBar

# Import the code for the dialog
from world_engine_dialog import WorldEngineDialog

# Initialize Qt resources from file resources.py, don't delete even if it
# shows not used
import resources_rc
import zmq
#import pydevd
#pydevd.settrace('localhost', port=55555, stdoutToServer=True,
#                stderrToServer=True, suspend=False)

class WorldEngine:
    """Main class for Chainage
    """
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.context = zmq.Context()
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = \
            QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + \
            "/python/plugins/world_engine"
        # initialize locale
        locale_path = ""
        locale = QSettings().value("locale/userLocale")[0:2]

        if QFileInfo(self.plugin_dir).exists():
            locale_path = self.plugin_dir + "/i18n/world_engine_" + locale + ".qm"

        if QFileInfo(locale_path).exists():
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference

    def initGui(self):
        """Initiate GUI
        """
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/world_engine/img/hslLogo.png"),
            u"WorldEngine", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu(u"&WorldEngine", self.action)

    def unload(self):
        """ Unloading the plugin
        """
        # Remove the plugin menu item and icon
        self.iface.removePluginVectorMenu(u"&WorldEngine", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        """ Running the plugin
        """
        leave = -1
        for layer in self.iface.mapCanvas().layers():
            if layer.type() == QgsMapLayer.VectorLayer and \
               layer.geometryType() == QGis.Line:
                leave += 1

        if leave < 0:
            message = QCoreApplication.translate('world_engine',
                                                 "No layers with line features - chainage not useful!")
            mb = self.iface.messageBar()
            mb.pushWidget(mb.createMessage(message),
                          QgsMessageBar.WARNING, 5)
            return
        # show the dialog            
        dialog = WorldEngineDialog(self.iface)
        # Run the dialog event loop
        result = dialog.exec_()
        # See if OK was pressed
        self.iface.messageBar().pushInfo(u'WorldEngine Result:{}'.format(result), u'Pass')       
        if result == 1:
        
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
