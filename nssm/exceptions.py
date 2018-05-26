"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""

__all__ = ["NssmException", "ServiceException", "ServiceDoesntExistException",
           "ServiceInstallException", "ServiceAlreadyInstalledException",
           "ServiceRemoveException", "ServiceStartException",
           "ServiceStopException", "ServiceResumeException",
           "ServicePauseException", "ServiceConfigurationException",
           "ServiceNotStartedException"]


class NssmException(Exception):
    """
    NSSM generic exception class
    """

    MESSAGE_TEMPLATE = "[{service}] {message}"
    DEFAULT_MESSAGE = "NSSM error occurred"

    def __init__(self, service, message=None, output=None, rcode=None):
        """
        :param service: Service name
        :type service: str
        :param message: Exception message
        :type message: str
        :param output: Console process output message
        :type output: str
        :param rcode: Console process return code
        :type rcode: int
        """
        self.service = service
        self.output = output

        if message is None:
            message = self.DEFAULT_MESSAGE

        message = self.MESSAGE_TEMPLATE.format(service=service,
                                               message=message)
        super(Exception, self).__init__(message)


class ServiceException(NssmException):
    """
    Service base exception
    """
    pass


class ServiceDoesntExistException(ServiceException):
    """
    Service doesn't exist exist exception
    """
    DEFAULT_MESSAGE = "The specified service does not exist as an installed " \
                      "service."


class ServiceInstallException(ServiceException):
    """
    Service install generic exception
    """
    DEFAULT_MESSAGE = "Service installation failed"


class ServiceAlreadyInstalledException(ServiceException):
    """
    Service already created exception
    """
    DEFAULT_MESSAGE = "The specified service already exists"


class ServiceRemoveException(ServiceException):
    """
    Service removal generic exception
    """
    DEFAULT_MESSAGE = "Service removal failed"


class ServiceStartException(ServiceException):
    """
    Service start generic exception
    """
    DEFAULT_MESSAGE = "Service start failed"


class ServiceNotStartedException(ServiceException):
    """
    Service start generic exception
    """
    DEFAULT_MESSAGE = "The service has not been started"


class ServiceStopException(ServiceException):
    """
    Service stop generic exception
    """
    DEFAULT_MESSAGE = "Service stop failed"


class ServicePauseException(ServiceException):
    """
    Service pause generic exception
    """
    DEFAULT_MESSAGE = "Service pause failed"


class ServiceResumeException(ServiceException):
    """
    Service pause generic exception
    """
    DEFAULT_MESSAGE = "Service resume failed"


class ServiceConfigurationException(ServiceException):
    """
    Service pause generic exception
    """
    DEFAULT_MESSAGE = "Service configuration failed"


def map_exception(command, rcode):
    """
    Map command return codes to exceptions

    :param command: Console command
    :param rcode: Command return code
    :type rcode: int
    :return: Mapped exception class
    :rtype: :class:`NssmException`
    """
    cmd_rc_exception_map = {
        # Install command
        ("install", 5): ServiceAlreadyInstalledException,
        ("install", "*"): ServiceInstallException,

        # Remove command
        ("remove", "*"): ServiceRemoveException,

        # Start command
        ("start", "*"): ServiceStartException,

        # Restart command
        ("restart", "*"): ServiceStartException,

        # Stop command
        ("stop", "*"): ServiceStopException,

        # Pause command
        ("pause", 1): ServiceNotStartedException,
        ("pause", "*"): ServicePauseException,

        # Continue command
        ("continue", 1): ServiceNotStartedException,
        ("continue", "*"): ServiceResumeException,

        # Get/Set command
        ("set", "*"): ServiceConfigurationException,
        ("get", "*"): ServiceConfigurationException,

        # Any command
        ("*", 3): ServiceDoesntExistException,
    }

    # Match exact return command and return code
    try:
        return cmd_rc_exception_map[(command, rcode)]
    except KeyError:
        pass  # Not in the map

    # Try with match-all command
    try:
        return cmd_rc_exception_map[("*", rcode)]
    except KeyError:
        pass  # Not in the map

    # Try with match-all return code
    try:
        return cmd_rc_exception_map[(command, "*")]
    except KeyError:
        pass  # Not in the map

    # Unknown return command and return code pair
    return NssmException
