#
# Libraries - native
#
import os.path
import sys
#
# Class
#
class _HelperGetPathToDirProj:

    def get_string_path_to_dir_proj(self, arg_string_path_dir: str) -> str:
        #
        # Defs
        #
        bool_raise_error = False
        bool_string_path_is_dir = True
        err_to_print = None
        string_path_to_return = arg_string_path_dir
        #
        # Prioritize the in-module definition for the path
        # If string_path_to_return is not in a 'true' state, then try to
        # replace the value with that in the arguments
        #
        if not string_path_to_return:

            # Only attempt this is there's at least one argument
            if len( sys.argv ) > 0: string_path_to_return = sys.argv[ 0 ]
            else : bool_raise_error = True
        #
        # At this point, the string *should* have something resembling a passed value
        #
        if not bool_raise_error and not os.path.isdir( string_path_to_return ):

            bool_raise_error = True
            bool_string_path_is_dir = False
        #
        # If bool_raise_error is somehow True, then raise an error
        #
        if bool_raise_error:
            print( "Error: No viable path provided for the target project to compile.\n" )
            print( "arg_string_path_dir =", arg_string_path_dir, "\n", )
            print( "bool_string_path_is_dir =", bool_string_path_is_dir, "\n", )
            print( "len( sys.argv ) =", len( sys.argv ), "\n", )
            print( "err_to_print =", err_to_print, "\n", )
            raise()
        #
        # If we get this far, then all checks passed
        #
        return string_path_to_return
#
# Public
#
helperGetPathToDirProj = _HelperGetPathToDirProj()




















































