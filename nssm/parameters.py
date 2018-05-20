"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
from nssm.abstract.collections import AbstractEnum

__all__ = ["StartupType", "PriorityLevel", "ServiceType", "ExitAction"]


class StartupType(AbstractEnum):
        """
        AUTOMATIC: Automatic startup at boot.
        DELAYED: Delayed startup at boot.
        MANUAL: Manual startup.
        DISABLED: Service is disabled.

        Note that SERVICE_DELAYED_START is not supported on versions of
        Windows prior to Vista. `nssm` will set the service to automatic
        startup if delayed start is unavailable.
        """
        AUTOMATIC = "SERVICE_AUTO_START"
        DELAYED = "SERVICE_DELAYED_AUTO_START"
        MANUAL = "SERVICE_DEMAND_START"
        DISABLED = "SERVICE_DISABLED"


class PriorityLevel(AbstractEnum):
    """
    The AppPriority parameter takes a priority class constant as specified
    in the SetPriorityClass() documentation.
    """
    REALTIME = "REALTIME_PRIORITY_CLASS"
    HIGH = "HIGH_PRIORITY_CLASS"
    ABOVE_NORMAL = "ABOVE_NORMAL_PRIORITY_CLASS"
    NORMAL = "NORMAL_PRIORITY_CLASS"
    BELOW_NORMAL = "BELOW_NORMAL_PRIORITY_CLASS"
    IDLE = "IDLE_PRIORITY_CLASS"


class ServiceType(AbstractEnum):
    """
    The Type parameter is used to query or set the service type. `nssm`
    recognises all currently documented service types but will only allow
    setting one of two types: SERVICE_WIN32_OWN_PROCESS or
    SERVICE_INTERACTIVE_PROCESS
    """
    # A standalone service. This is the default.
    STANDALONE = "SERVICE_WIN32_OWN_PROCESS"
    # A service which can interact with the desktop.
    DESKTOP = "SERVICE_INTERACTIVE_PROCESS"


class ExitAction(AbstractEnum):
    """
    Exit action
    """
    RESTART = "Restart"
    IGNORE = "Ignore"
    EXIT = "Exit"
    SUICIDE = "Suicide"


PARAM_MAP = {
    # Application
    "path": "Application",
    "startup_dir": "AppDirectory",
    "arguments": "AppParameters",

    # Details
    "display_name": "DisplayName",
    "description": "Description",
    "startup": "Start",

    # Log on
    "user_account": "ObjectName",
    "type": "Type",

    # Dependencies
    "dependencies": "DependsOnService",

    # Process
    "process_priority": "AppPriority",
    "console_window": "AppNoConsole",
    "cpu_affinity": "AppAffinity",

    # Shutdown
    "terminate_process": "AppStopMethodSkip",
    "stop_console": "AppStopMethodConsole",
    "stop_window": "AppStopMethodWindow",
    "stop_threads": "AppStopMethodThreads",

    # Exit action
    "restart_throttling": "AppThrottle",
    "restart_delay": "AppRestartDelay",
    "action_on_exit": "AppExit",

    # I/O
    "stdout": "AppStdout",
    "stderr": "AppStderr",

    # File rotation
    "rotate_files": "AppRotateFiles",
    "rotate_online": "AppRotateOnline",
    "stdout_creation_disposition": "AppStdoutCreationDisposition",
    "stderr_creation_disposition": "AppStderrCreationDisposition",
    "rotation_time": "AppRotateSeconds",
    "rotation_size": "AppRotateBytes",

    # Environment
    "env": "AppEnvironmentExtra"
}
