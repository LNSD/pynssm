"""

"""
import re
from nssm.abstract.collections import AbstractEnum

from nssm.wrapper import Wrapper
from nssm.parameters import PARAM_MAP
from nssm.configuration import ServiceConfiguration


class ServiceStatus(AbstractEnum):
    STOPPED = "SERVICE_STOPPED"
    RUNNING = "SERVICE_RUNNING"
    PAUSED = "SERVICE_PAUSED"


class Service(object):
    """
    NSSM Service class
    """

    def __init__(self, name, path, **kwargs):
        """
        :param name: Service name
        :type name: str
        """
        self.name = name
        self.path = path
        self.configuration = ServiceConfiguration(**kwargs)

    def install(self):
        """
        Install the service
        """
        Wrapper.command("install", self.name, self.path)

        if self.configuration:
            self.configure(self.configuration)

    def remove(self):
        """
        Remove the service
        """
        Wrapper.command("remove", self.name, "confirm")

    def start(self):
        """
        Start the service
        """
        Wrapper.command("start", self.name)

    def stop(self):
        """
        Stop the service
        """
        Wrapper.command("stop", self.name)

    def restart(self):
        """
        Restart the service
        """
        Wrapper.command("restart", self.name)

    def pause(self):
        """
        Pause the service
        """
        Wrapper.command("pause", self.name)

    def resume(self):
        """
        Resume the service
        """
        Wrapper.command("continue", self.name)

    def rotate(self):
        """
        Triggers on-demand rotation for `nssm` services with I/O redirection
        and online rotation enabled.

        `nssm` accepts user-defined control 128 as a cue to begin output
        file rotation. Non-nssm services might respond to control 128 in
        their own way (or ignore it, or crash).
        """
        Wrapper.command("rotate", self.name)

    def status(self):
        """
        Query the service's status
        """
        rc, out = Wrapper.command("status", self.name)

        # Parse response
        status = re.search(r"SERVICE_([A-Z]+)", out).group(1)
        return ServiceStatus.coerce(status)

    def configure(self, config):
        """
        Configure the service
        :param config: Service configuration
        :type config: :class:`ServiceConfiguration`
        """
        msg = "Unknown configuration object: {}"
        assert isinstance(config, ServiceConfiguration), msg.format(config)

        # Update service configuration
        self.configuration.update(config)

        for param, val in config.items():
            Wrapper.command("set", self.name, PARAM_MAP[param], val)


