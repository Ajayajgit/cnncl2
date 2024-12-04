import os
import sys
import logging

log_str = "[%(asctime)s: %(levelname)s: %(module)s %(message)s]"
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)
log_path = os.path.join(logs_dir, "running_logs.log")
logging.basicConfig(
    level= logging.INFO,
    format= log_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnclassifierlogger")