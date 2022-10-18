#
# Libraries - custom
#
from src.helpers_compilers.helper_compile_rust_to_wasm.helper_compile_rust_to_wasm import helperCompileRustToWasm
from src.helpers_compilers.helpers_get_path_to_dir_proj.helper_get_path_to_dir_proj import helperGetPathToDirProj
#
# Test area
#
if __name__ == "__main__" :
    #
    # Get the path to the project to compile
    #
    str_path_dir_project_to_compile = ""
    str_path_dir_project_to_compile = helperGetPathToDirProj.get_string_path_to_dir_proj( str_path_dir_project_to_compile )
    #
    # Run compilation process
    #
    helperCompileRustToWasm.compile( str_path_dir_project_to_compile )
    #
    # Run setup for web server
    #
    helperCompileRustToWasm.setup_nodejs_server_for_testing( str_path_dir_project_to_compile )


















































