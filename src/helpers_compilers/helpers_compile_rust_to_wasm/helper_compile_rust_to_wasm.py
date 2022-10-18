"""
To set this up...

brew install rust
brew install wasm-pack

Info source:
https://rustwasm.github.io/book/game-of-life/hello-world.html


How compilation works...
- Process runs 'wasm-pack build' and this leads to a pretty straight forward creation of ./pkg

Shortcut for building a web server...
- Runs 'npm init wasm-app www'
- This creates a new server in ./www
- Adds the wasm package as a dependency in ./www/package.json

"""
#
# Libraries - native
#
import os
#
# Libraries - custom
#
from src.helpers_disk.helpers_paths.helper_paths import helperPaths
from src.helpers_compilers.helpers_compile_rust_to_wasm.support.helper_printing import helperPrinting
from src.helpers_compilers.helpers_compile_rust_to_wasm.support.helper_setup_web_server import helperSetupWebServer
from src.helpers_shell.helper_shell_cmd import helperShellCmd
#
# Class
#
class _HelperCompileRustToWasm:
    #
    # Public - wrappers
    #
    def compile( self, arg_str_path_dir_project: str ):
        #
        # This runs the shell cmd:
        # wasm-pack build
        #
        # The cmd creates <project dir>/pkg
        #
        helperPrinting.print_message( "Compiling wasm..." )

        with helperPaths.temporarily_set_cwd( arg_str_path_dir_project ):

            helperPrinting.print_message( "".join( [ "cwd: ", os.getcwd(), "...", ] ) )

            helperShellCmd.run_cmd( "wasm-pack build" )

    def setup_nodejs_server_for_testing( self, arg_str_path_dir_project: str ): helperSetupWebServer.setup_nodejs_server_for_testing( arg_str_path_dir_project )
#
# Public
#
helperCompileRustToWasm = _HelperCompileRustToWasm()























































