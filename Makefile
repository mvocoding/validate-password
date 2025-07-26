.PHONY: test build package clean

# Run unit tests using pytest
test:
	pytest

# Simulate a build step (compiling .pyc files)
build:
	python -m compileall validate_password.py

# Create a zip package of the app
package:
	zip -r dist.zip validate_password.py

# Clean build artifacts
clean:
	rm -rf __pycache__ dist.zip
