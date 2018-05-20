"""

"""
from voluptuous import Schema, Required, Optional, Or, Coerce, REMOVE_EXTRA, \
                       humanize as hum

from nssm.abstract.collections import AbstractDict
from nssm.parameters import StartupType, PriorityLevel, ServiceType


class ServiceConfiguration(AbstractDict):
    """
    Service configuration object
    """

    def __init__(self, *args, **kwargs):
        """

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
            Optional("user_account"): Or(str, {
                Required("username"): str,
                Required("password"): str
            }),
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

            # I/O
            Optional("stdout"): str,
            Optional("stderr"): str,

            # Environment
            Optional("env"): Or(str, dict)
        }, extra=REMOVE_EXTRA)
