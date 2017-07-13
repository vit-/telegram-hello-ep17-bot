#!/usr/bin/env bash

VENV_DIR='./.venv'

pyvenv $VENV_DIR
$VENV_DIR/bin/pip install -r requirements.txt
