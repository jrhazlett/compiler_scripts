#
# Libraries - native
#
import os
#
# Class
#
class _HelperCreateOnDisk:

    def create_dir_if_non_existent( self, arg_str_path_dir: str ) :

        self.raise_error_if_path_is_not_in_dir_home( arg_str_path_dir )

        if not os.path.exists( arg_str_path_dir ) : os.mkdir( arg_str_path_dir )

    def raise_error_if_path_is_not_in_dir_home( self, arg_string_path: str ) :
        #
        # Get path to home directory
        #
        str_path_dir_home = os.path.expanduser( "~" )
        #
        # Get absolute path
        #
        str_path_absolute = arg_string_path
        if str_path_absolute.startswith( "~" ) : str_path_absolute = os.path.expanduser( str_path_absolute )
        # Reminder: This also accounts for '../'
        elif str_path_absolute.startswith( "." ) : str_path_absolute = os.path.abspath( str_path_absolute )
        elif not str_path_absolute.startswith( "/" ) : str_path_absolute = os.path.abspath( os.path.join( ".", str_path_absolute, ) )
        #
        # Do check
        #
        if not str_path_absolute.startswith( str_path_dir_home ) :
            print( "Error: arg_string_path is not in user home." )
            print( "arg_string_path =", arg_string_path, )
            print( "arg_string_path.startswith( str_path_dir_home ) =", arg_string_path.startswith( str_path_dir_home ), )
            print( "\n" )
            raise ()
#
# Public
#
helperCreateOnDisk = _HelperCreateOnDisk()


















































