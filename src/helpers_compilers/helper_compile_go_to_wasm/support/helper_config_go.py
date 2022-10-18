#
# Libraries - native
#
import contextlib
import os
#
# Class
#
class _HelperConfigGo:

    def get_str_path_dir_pkg( self, arg_str_path_dir_project: str ) -> str : return os.path.join( arg_str_path_dir_project, "pkg", )

    def print_message( self, arg_str_message: str ) : print( "(go -> wasm)", arg_str_message, "\n", )

    @contextlib.contextmanager
    def temporarily_print_message( self, arg_str_message: str ):
        str_message = arg_str_message if arg_str_message.endswith( "..." ) else "".join( [ arg_str_message, "...", ] )
        print( str_message )
        yield
        print( "".join( [ str_message, "DONE\n", ] ) )

    def __init__(self):

        self.field_str_name_file_main_wasm = "main.wasm"

        self.field_str_path_dir_gopath = os.environ[ "GOPATH" ]

        self.field_str_version_for_go = "1.19.1"
        self.field_str_path_dir_goroot = os.path.join( "/usr/local/Cellar/go", self.field_str_version_for_go, "libexec" )
#
# Public
#
helperConfigGo = _HelperConfigGo()
















































