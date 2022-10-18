#
# Libraries - native
#
import os
import sys
#
# Public
#
def get_string_path_dir_proj_root():

    string_name_file_in_dir_proj_root = "config_path_project.py"
    #
    # Go up through directories until the config file is found
    #
    string_path_dir_proj_root = os.path.abspath( sys.argv[ 0 ] )
    while True:

        if os.path.isdir( string_path_dir_proj_root ):

            if string_name_file_in_dir_proj_root in os.listdir( string_path_dir_proj_root ): break

        string_path_dir_proj_root = os.path.dirname( string_path_dir_proj_root )

    return string_path_dir_proj_root
#
# Return result to the shell
#
print( get_string_path_dir_proj_root() )
















































