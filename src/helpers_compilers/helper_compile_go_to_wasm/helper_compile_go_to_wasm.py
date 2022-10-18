"""
GOOS=js GOARCH=wasm go build -o main.wasm

cp "$(go env GOROOT)/misc/wasm/wasm_exec.js" .


Command which works in this context...
GOOS=js GOARCH=wasm /usr/local/Cellar/go/1.19.1/libexec/bin/go build -o main.wasm



How the compilation process works...

- This runs the cmd stored in self._get_str_cmd()
- At this stage, the script has to chase down the resulting files
- Move "/usr/local/Cellar/go/1.19.1/libexec/misc/wasm/wasm_exec.js" to the output directory
- Move the resulting "main.wasm" from the project director to the destination

This has two benefits:
- It keeps the actual source area clean
- It consolidates the results into a single directory
    Why Go doesn't do this by default, or have a clear way to set the compilation output dir directly, is a mystery
"""
#
# Libraries - custom
#
from src.helpers_compilers.helper_compile_go_to_wasm.support.helper_compiler_go import helperCompilerGo
from src.helpers_compilers.helper_compile_go_to_wasm.support.helper_setup_server_go import helperSetupServerGo
#
# Class
#
class _HelperCompileGoToWasm :
    #
    # Public - wrappers
    #
    def compile( self, arg_str_path_dir_project: str ): helperCompilerGo.compile( arg_str_path_dir_project )

    def setup_server( self, arg_str_path_dir_project: str ): helperSetupServerGo.setup_server( arg_str_path_dir_project )
#
# Public
#
helperCompileGoToWasm = _HelperCompileGoToWasm()













































