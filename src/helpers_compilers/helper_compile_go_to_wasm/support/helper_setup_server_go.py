#
# Libraries - native
#
import os
#
# Libraries - custom
#
from config_path_project import configPathProject
from src.helpers_compilers.helper_compile_go_to_wasm.support.helper_config_go import helperConfigGo
from src.helpers_disk.helpers_copy_on_disk.helper_copy_on_disk import helperCopyOnDisk
#
# Class
#
class _HelperSetupServerGo:

    def setup_server( self, arg_str_path_dir_project: str ) :

        str_path_dir_server_orig = os.path.join(
            configPathProject.FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT,
            "src/helpers_compilers/helper_compile_go_to_wasm/copy/www",
        )
        helperCopyOnDisk.copy_dir_into_dir(
            arg_str_path_dir_orig = str_path_dir_server_orig,
            arg_str_path_dir_dest = arg_str_path_dir_project,
        )
        self._copy_file_index_to_pkg( arg_str_path_dir_project )

    def _copy_file_index_to_pkg( self, arg_str_path_dir_project: str ):

        str_name_file = "index.html"

        str_path_file_orig = os.path.join(
            configPathProject.FIELD_PATH_TO_DIR_ROOT_FOR_PROJECT,
            "src/helpers_compilers/helper_compile_go_to_wasm/copy/www/pkg_orig",
            str_name_file,
        )
        str_path_file_dest = os.path.join(
            helperConfigGo.get_str_path_dir_pkg( arg_str_path_dir_project ),
            str_name_file,
        )
        with helperConfigGo.temporarily_print_message( "".join( [ "Copying file: ", str_path_file_orig, ] ) ):

            helperCopyOnDisk.copy_file_from_path_orig_to_path_dest(
                arg_str_path_to_file_orig = str_path_file_orig,
                arg_str_path_to_dest = str_path_file_dest,
            )
#
# Public
#
helperSetupServerGo = _HelperSetupServerGo()










































