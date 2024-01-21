#!/bin/bash

timeout 4h python3 sweep_optimized_folding_angles.py $1 $2

timeout_exit_status=$?

if [ $timeout_exit_status -eq 124 ]; then
    exit 85
fi

exit $timeout_exit_status