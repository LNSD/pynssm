"""

"""

from nssm.abstract.collections import AbstractEnum

__all__ = ["StartupType", "PriorityLevel", "ServiceType"]


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
        DELAYED = "SERVICE_DELAYED_START"
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
    # EXIT_ACTION_THROTTLING: "AppThrottle",
    # EXIT_ACTION_RECOVERY_ACTION: "AppExit Default",
    # EXIT_ACTION_RECOVERY_DELAY: "AppRestartDelay",

    # I/O
    "stdout": "AppStdout",
    "stderr": "AppStderr",

    # File rotation
    # FILE_ROTATION_ENABLED: "AppRotateFiles",
    # FILE_ROTATION_ONLINE: "AppRotateOnline",
    # FILE_ROTATION_STDOUT: "AppStdoutCreationDisposition",
    # FILE_ROTATION_STDERR: "AppStderrCreationDisposition",
    # FILE_ROTATION_TIME: "AppRotateSeconds",
    # FILE_ROTATION_SIZE: "AppRotateBytes",

    # Environment
    "env": "AppEnvironmentExtra"
}
