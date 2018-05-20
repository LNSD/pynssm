"""
 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""


class NssmException(Exception):
    """

    """
    MESSAGE_TEMPLATE = "[{service}] {message}"
    DEFAULT_MESSAGE = "NSSM error occurred"

    def __init__(self, service, msg=None):
        """

        """
        if msg is None:
            msg = self.DEFAULT_MESSAGE

        msg = self.MESSAGE_TEMPLATE.format(service=service, message=msg)
        super(Exception, self).__init__(msg)


class ServiceInstallException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service installation failed"


class ServiceRemoveException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service removal failed"


class ServiceStartException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service start failed"


class ServiceStopException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service stop failed"


class ServicePauseException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service pause failed"


class ServiceResumeException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service resume failed"


class ServiceConfigurationException(NssmException):
    """

    """
    DEFAULT_MESSAGE = "Service configuration failed"
