#!/usr/bin/env bash
# black tests ogame_stats --line-length 100
rm -rf build
rm -rf dist
rm -rf ogame_stats.egg-info
python setup.py build sdist bdist_wheel
