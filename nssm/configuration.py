"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
from voluptuous import Schema, Required, Optional, Or, Coerce, \
                       humanize as hum, REMOVE_EXTRA, ALLOW_EXTRA

from nssm.abstract.collections import AbstractDict
from nssm.parameters import StartupType, PriorityLevel, ServiceType, ExitAction


class ServiceConfiguration(AbstractDict):
    """
    Service configuration object
    """

    def __init__(self, *args, **kwargs):
        """
        Service configuration class constructor
        """
        super(ServiceConfiguration, self).__init__()

        schema = self._get_schema()
        self.dictionary = hum.validate_with_humanized_errors(kwargs, schema)

    @staticmethod
    def _get_schema():
        """
        Build a voluptuous schema to validate the input keyword arguments
        :return: Voluptuous schema
        :rtype: :class:`Schema`
        """
        return Schema({
            # Application
            Optional("path"): str,
            Optional("startup_dir"): str,
            Optional("arguments"): Or(str, list),

            # Details
            Optional("display_name"): str,
            Optional("description"): str,
            Optional("startup"): Coerce(StartupType.coerce),

            # Log on
            Optional("user_account"): Or(str, Schema({
                Required("username"): str,
                Required("password"): str
            }, extra=REMOVE_EXTRA)),
            Optional("type"): Coerce(ServiceType.coerce),

            # Dependencies
            Optional("dependencies"): Or(str, list),

            # Process
            Optional("process_priority"): Coerce(PriorityLevel.coerce),
            Optional("console_window"): bool,
            Optional("cpu_affinity"): Or("All", int),

            # Shutdown
            Optional("terminate_process"): bool,
            Optional("stop_console"): int,
            Optional("stop_window"): int,
            Optional("stop_threads"): int,

            # Exit action
            Optional("restart_throttling"): int,
            Optional("restart_delay"): int,
            Optional("action_on_exit"): Schema({
                Required("Default"): Coerce(ExitAction.coerce)
            }, extra=ALLOW_EXTRA),

            # I/O
            Optional("stdout"): str,
            Optional("stderr"): str,

            # File rotation
            Optional("rotate_files"): bool,
            Optional("rotate_online"): bool,
            Optional("stdout_creation_disposition"): int,
            Optional("stderr_creation_disposition"): int,
            Optional("rotation_time"): int,
            Optional("rotation_size"): int,

            # Environment
            Optional("env"): Or(str, dict)
        }, extra=REMOVE_EXTRA)
