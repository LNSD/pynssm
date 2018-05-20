"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
import os
import re
import subprocess as sp
import logging

from nssm.exceptions import *

log = logging.getLogger(__name__)


class Wrapper(object):

    @staticmethod
    def command(command, service_name, *args):
        """
        Service installation
        :param command: nssm command
        :type command: str
        :param service_name: Service name
        :type service_name: str
        :param args: Program arguments
        :type args: str or tuple
        :return: Return code and output of the command
        :rtype: (int, str)
        """
        # Build de command string
        cmd = [Wrapper._nssm_exe(), command, service_name]
        cmd += args if len(args) == 1 else list(args)

        # Format in an unique command string
        cmd = " ".join(cmd)

        # Print command string for debugging purpose
        log.debug(cmd)

        # Run the command
        try:
            out = sp.check_output(cmd, stderr=sp.STDOUT,
                                  universal_newlines=True)
            return 0, out.decode("utf-16")

        except sp.CalledProcessError as err:
            msg = "{msg} ({rc}): {out}"
            err.output = err.output.decode("utf-16")
            err.output = re.sub(r"\n+", " ", err.output)

            command_except_map = {
                "install": ServiceInstallException,
                "remove": ServiceRemoveException,
                "start": ServiceStartException,
                "restart": ServiceStartException,
                "stop": ServiceStopException,
                "pause": ServicePauseException,
                "continue": ServiceResumeException
            }

            if command in command_except_map.keys():
                msg = msg.format(
                    msg=command_except_map[command].DEFAULT_MESSAGE,
                    rc=err.returncode,
                    out=err.output
                )
                raise command_except_map[command](service_name, msg)

            else:
                msg = msg.format(msg=NssmException.DEFAULT_MESSAGE,
                                 rc=err.returncode,
                                 out=err.output)
                raise NssmException(service_name, msg)

    @staticmethod
    def _nssm_exe():
        """
        Build executable full path depending on processor architecture
        :return: Path to the bundled executable
        :rtype: str
        """
        arch = "win64" if os.environ['PROCESSOR_ARCHITECTURE'] else "win32"
        return os.path.join(os.path.dirname(__file__), "bin", arch, "nssm.exe")
