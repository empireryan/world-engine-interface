# -*- coding: utf-8 -*-
"""
/***************************************************************************
 world_engine
                                 A QGIS plugin
 chainage features
                             -------------------
        begin                : 2015-9-7
        copyright            : (C) 2015 Ryan A. Rodriguez
        email                : ryarodri@ucsc.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    """
    load WorldEngine class from file world_engine and init plugin
    """
    from world_engine import WorldEngine
    return WorldEngine(iface)
