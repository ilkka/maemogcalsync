#!/usr/bin/env bash
nosetests --with-doctest --with-coverage --cover-package=maemogcalsync --cover-erase --noexe \
&& pep8 --show-source --show-pep8 --filename='*.py' maemogcalsync \
&& pylint maemogcalsync
