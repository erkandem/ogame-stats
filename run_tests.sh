#!/usr/bin/env bash
set -e

PYTHONPATH=. pytest --cov ogame_stats/
rm -rf htmlcov
coverage html
firefox htmlcov/index.html

