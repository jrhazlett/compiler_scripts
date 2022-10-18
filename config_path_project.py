#
# Libraries - native
#
import os
#
# Class
#
class _ConfigPathProject:

    def get_str_path_abs( self, arg_str_path_rel: str ): return os.path.join( self.FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT, arg_str_path_rel, )

    def __init__(self): self.FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT = os.path.dirname( __file__ )
#
# Public
#
configPathProject = _ConfigPathProject()

























































