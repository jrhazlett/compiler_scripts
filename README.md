# Compiler Scripts

This script package's main purpose is to give the Rust and Go wasm compilation processes
the same results.

I'll add more features if practical, but the web assembly development process has unique
quirks warranting the scripts.

## Upfront warnings

This package *does* include code which manipulates files outside of the project. While
there are validation functions to help with preventing incidental damage, this is very
much a "run at your own risk" repo.

I recommend reading the code, and determining for yourself if you want to actually make
use of it.

This package is not designed to run like a pip-style package. You won't find it on pip.

I commented out the code in setup.py, so running it shouldn't accomplish anything. Its
mainly here for record keeping.

All the safeguards implemented in the disk manipulations are meant for a Mac-style
file system. This package is *not* tested on Windows.

## Now onto the package...

### Main features

- Supports compiling Go and Rust web assembly (wasm) files
- Provides a consistent file layout across both languages
- Ideally, to do a basic test, you should be able to plug in a path to a project you want
to compile, and it *should* work out of the box

### Caveats 

Your environment needs to support the languages...

For mac os

https://formulae.brew.sh/formula/go
https://formulae.brew.sh/formula/rust
https://formulae.brew.sh/formula/wasm-pack (for Rust)
https://formulae.brew.sh/formula/node (for the Rust web server)

You should also familiarize yourself with the manual compilation processes...

Go

https://golangbot.com/webassembly-using-go/

Rust

https://rustwasm.github.io/book/game-of-life/hello-world.html

### How the package works...

Both scripts should result in similar outputs as outlined by the end of Rust's hello-world
process; outlined here:

https://rustwasm.github.io/book/game-of-life/hello-world.html

When I followed this, I found Rust's approach much more intuitive, so I built the Go
compilation script produce the same results.

Both languages are setup here to do the following:

- Compile the wasm files and move / copy them into <project dir>/pkg
- Create a test server in <project dir>/www
- After running both of the above, the resulting servers should be runnable "out-of-the-box"

Both the compilation process and web server creation are distinctly separate tasks from each other.
These can also be ran independently of each other.

These processes can be configured at the following paths:
src/helpers_compilers/helper_compile_go_to_wasm/main_go.py
src/helpers_compilers/helper_compile_rust_to_wasm/main_rust.py

This project also supports shell commands. The associated scripts can be found here:
src/helpers_compilers/helper_compile_go_to_wasm/run_script_go.sh
src/helpers_compilers/helper_compile_rust_to_wasm/run_script_rust.sh

Go's web server is stored within this repo, and can be found here:
src/helpers_compilers/helper_compile_go_to_wasm/www

### File layouts

This is entirely built around the idea behind "re-useable" code. A lot of the 
'broad use case' code can be found in...

src/helpers_disk

src/helpers_shell

The files under...

src/helpers_compilers

...are generally language specific.

### General workflow...

The high-level workflow can be seen in the default `main_<language>.py` files.

In both cases, the compilation process generates the relevant .wasm files and puts
them in the ./pkg directory of the target project.

The Go script will copy the wasm_exec.js file from its directory and put it in the 
same pkg dir.

Building the web server...

This involves its own separate function call processes, which can also be found in the 
'main'-files.

The Go build will produce a Go server.

The Rust build will produce a nodejs server.

Both of these can be found in ./www within the project directory.

The Rust process will update the package.json file with the wasm asset as a dependency. The
relative path will assume the asset is in the ./pkg dir.

The one major difference between the two builds is the Go process will put index.html in the pkg
directory, while Rust will leave it in the Rust project's root directory.

The reason for this is two-fold:
- These files come about in the Rust process as part of the third party build. I'll defer to it.
- In Go's case, the file needs to be copied over. The file also directly references
the wasm file's relative path.

In either case, if you cd into <project>/www, and then run `sh run_server.sh` and both should work.

One cautionary note: Both `run_server.sh` use `#!/bin/zsh`, depending on your environment, you might 
need to change it to `#!/bin/bash`.

### Addressing any questions

#### Why is this in Python?

This package deals primarily with file management overhead, and at no point plays
a direct role in running the resulting files outputted by this process.

Rust is overkill with a lot of minutiae to manage, and Go appears to have issues 
calling its own compiler from the shell.

BASH isn't super-accommodating to complex operations.

The only other language I would seriously consider is javascript (nodejs).














































