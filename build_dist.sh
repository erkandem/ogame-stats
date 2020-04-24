#!/usr/bin/env bash

rm -rf build
rm -rf dist
rm -rf ogame_stats.egg-info
python setup.py build sdist bdist_wheel
