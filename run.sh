#!/bin/bash
mlflow server --host 0.0.0.0 --port 5000
python3 scripts/houseprice.py