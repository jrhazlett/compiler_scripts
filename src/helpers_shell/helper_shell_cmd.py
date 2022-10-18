"""
This module is meant really heavy-duty shell work
"""
#
# Libraries - native
#
import contextlib
import os
import subprocess
#
# Libraries - downloaded
#
import sh
#
# Config
#
# Turn offline limits, its clearer which line is which
sh.ErrorReturnCode.truncate_cap = 999999
#
# Public - cmd
#
class _Helper_shell_cmd :
    #
    # Public
    #
    def run_cmd( self, arg_str_cmd: str, arg_dict_environment: {} = None ) :

        with self._temporarily_report_subprocess( arg_str_cmd ) : subprocess.run( arg_str_cmd, **self._get_dict_of_arguments_for_subprocess( arg_dict_environment = arg_dict_environment ), )
    #
    # Private
    #
    def _get_dict_of_arguments_for_subprocess( self, arg_dict_environment: {} = None ) -> {} :

        return {
            #
            # This 'forces' the method to use an environment object (with exceptions), rather than the system
            # environment.
            # WARNING: This isn't 100% valid in ALL cases.  One example: if kivy can't find 'archflags' in the
            # environment object it WILL expand its search to the system environment, unless any triggers are activated
            # to prevent this.
            "env" : arg_dict_environment if arg_dict_environment else os.environ,
            #
            # Reminder: Per James - This assigns a process id, which can be used to reference this process instance
            # later.
            "preexec_fn" : os.setsid,
            #
            # This explicitely forces the cmd to go trough the shell interface.
            # Keep this off the client distributions, because it could become a security issue.
            # Ref: https://docs.python.org/3.5/library/subprocess.html#security-considerations
            #
            "shell" : True,
            #
            # Reminder: Per James - This sets the subprocess output to 'text' so the utf-8 translation doesn't have to
            # happen.
            #
            "universal_newlines" : True,
            #
            # Output options
            #
            # Reminder: Per James - Sending the error templates to the pipe seems to hide it.  For now, leave it none,
            # so we know it will show up in the build output.
            #
            # stderr = subprocess.PIPE,
            #
            "stdout" : subprocess.PIPE,
        }

    @contextlib.contextmanager
    def _temporarily_report_subprocess( self, arg_str_cmd: str ) :

        str_message = "".join( [ "RUNNING COMMAND: ", arg_str_cmd, "...", ] )
        print( str_message )
        yield
        print( "".join( [ str_message, "DONE\n", ] ) )
#
# Public
#
helperShellCmd = _Helper_shell_cmd()













































