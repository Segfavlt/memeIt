#!/bin/bash
has_package=$(python3 check.py)

if [[ $has_package == "yes" ]]
then
  python3 setup.py build
  python3 setup.py install --user
else
  echo "You need python3 setuptools installed"
fi
