import base64
import binascii
import logging
import tkinter as tk

from ast import literal_eval
from json import dumps, loads
from typing import List, Tuple

__author__ = 'eagle_vis'

logger = logging.getLogger(__name__)


class IncompatibleVersionError(Exception):
    pass


class InvalidValueError(Exception):
    pass


class SettingsVariable:
    def __init__(self, name: str, variable: tk.Variable, options: (List, Tuple)=None, on_update=None):
        self.name = name
        self.variable = variable
        self.options = options
        self.on_update = on_update

    def get(self) -> str:
        value = self.variable.get()
        if self.options is not None and len(self.options) and value not in self.options:
            raise InvalidValueError('Invalid value {} for {}'.format(value, self.name))

        return str(value)

    def set(self, value: str):
        try:
            new_val = None
            if isinstance(self.variable, tk.BooleanVar):
                new_val = bool(literal_eval(value))
            elif isinstance(self.variable, tk.IntVar):
                new_val = int(value)
            elif isinstance(self.variable, tk.DoubleVar):
                new_val = float(value)
            elif isinstance(self.variable, tk.StringVar):
                new_val = str(value)

            if self.options is not None and len(self.options):
                if new_val not in self.options:
                    raise ValueError

            self.variable.set(new_val)
            if callable(self.on_update):
                self.on_update()
        except Exception as e:
            logger.exception('Invalid value supplied for variable {}: "{}" - '.format(self.name, value, e))
            raise ValueError


class SettingsStringIO:
    def __init__(self, version: str, compatible_versions: List[str], variables: List[SettingsVariable], call_after_update=None):
        self.version = version
        self.compatible_version = compatible_versions
        self.variables = variables
        self.call_after_update = call_after_update

        self.required_keys = [v.name for v in variables]
        self.required_keys.append('rv')
        self.required_keys.sort()

    def construct(self) -> str:
        data_dict = {
            'rv': self.version,
        }

        for var in self.variables:
            data_dict[var.name] = var.get()
        dict_string = bytes(dumps(data_dict, indent=None), 'ascii')

        crc_string = '{:08x}'.format(binascii.crc32(dict_string) & 0xffffffff)

        return base64.b64encode(dict_string + bytes(crc_string, 'ascii'))

    def parse(self, string: str) -> bool:
        data_string = base64.b64decode(string, validate=True)
        given_crc = data_string[-8:].decode('ascii')
        data_string = data_string[:-8]

        computed_crc_string = '{:08x}'.format(binascii.crc32(data_string) & 0xffffffff)

        if computed_crc_string != given_crc:
            raise InvalidValueError

        data_dict = loads(data_string)

        if self.version != data_dict['rv']:
            raise IncompatibleVersionError

        if len(data_dict.keys()) != len(self.required_keys):
            return False

        for k in self.required_keys:
            if k not in data_dict:
                return False

        for var in self.variables:
            var.set(data_dict[var.name])

        if callable(self.call_after_update):
            self.call_after_update()

        return True
