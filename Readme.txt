== Build Instructions ==

This project uses a Makefile for simple build automation.
To use these commands, you need to have Python and `make` installed.

1. Run tests:
    make test

2. Compile the code (generates .pyc files):
    make build

3. Create a deployable zip package:
    make package

4. Clean up generated files:
    make clean

== Requirements ==
- Python 3.x
- pytest
- make (already installed on Linux/macOS. On Windows, use Git Bash or WSL.)
