"""
This library is built exclusively for handling non-database files on desktops
"""
#
# Libraries - native
#
import codecs
import io
import json
import os
#
# Class
#
class _HelperFiles:
    #
    # Public - get
    #
    def get_dict_from_file( self, arg_str_path_file: str ) -> {}:

        with io.open( arg_str_path_file, encoding = "utf-8", ) as file : return json.loads( file.read( ) )
    #
    # Public - write
    #
    def write_dict_to_file( self, arg_dict: {}, arg_str_path_file: str ):
        #
        # Create destination directory if it doesn't exist
        #
        str_path_to_dir_parent = os.path.dirname( arg_str_path_file )
        if not os.path.exists( str_path_to_dir_parent ) : os.makedirs( str_path_to_dir_parent )
        #
        # Write to file
        #
        with codecs.open( arg_str_path_file, "w", "utf8", ) as file : file.write( json.dumps( arg_dict, indent = 4, ) )
#
# Public
#
helperFiles = _HelperFiles()
#
# Test area
#
if __name__ == "__main__" : pass






















































