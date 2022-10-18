#
# Libraries - native
#
import os
#
# Libraries - custom
#
from src.helpers_compilers.helper_compile_go_to_wasm.support.helper_config_go import helperConfigGo
from src.helpers_disk.helpers_copy_on_disk.helper_copy_on_disk import helperCopyOnDisk
from src.helpers_disk.helpers_create_on_disk.helper_create_on_disk import helperCreateOnDisk
from src.helpers_disk.helpers_move_on_disk.helper_move_on_disk import helperMoveOnDisk
from src.helpers_disk.helpers_paths.helper_paths import helperPaths
from src.helpers_shell.helper_shell_cmd import helperShellCmd
#
# Class
#
class _HelperCompilerGo:

    def compile( self, arg_str_path_dir_project: str ) :
        #
        # Reminder: Don't auto-clear the output directory because there might be files you don't want to remove
        #
        with helperPaths.temporarily_set_cwd( arg_str_path_dir_project ) :

            helperConfigGo.print_message( "".join( [ "Current directory: ", os.getcwd( ), ] ) )
            #
            # Compile app
            #
            helperShellCmd.run_cmd( self._get_string_cmd() )
            #
            # Copy wasm_exec.js to output dir
            # Reminder: Research didn't really turn up a way to set the output dir directly in the shell cmd
            #
            self._copy_file_wasm_exec_js_to_dir_output( arg_str_path_dir_project )
            #
            # Move main.wasm to output dir
            #
            self._copy_file_main_wasm_to_output_dir( arg_str_path_dir_project )

    def _get_string_cmd( self ) -> str:

        return " ".join( [
            "".join( [ "GOOS=", "js", ] ),
            "".join( [ "GOARCH=", "wasm", ] ),
            os.path.join( "/usr/local/Cellar/go", helperConfigGo.field_str_version_for_go, "libexec/bin/go", ),
            "build",
            " ".join( [ "-o", helperConfigGo.field_str_name_file_main_wasm, ] ),
        ] )

    def _copy_dir_web_server( self, arg_str_path_dir_dest: str ):

        str_path_dir_orig = "src/helpers_compilers/helper_compile_go_to_wasm/www"
        #
        # Make dir if non-existent
        #
        str_path_dir_dest = helperConfigGo.get_str_path_dir_pkg( arg_str_path_dir_dest )

        helperCreateOnDisk.create_dir_if_non_existent( str_path_dir_dest )

        with helperConfigGo.temporarily_print_message( "".join( [ "Copying dir: ", str_path_dir_orig, ] ) ):

            helperCopyOnDisk.copy_dir_into_dir(
                arg_str_path_dir_orig = str_path_dir_orig,
                arg_str_path_dir_dest = str_path_dir_dest,
            )

    def _copy_file_main_wasm_to_output_dir( self, arg_str_path_dir_project: str ):

        with helperConfigGo.temporarily_print_message( "".join( [ "Copying ", helperConfigGo.field_str_name_file_main_wasm, ] ) ):

            helperMoveOnDisk.move_path_orig_to_path_dest(
                # origin
                os.path.join( arg_str_path_dir_project, helperConfigGo.field_str_name_file_main_wasm, ),
                # dest
                os.path.join( helperConfigGo.get_str_path_dir_pkg( arg_str_path_dir_project ), helperConfigGo.field_str_name_file_main_wasm, ),
            )

    def _copy_file_wasm_exec_js_to_dir_output( self, arg_str_path_file_dir_output: str ):
        #
        # The original path is...
        # "/usr/local/Cellar/go/1.19.1/libexec/misc/wasm/wasm_exec.js"
        #
        # COPY that file, and move it to the target output dir
        #
        str_name_file_wasm_exec_js = "wasm_exec.js"

        str_path_dir_output = helperConfigGo.get_str_path_dir_pkg( arg_str_path_file_dir_output )
        #
        # Make the dest if it doesn't already exist
        #
        helperCreateOnDisk.create_dir_if_non_existent( str_path_dir_output )

        with helperConfigGo.temporarily_print_message( "".join( [ "Copying ", str_name_file_wasm_exec_js, ] ) ) :

            helperCopyOnDisk.copy_file_from_path_orig_to_path_dest(
                # origin
                os.path.join( helperConfigGo.field_str_path_dir_goroot, "misc/wasm", str_name_file_wasm_exec_js, ),
                # dest
                os.path.join( str_path_dir_output, str_name_file_wasm_exec_js, ),
            )
#
# Public
#
helperCompilerGo = _HelperCompilerGo()













































