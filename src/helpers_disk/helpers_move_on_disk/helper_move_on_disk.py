#
# Libraries - native
#
import os
import shutil
#
# Class
#
class _HelperMoveOnDisk:

    def move_path_orig_to_path_dest( self, arg_str_path_orig: str, arg_str_path_dest: str ) :
        """
        For more info:
        https://docs.python.org/3/library/shutil.html

        Recursively move file or directory
        If destination is existing directory, move origin INTO it
        """
        self.raise_error_if_path_is_not_in_dir_home( arg_str_path_orig )
        self.raise_error_if_path_is_not_in_dir_home( arg_str_path_dest )
        #
        # Create destination directory parent if it doesn't exist
        # Note: We do the check because python claims os.makedirs() isn't necessarily safe in all cases
        #
        path_to_dir_dest_parent = os.path.dirname( arg_str_path_dest )
        if not os.path.exists( path_to_dir_dest_parent ) : os.makedirs( path_to_dir_dest_parent )
        #
        # Execute move
        #
        shutil.move( arg_str_path_orig, arg_str_path_dest, )

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
helperMoveOnDisk = _HelperMoveOnDisk()


















































