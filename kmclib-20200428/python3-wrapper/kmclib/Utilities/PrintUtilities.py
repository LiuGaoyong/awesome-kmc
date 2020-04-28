""" Module for holding common printing utility functions. """


# Copyright (c)  2013-2016  Mikael Leetmaa
#
# This file is part of the kmclib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import sys

from kmclib.Backend.Backend import MPICommons


def prettyPrint(msg, output=None):
    """
    Utility function for printing an output string to screen.

    :param msg: The message to print.
    :type msg: str

    :param out: The stream to write to. Defaults to sys.stdout.
    """
    # Set the default.
    if output is None:
        output = sys.stdout

    # Write.
    if MPICommons.isMaster():
        output.write(msg)
        output.write("\n")
    MPICommons.barrier()

def printHeader(output=None):
    """
    Utility function for printing the run header information.

    :param out: The stream to write to. Defaults to sys.stdout.
    """
    # Set the default.
    if output is None:
        output = sys.stdout

    # Write.
    prettyPrint("# -----------------------------------------------------------------------------", output)
    prettyPrint("# kmclib version 2.0-a1", output)
    prettyPrint("# Distributed under the GPLv3 license", output)
    prettyPrint("# Copyright (C)  2012-2016  Mikael Leetmaa", output)
    prettyPrint("# Developed by Mikael Leetmaa <leetmaa@kth.se>", output)

    prettyPrint("#", output)
    prettyPrint("# This program is distributed in the hope that it will be useful", output);
    prettyPrint("# but WITHOUT ANY WARRANTY; without even the implied warranty of", output);
    prettyPrint("# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the", output);
    prettyPrint("# LICENSE and README files, and the source code, for details.", output);
    prettyPrint("#", output);
    prettyPrint("# You should have received a copy of the GNU General Public License version 3", output);
    prettyPrint("# (GPLv3) along with this program. If not, see <http://www.gnu.org/licenses/>.", output);
    prettyPrint("# -----------------------------------------------------------------------------", output)
    prettyPrint("", output)
