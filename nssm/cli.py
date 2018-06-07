"""
 Created on June 7, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
from inspect import isclass
from argparse import ArgumentParser, Namespace, _SubParsersAction


class CliCommand(object):
    """
    Command line command class
    """

    def __init__(self, parser):
        """
        :param parser: Root argument parser or "command" sub-parser
        :type parser: :class:`.ArgumentParser` or :class:`._SubParsersAction`
        """

        # Check parser type to avoid undesired exceptions from
        # :class:`.ArgumentParser`.
        if isinstance(parser, ArgumentParser):
            self.subparsers = parser.add_subparsers(dest="command")
        elif isinstance(parser, _SubParsersAction):
            self.subparsers = parser
        else:
            msg = "Invalid input argument type: {}"
            raise TypeError(msg.format(parser))

    @staticmethod
    def execute(args):
        """
        Execute the desired command actions

        :param args: Command line parsed arguments
        :type args: :class:`.Namespace`
        """
        pass


class ServiceCliCommand(CliCommand):
    """
    Service command line base class

    Extend this class to add custom arguments to the different commands
    """

    SERVICE = None

    def __init__(self, parser, service=None):
        """
        :param parser: Root argument parser
        :type parser: :class:`.ArgumentParser` or :class:`._SubParsersAction`
        :param service: Nssm service class
        :type service: :class:`type` or :class:`nssm.Service`
        """

        if service:
            self.SERVICE = service

        # Check parser type to avoid undesired exceptions from `argparser`.
        super(ServiceCliCommand, self).__init__(parser)

        # Service command
        service_parser = self.subparsers.add_parser("service")
        self.add_service_arguments(service_parser)

        # Service actions
        service_subparsers = service_parser.add_subparsers(dest="action")

        # Service action: "install"
        service_install_parser = service_subparsers.add_parser("install")
        self.add_service_install_arguments(service_install_parser)

        # Service action: "uninstall"
        service_remove_parser = service_subparsers.add_parser("remove")
        service_uninstall_parser = service_subparsers.add_parser("uninstall")
        self.add_service_uninstall_arguments(service_remove_parser)
        self.add_service_uninstall_arguments(service_uninstall_parser)

        # Service action: "start"
        service_start_parser = service_subparsers.add_parser("start")
        self.add_service_start_arguments(service_start_parser)

        # Service action: "restart"
        service_restart_parser = service_subparsers.add_parser("restart")
        self.add_service_restart_arguments(service_restart_parser)

        # Service action: "stop"
        service_stop_parser = service_subparsers.add_parser("stop")
        self.add_service_stop_arguments(service_stop_parser)

        # Service action: "pause"
        service_pause_parser = service_subparsers.add_parser("pause")
        self.add_service_pause_arguments(service_pause_parser)

        # Service action: "resume"
        service_resume_parser = service_subparsers.add_parser("resume")
        self.add_service_resume_arguments(service_resume_parser)

        # Service action: "status"
        service_status_parser = service_subparsers.add_parser("status")
        self.add_service_status_arguments(service_status_parser)

        # Service action: "configure"
        service_configure_parser = service_subparsers.add_parser("configure")
        self.add_service_configure_arguments(service_configure_parser)

        # Service action: "edit"
        service_edit_parser = service_subparsers.add_parser("edit")
        service_nssm_parser = service_subparsers.add_parser("nssm")

    def add_service_arguments(self, parser):
        """
        Override this method to add arguments to service command.

        :param parser: Argument parser for service command.
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_install_arguments(self, parser):
        """
        Override this method to add arguments to service command's "install"
        action.

        :param parser: Argument parser for service "install" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_uninstall_arguments(self, parser):
        """
        Override this method to add arguments to service command's
        "uninstall" action.

        :param parser: Argument parser for service "uninstall" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_start_arguments(self, parser):
        """
        Override this method to add arguments to service command's "start"
        action.

        :param parser: Argument parser for service "start" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_restart_arguments(self, parser):
        """
        Override this method to add arguments to service command's "restart"
        action.

        :param parser: Argument parser for service "restart" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_stop_arguments(self, parser):
        """
        Override this method to add arguments to service command's "stop"
        action.

        :param parser: Argument parser for service "stop" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_pause_arguments(self, parser):
        """
        Override this method to add arguments to service command's "pause"
        action.

        :param parser: Argument parser for service "pause" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_resume_arguments(self, parser):
        """
        Override this method to add arguments to service command's "resume"
        action.

        :param parser: Argument parser for service "resume" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_status_arguments(self, parser):
        """
        Override this method to add arguments to service command's "status"
        action.

        :param parser: Argument parser for service "status" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    def add_service_configure_arguments(self, parser):
        """
        Override this method to add arguments to service command's
        "configure" action.

        :param parser: Argument parser for service "configure" action
        :type parser: :class:`.ArgumentParser`
        """
        pass

    @classmethod
    def edit(cls):
        """
        Default implementation for "service edit/nssm" action
        """
        if cls.SERVICE:
            if isclass(cls.SERVICE):
                cls.SERVICE()._edit()
            else:
                cls.SERVICE._edit()
        else:
            msg = 'Service not associated: {}'
            raise AttributeError(msg.format(cls.SERVICE))

