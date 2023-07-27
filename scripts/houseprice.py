import argparse
import logging
import logging.config
import os
import os.path as op
import pickle
import sys
import warnings

import mlflow
import mlflow.sklearn
import numpy as np
from ingest_data import mlflow_data_ingest
from score import mlflow_score
from train import mlflow_train

import housinglib as hlb


def configure_logger(
    logger=None, cfg=None, log_file=None, console=True, log_level="DEBUG"
):
    if not cfg:
        logging.config.dictConfig(LOGGING_DEFAULT_CONFIG)
    else:
        logging.config.dictConfig(cfg)

    logger = logger or logging.getLogger()

    if log_file or console:
        for hdlr in logger.handlers:
            logger.removeHandler(hdlr)

        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(getattr(logging, log_level))
            logger.addHandler(fh)

        if console:
            sh = logging.StreamHandler()
            sh.setLevel(getattr(logging, log_level))
            logger.addHandler(sh)

    return logger


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    lib_path = op.join(op.dirname(op.abspath(__file__)), "..")
    sys.path.append(lib_path)

    parser = argparse.ArgumentParser(description="data folder path")
    parser.add_argument("--input_path", nargs="?")
    parser.add_argument("--output_path", nargs="?")
    parser.add_argument("--log_level", nargs="?")
    parser.add_argument("--log_path", nargs="?")
    parser.add_argument("--no_console_log", nargs="?")
    parser.add_argument("--model_path", nargs="?")
    parser.add_argument("--res_path", nargs="?")
    args = parser.parse_args()

    if args.log_level is None:
        log_level = "DEBUG"
    else:
        log_level = args.log_level

    if args.log_path is None:
        log_file = None
    else:
        log_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "logs",
            "houseprice.log",
        )

    if args.no_console_log is None:
        no_console_log = True
    else:
        no_console_log = args.no_console_log

    HERE = op.dirname(op.abspath(__file__))

    if args.input_path is None:
        HOUSING_PATH = op.join(HERE, "..", "data", "raw")
    else:
        HOUSING_PATH = args.input_path

    if args.output_path is None:
        output_path = op.join(HERE, "..", "artifacts")
    else:
        output_path = args.output_path

    if args.model_path is None:
        path = op.join(HERE, "..", "artifacts")
        with open(path + "/model_pickle.pkl", "rb") as f:
            final_model = pickle.load(f)
    else:
        with open(args.model_path, "rb") as f:
            final_model = pickle.load(f)

    if args.res_path is None:
        res_path = op.join(HERE, "..", "artifacts")
    else:
        res_path = args.res_path

    LOGGING_DEFAULT_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s \
                    - %(funcName)s:%(lineno)d - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "simple": {"format": "%(message)s"},
        },
        "root": {"level": "DEBUG"},
    }

    logger = configure_logger(
        log_file=log_file, console=no_console_log, log_level=log_level
    )
    with mlflow.start_run():
        with mlflow.start_run(nested=True):
            mlflow_data_ingest(HOUSING_PATH, HERE)

        with mlflow.start_run(nested=True):
            mlflow_train(HERE, logger, output_path)

        with mlflow.start_run(nested=True):
            mlflow_score(HERE, res_path, logger, final_model)
