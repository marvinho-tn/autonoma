#!/bin/bash

# Check if apt is available
if hash apt 2>/dev/null; then
  echo "apt is available, using it to install dependencies"
  sudo apt-get update
  sudo apt-get install -y python3 python3-pip
else
  echo "apt is not available, using brew to install dependencies"
  # Install brew if it's not already installed
  if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi
  # Use brew to install python3 and pip3
  brew install python
  alias python=python3
  alias pip=pip3
  # Install required packages using pip
  pip install -r requirements.txt
fi

# Run the automa.py script
python3 src/automa.py