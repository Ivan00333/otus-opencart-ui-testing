import logging
import os


class Logger:
    def _config_logger(self, test_name: str) -> logging.Logger:
        """
        Настраивает и возвращает logger с именем класса-наследника
        и пишет лог и в файл, и в консоль.
        """
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        os.makedirs("logs", exist_ok=True)
        log_file = f"logs/{test_name}.log"

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
