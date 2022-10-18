#
# Libraries - native
#
import os
import shutil
#
# Class
#
class _HelperCopyOnDisk:

    def copy_file_from_path_orig_to_path_dest( self, arg_str_path_to_file_orig: str, arg_str_path_to_dest: str ) :
        """
        This function arg_path_to_file_orig is definitely a file

        For more info:
        https://docs.python.org/3/library/shutil.html

        Copies file origin to destination

        If destination is an existing directory, then origin is copied INTO the directory
        """
        self.raise_error_if_path_is_not_in_dir_home( arg_str_path_to_dest )
        #
        # Create host directory if it doesn't already exist
        # Note: We do the check because python claims os.makedirs() isn't necessarily safe in all cases
        #
        str_path_to_dir_dest_parent = os.path.dirname( arg_str_path_to_dest )
        if not os.path.exists( str_path_to_dir_dest_parent ) : os.makedirs( str_path_to_dir_dest_parent )
        #
        # Execute copy
        #
        shutil.copyfile( arg_str_path_to_file_orig, arg_str_path_to_dest, )

    def copy_dir_into_dir( self, arg_str_path_dir_orig: str, arg_str_path_dir_dest: str ) :

        self.raise_error_if_path_is_not_in_dir_home( arg_str_path_dir_dest )

        str_path_dir_actual_dest = os.path.join( arg_str_path_dir_dest, os.path.basename( arg_str_path_dir_orig ), )

        try : shutil.copytree( arg_str_path_dir_orig, str_path_dir_actual_dest, )
        except Exception as err :
            print( "Warning: copy_dir_into_dir() failed. Skipping attempt." )
            print( "arg_str_path_dir_orig =", arg_str_path_dir_orig, )
            print( "arg_str_path_dir_dest =", arg_str_path_dir_dest, )
            print( "str_path_dir_actual_dest =", str_path_dir_actual_dest, )
            print( "type( err ) =", type( err ), ".", )
            print( "err =", err, )
            print( "\n" )

    def raise_error_if_path_is_not_in_dir_home( self, arg_string_path: str ):
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
helperCopyOnDisk = _HelperCopyOnDisk()





















































