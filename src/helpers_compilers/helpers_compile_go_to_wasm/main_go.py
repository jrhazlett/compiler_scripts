#
# Libraries - custom
#
from src.helpers_compilers.helpers_compile_go_to_wasm.helper_compile_go_to_wasm import helperCompileGoToWasm
from src.helpers_compilers.zzz_helpers_compile_from_shell.helpers_get_path_to_dir_proj.helper_get_path_to_dir_proj import helperGetPathToDirProj
#
# Test area
#
if __name__ == "__main__":
    #
    # Get the path to the project to compile
    #
    str_path_dir_project_to_compile = "/Users/jameshazlett/Projects/wasm/go/project_webassembly"
    str_path_dir_project_to_compile = helperGetPathToDirProj.get_string_path_to_dir_proj( str_path_dir_project_to_compile )
    #
    # Run compilation process
    #
    helperCompileGoToWasm.compile( str_path_dir_project_to_compile )
    #
    # Run setup for web server
    #
    helperCompileGoToWasm.setup_server( str_path_dir_project_to_compile )










































