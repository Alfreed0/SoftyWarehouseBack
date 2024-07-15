# flake8: noqa
from config import general_settings
from .colors import Colors

DEBUG = general_settings.DEBUG


def output_ERROR(func: str, message: str = None, ex: Exception = None):
    if DEBUG:
        msg = f"---> Error : {func} -> {message}"
        if ex != None:
            file = Colors(ex.__traceback__.tb_frame.f_code.co_filename).underline_fail()
            underline_msg = Colors(f"in line {ex.__traceback__.tb_lineno}").underline_fail()
            func_err = Colors(f"{func} -> {ex}").fail()
            msg = f"---> Error : {file} {func_err} {underline_msg}"
        print(Colors(msg).fail())


def output_INFO(msg: str):
    if DEBUG:
        print(Colors(f"---> INFO: {msg}").okCyan())


def output_OK(msg: str):
    if DEBUG:
        print(Colors(f"---> OK: {msg}").okGreen())


def output_WARNING(msg: str):
    if DEBUG:
        print(Colors(f"---> WARNING: {msg}").warning())
