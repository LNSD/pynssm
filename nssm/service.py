"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
from .abstract.collections import AbstractEnum

from .wrapper import Wrapper
from .parameters import PARAM_MAP
from .configuration import ServiceConfiguration


class ServiceStatus(AbstractEnum):
    STOPPED = "SERVICE_STOPPED"
    RUNNING = "SERVICE_RUNNING"
    PAUSED = "SERVICE_PAUSED"


class Service(object):
    """
    NSSM Service class
    """

    SERVICE_NAME = None
    SERVICE_PATH = None

    def __init__(self, name=None, path=None, **kwargs):
        """
        :param name: Service name
        :type name: :class:`str`
        :param path: Executable path
        :type path: :class:`str`
        """
        if name:
            self.SERVICE_NAME = name

        if path:
            self.SERVICE_PATH = path

        self.configuration = ServiceConfiguration(**kwargs)

    def install(self):
        """
        Install the service
        """
        Wrapper.command("install", self.SERVICE_NAME, self.SERVICE_PATH)

        if self.configuration:
            self.configure(self.configuration)

    def remove(self):
        """
        Remove the service
        """
        Wrapper.command("remove", self.SERVICE_NAME, "confirm")

    def start(self):
        """
        Start the service
        """
        Wrapper.command("start", self.SERVICE_NAME)

    def stop(self):
        """
        Stop the service
        """
        Wrapper.command("stop", self.SERVICE_NAME)

    def restart(self):
        """
        Restart the service
        """
        Wrapper.command("restart", self.SERVICE_NAME)

    def pause(self):
        """
        Pause the service
        """
        Wrapper.command("pause", self.SERVICE_NAME)

    def resume(self):
        """
        Resume the service
        """
        Wrapper.command("continue", self.SERVICE_NAME)

    def rotate(self):
        """
        Triggers on-demand rotation for `nssm` services with I/O redirection
        and online rotation enabled.

        `nssm` accepts user-defined control 128 as a cue to begin output
        file rotation. Non-nssm services might respond to control 128 in
        their own way (or ignore it, or crash).
        """
        Wrapper.command("rotate", self.SERVICE_NAME)

    def status(self):
        """
        Query the service's status

        :return: Service status
        :rtype: :class:`.ServiceStatus`
        """
        rc, out = Wrapper.command("status", self.SERVICE_NAME)
        return ServiceStatus(out.strip())

    def configure(self, config):
        """
        Configure the service

        :param config: Service configuration
        :type config: :class:`.ServiceConfiguration`
        """
        msg = "Unknown configuration object: {}"
        assert isinstance(config, ServiceConfiguration), msg.format(config)

        # Update service configuration
        self.configuration.update(config)

        for param, value in config.items():

            if param == "user_account" and isinstance(value, dict):
                value = value["username"] + " " + value["password"]

            elif param == "env" and isinstance(value, dict):
                env = ""
                for k, v in value.items():
                    env += k + "=" + v
                value = env

            elif param == "action_on_exit":
                for k, v in value.items():
                    v = v.value
                    Wrapper.command("set", self.SERVICE_NAME, PARAM_MAP[param], k, v)
                continue

            if isinstance(value, AbstractEnum):
                value = value.value
            elif isinstance(value, bool):
                value = 1 if value else 0

            Wrapper.command("set", self.SERVICE_NAME, PARAM_MAP[param], value)

    def _edit(self):
        """
        Opens the NSSM in GUI mode to edit the configured service. Intended
        to be called only from the CLI.

        :param name: Service name
        :type name: :class:`str`
        """
        Wrapper.command("edit", self.SERVICE_NAME)
