"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
import os
import re
import subprocess as sp
import logging

from .exceptions import NssmException, map_exception

log = logging.getLogger(__name__)


class Wrapper(object):

    @staticmethod
    def command(command, service_name, *args):
        """
        NSSM command

        :param command: NSSM command
        :type command: str
        :param service_name: Service name
        :type service_name: str
        :param args: Program arguments
        :type args: str or tuple
        :return: Return code and output of the command
        :rtype: (int, str)
        """
        # Build de command string
        cmd = [Wrapper.nssm_exe(), command, service_name]
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
            # Tidy up the command error output
            err.output = err.output.decode("utf-16")
            err.output = re.sub(r"\n+", " ", err.output)

            # Map the error output code to an exception
            exception = map_exception(command, err.returncode)

            if exception != NssmException:
                message = None

            else:
                message = "{msg} ({rc}): {out}"
                message = message.format(
                    msg=exception.DEFAULT_MESSAGE,
                    rc=err.returncode,
                    out=err.output
                )

            raise exception(service_name, message,
                            output=err.output,
                            rcode=err.returncode)

    @staticmethod
    def nssm_exe():
        """
        Build full path to the NSSM binary executable depending on processor
        architecture

        :return: Path to the bundled executable
        :rtype: str
        """
        arch = "win64" if os.environ['PROCESSOR_ARCHITECTURE'] else "win32"
        return os.path.join(os.path.dirname(__file__), "bin", arch, "nssm.exe")


executable = Wrapper.nssm_exe()
