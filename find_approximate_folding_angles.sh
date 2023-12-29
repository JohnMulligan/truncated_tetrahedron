#!/bin/bash

timeout 5h python3 find_approximate_folding_angles.py $1 $2 $3

timeout_exit_status=$?

if [ $timeout_exit_status -eq 124 ]; then
    exit 85
fi

exit $timeout_exit_status
