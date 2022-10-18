#
# Libraries - native
#
import contextlib
from collections import deque
import glob
import os
#
# Libraries - custom
#
from config_path_project import configPathProject
#
# Class
#
class _HelperPaths:
    """
    This class is meant to be runnable on mobile if necessary.
    """
    #
    # Public
    #
    FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT = configPathProject.FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT
    #
    # Public - get - list
    #
    def get_list_of_str_paths_in_dir( self, arg_str_path_to_directory: str ) -> [] : return [ os.path.join( arg_str_path_to_directory, item_str_name ) for item_str_name in os.listdir( arg_str_path_to_directory ) ]

    FIELD_STR_CHARACTER_WILDCARD_FOR_GETTING_ALL_DIR_CONTENTS = "*"

    def get_list_of_str_paths_in_dir_and_sub_directories( self, arg_str_path_to_directory: str ) -> [] :
        #
        # Adding the wildcard will tell glob.glob to scan all paths inside the directory
        # This *doesn't* mean 'sub directories'
        #
        str_path_to_directory = arg_str_path_to_directory
        if not self.FIELD_STR_CHARACTER_WILDCARD_FOR_GETTING_ALL_DIR_CONTENTS in str_path_to_directory : str_path_to_directory = os.path.join( str_path_to_directory, self.FIELD_STR_CHARACTER_WILDCARD_FOR_GETTING_ALL_DIR_CONTENTS, )

        list_of_paths_for_files_in_directory = glob.glob( str_path_to_directory )
        stack = deque( [ item_path for item_path in list_of_paths_for_files_in_directory if os.path.isdir( item_path ) ] )
        while stack :
            #
            # Grab the list of paths
            #
            item_list_of_str_paths = glob.glob( os.path.join( stack.pop(), self.FIELD_STR_CHARACTER_WILDCARD_FOR_GETTING_ALL_DIR_CONTENTS, ) )
            #
            # Add all these paths to the list of paths
            #
            list_of_paths_for_files_in_directory = [ *list_of_paths_for_files_in_directory, *item_list_of_str_paths, ]
            #
            # Check for directories and add those paths into the stacks
            #
            stack.extend( [ item_path_sub for item_path_sub in item_list_of_str_paths if os.path.isdir( item_path_sub ) ] )

        return list_of_paths_for_files_in_directory
    #
    # Public - get - string
    #
    def get_str_path_abs( self, arg_str_path: str ) -> str :
        #
        # Reminder: os.path.abspath() with a '~' prefix returns both the current working directory and the path *with*
        # the '~' in place.
        #
        str_path_to_return = arg_str_path
        if str_path_to_return.startswith( "~" ) : str_path_to_return = os.path.expanduser( str_path_to_return )
        # Reminder: This also accounts for '../'
        elif str_path_to_return.startswith( "." ) : str_path_to_return = os.path.abspath( str_path_to_return )
        elif not str_path_to_return.startswith( "/" ) : str_path_to_return = os.path.abspath( os.path.join( ".", str_path_to_return, ) )
        return str_path_to_return
    #
    # Public - temporarily
    #
    @contextlib.contextmanager
    def temporarily_set_cwd( self, arg_str_path_dir_dest: str ) :

        path_dir_current_working_original = os.getcwd()
        os.chdir( arg_str_path_dir_dest )
        yield
        os.chdir( path_dir_current_working_original )
#
# Public
#
helperPaths = _HelperPaths()
#
# Execution area
#
if __name__ == "__main__" : pass
































