#!/usr/bin/env bash
SCRIPTDIR=$(dirname "$0")
"$SCRIPTDIR/run_unit_tests.sh" && "$SCRIPTDIR/run_pep8_and_lint.sh"
