""" Module for easy KMC from python. """


# Copyright (c)  2013-2015  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

# Check for ATK-Python support.

__atkpython__ = True
try:
    from NanoLanguage import *
except:
    __atkpython__ = False

from kmclib.CoreComponents.KMCLocalConfiguration import KMCLocalConfiguration
from kmclib.CoreComponents.KMCInteractions import KMCInteractions
from kmclib.CoreComponents.KMCProcess import KMCProcess
from kmclib.CoreComponents.KMCBucketProcess import KMCBucketProcess
from kmclib.CoreComponents.KMCConfiguration import KMCConfiguration
from kmclib.CoreComponents.KMCLattice import KMCLattice
from kmclib.CoreComponents.KMCLatticeModel import KMCLatticeModel
from kmclib.CoreComponents.KMCUnitCell import KMCUnitCell
from kmclib.CoreComponents.KMCControlParameters import KMCControlParameters
from kmclib.Analysis.OnTheFlyMSD import OnTheFlyMSD
from kmclib.Analysis.TimeStepDistribution import TimeStepDistribution
from kmclib.Analysis.ProcessStatistics import ProcessStatistics
from kmclib.Analysis.Composition import Composition
from kmclib.Utilities.SaveAndReadUtilities import KMCInteractionsFromScript
from kmclib.Utilities.SaveAndReadUtilities import KMCConfigurationFromScript
from kmclib.PluginInterfaces.KMCRateCalculatorPlugin import KMCRateCalculatorPlugin
from kmclib.PluginInterfaces.KMCAnalysisPlugin import KMCAnalysisPlugin
from kmclib.PluginInterfaces.KMCBreakerPlugin import KMCBreakerPlugin
from kmclib.Backend.Backend import MPICommons

__all__ = ['KMCLocalConfiguration', 'KMCInteractions', 'KMCConfiguration',
           'KMCLattice', 'KMCLatticeModel', 'KMCUnitCell',
           'KMCControlParameters', 'KMCInteractionsFromScript',
           'KMCConfigurationFromScript', 'KMCRateCalculatorPlugin',
           'KMCAnalysisPlugin', 'KMCBreakerPlugin', 'KMCProcess',
           'KMCBucketProcess', 'OnTheFlyMSD',
           'TimeStepDistribution', 'Composition',
           'ProcessStatistics', 'MPICommons']

# Trick to initialize and finalize MPI only once.
MPICommons.init()

# Print the header when the module is loaded.
Utilities.PrintUtilities.printHeader()

# Make sure to finalize MPI on exit.
def killme():
    MPICommons.finalize()

import atexit
atexit.register(killme)

