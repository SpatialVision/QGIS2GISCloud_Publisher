# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GISCloudUpload
                                 A QGIS plugin
 Uploader to GIs cloud
                              -------------------
        begin                : 2015-11-23
        copyright            : (C) 2015 by Spatial Vision
        email                : michael.king@spatialvision.com.au
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

__author__ = 'Spatial Vision'
__date__ = '2015-11-23'
__copyright__ = '(C) 2015 by Spatial Vision'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from giscloud_uploader_algorithm import GISCloudUploadAlgorithm
from giscloud_utils import GISCloudUtils


class GISCloudUploadProvider(AlgorithmProvider):
    """
    In this class we set the default processing options.
    """

    def __init__(self):
        AlgorithmProvider.__init__(self)

        # Deactivate provider by default
        self.activate = False

        # Load algorithms
        self.alglist = [GISCloudUploadAlgorithm()]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        """
        Setting of the GIS Cloud API Key as a core parameter.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        AlgorithmProvider.initializeSettings(self)
        ProcessingConfig.addSetting(Setting(
            self.getDescription(),
            GISCloudUtils.GISCloud_character,
            'Please enter your GIS Cloud account API', "Paste API Key here", valuetype=Setting.STRING))

    def unload(self):
        """
        Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        AlgorithmProvider.unload(self)
        ProcessingConfig.removeSetting(
            GISCloudUtils.GISCloud_character)

    def getName(self):
        """This is the name that will appear on the toolbox.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return self.getDescription()

    def getDescription(self):
        """
        This is the provided full name.
        """
        return "GIS Cloud Uploader"

    def getIcon(self):
        """
        Get the icon.
        """
        return GISCloudUtils.getIcon()

    def _loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = self.alglist
