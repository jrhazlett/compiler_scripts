#
# Libraries - native
#
import os
#
# Libraries - custom
#
from config_path_project import configPathProject
from src.helpers_disk.helpers_copy_on_disk.helper_copy_on_disk import helperCopyOnDisk
from src.helpers_disk.helpers_files.helper_files import helperFiles
from src.helpers_disk.helpers_paths.helper_paths import helperPaths
from src.helpers_compilers.helper_compile_rust_to_wasm.support.helper_printing import helperPrinting
from src.helpers_shell.helper_shell_cmd import helperShellCmd
#
# Class
#
class _HelperSetupWebServer:

    def setup_nodejs_server_for_testing( self, arg_str_path_dir_project: str ):

        helperPrinting.print_message( "Setting up nodejs server for testing..." )

        with helperPaths.temporarily_set_cwd( arg_str_path_dir_project ):

            helperPrinting.print_message( "".join( [ "cwd: ", os.getcwd(), "...", ] ) )
            helperShellCmd.run_cmd( "npm init wasm-app www" )

            self._setup_nodejs_server_within_dir( arg_str_path_dir_project )

        self._copy_additional_files( arg_str_path_dir_project )

    def _setup_nodejs_server_within_dir( self, arg_str_path_dir_project ):

        str_path_dir_server = os.path.join( arg_str_path_dir_project, "www", )

        with helperPaths.temporarily_set_cwd( str_path_dir_server ):

            helperShellCmd.run_cmd( "npm i" )

            self._update_package_json( arg_str_path_dir_project, str_path_dir_server, )

            helperShellCmd.run_cmd( "npm i" )
            #
            # By this point, the wasm file should be importable
            #

    def _update_package_json( self, arg_str_path_dir_project: str, arg_str_path_dir_server: str ):

        str_path_file_package_json = os.path.join( arg_str_path_dir_server, "package.json", )
        #
        # Get dict_json from file
        #
        dict_package_json = helperFiles.get_dict_from_file( str_path_file_package_json )
        #
        # Add dependencies if not already present
        #
        dict_package_json = self._get_dict_with_dependencies_added(
            arg_dict_package_json = dict_package_json,
            arg_str_path_dir_project = arg_str_path_dir_project,
        )
        #
        # Write to file
        #
        helperFiles.write_dict_to_file(
            arg_dict = dict_package_json,
            arg_str_path_file = str_path_file_package_json,
        )

    def _get_dict_with_dependencies_added( self, arg_dict_package_json: {}, arg_str_path_dir_project: str ):

        str_name_for_wasm_package = self._get_str_name_for_wasm_package( arg_str_path_dir_project )

        helperPrinting.print_message( "".join( [ "Adding dependency: ", str_name_for_wasm_package, "...", ] ) )

        str_key_dependencies = "dependencies"
        if not str_key_dependencies in arg_dict_package_json.keys( ) : arg_dict_package_json[ str_key_dependencies ] = { }
        dict_dependencies = arg_dict_package_json[ str_key_dependencies ]
        #
        # Add dependency line
        #
        dict_dependencies[ str_name_for_wasm_package ] = "file:../pkg"

        return arg_dict_package_json

    def _get_str_name_for_wasm_package( self, arg_str_path_dir_project: str ):

        str_path_dir_pkg = os.path.join( arg_str_path_dir_project, "pkg", )

        list_of_paths_in_dir = [
            item_path
            for item_path in helperPaths.get_list_of_str_paths_in_dir_and_sub_directories( str_path_dir_pkg )
            if item_path.endswith( ".js" ) and not item_path.endswith( "_bg.js" )
        ]
        str_name = os.path.basename( list_of_paths_in_dir[ 0 ] )
        str_name = str_name.split( "." )[ 0 ]
        return str_name.replace( "_", "-", )

    def _copy_additional_files( self, arg_str_path_dir_project: str ):

        str_path_dir_www = os.path.join( arg_str_path_dir_project, "www", )
        str_path_file_orig = configPathProject.get_str_path_abs( "src/helpers_compilers/helper_compile_rust_to_wasm/copy/run_server.sh" )

        helperPrinting.print_message( "".join( [ "Copying file: ", str_path_file_orig, "...", ] ) )

        helperCopyOnDisk.copy_file_from_path_orig_to_path_dest(
            str_path_file_orig,
            os.path.join( str_path_dir_www, os.path.basename( str_path_file_orig ), ),
        )

helperSetupWebServer = _HelperSetupWebServer()
































