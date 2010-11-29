#!/usr/bin/env bash
pep8 --show-source --show-pep8 --filename='*.py' maemogcalsync \
&& pylint maemogcalsync
