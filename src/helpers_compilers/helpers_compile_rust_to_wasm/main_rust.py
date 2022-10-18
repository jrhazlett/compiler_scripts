#
# Libraries - custom
#
from src.helpers_compilers.helpers_compile_rust_to_wasm.helper_compile_rust_to_wasm import helperCompileRustToWasm
from src.helpers_compilers.zzz_helpers_compile_from_shell.helpers_get_path_to_dir_target.helper_get_path_to_dir_target import helperGetPathToDirProj
#
# Test area
#
if __name__ == "__main__" :
    #
    # Get the path to the project to compile
    #
    str_path_dir_project_to_compile = ""
    str_path_dir_project_to_compile = helperGetPathToDirProj.get_string_path_to_dir_target( str_path_dir_project_to_compile )
    #
    # Run compilation process
    #
    helperCompileRustToWasm.compile( str_path_dir_project_to_compile )
    #
    # Run setup for web server
    #
    helperCompileRustToWasm.setup_nodejs_server_for_testing( str_path_dir_project_to_compile )


















































