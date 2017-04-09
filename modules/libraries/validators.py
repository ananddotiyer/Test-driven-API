# -*- encoding: utf-8 -*-
#Forked from https://github.com/nano-labs/json_schema

"""Standard validators to be used by json_schema."""

import re
from datetime import datetime


class StringValidator:

    """Class only for grouping the validator methods.

    Validation:
        Check if the item is a string and if the maximum size doesn't exceed max length.

        Possible formats: "Str",  "Str: max length"

        Former: "Str: 10"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("str")

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of the string."""
        if isinstance(item, str) or isinstance(item, unicode):
            if item_schema.startswith("str:"):
                try:
                    tamanho = int(item_schema.replace("str:", ""))
                    if len(item) > tamanho:
                        return False
                    return True
                except ValueError:
                    return item == item_schema.replace("str:", "")
            return True
        return False


class IntValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the item is an Int and if the value is between min and max

    Possible formats:
        "int"
        "int:min:max

    Ex:
        "int:-10:10"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("int")

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of fact of int."""
        if not isinstance(item, int):
            return False
        if item_schema == "int":
            return True
        m = re.match("int\:(\-?[0-9]+)\:(\-?[0-9]+)", item_schema)
        if m:
            inferior, superior = m.groups()
            if item >= int(inferior) and item <= int(superior):
                return True
        return False


class FloatValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the item is a Float and if the value is between min and max

    Possible formats:
        "float"
        "float:min:max

    Ex:
        "float:-10.5:10.5"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("float")

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of float fact."""
        if not isinstance(item, float):
            return False
        if item_schema == "float":
            return True
        m = re.match("float\:(\-?[0-9]+\.[0-9]+)\:(\-?[0-9]+\.[0-9]+)",
                     item_schema)
        if m:
            inferior, superior = m.groups()
            if item >= float(inferior) and item <= float(superior):
                return True
        return False


class UrlValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the match item in a url

    Possible formats:
        "url"

    Ex:
        "url"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema == "url"

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of the url."""
        regex = re.compile(r'^(?:http|ftp)s?://'  # HTTP, HTTPS, FTP, FTPS
                           # Domain
                           r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                           # Localhost
                           r'localhost|'
                           # IP
                           r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                           # Port
                           r'(?::\d+)?'
                           r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        try:
            return True if regex.match(item) else False
        except:
            return False


class BooleanValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the match item in a boolean

    Possible formats:
        "bool"
        "bool:True"
        "bool:False"

    Ex:
        "bool"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("bool")

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of the bool."""
        if ":" in item_schema:
            value = item_schema.split(":")[1] == "True"
            return item == value
        return isinstance(item, bool)


class RegexValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the match item in a regex

    Possible formats:
        "regex:regex string"

    Ex:
        "regex:^[0-9]{2}\\\\:[0-9]{2}\\\\:[0-9]{2}$"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        if schema.startswith("regex:"):
            re.compile(schema.replace("regex:", ""))
            return True
        return False

    @classmethod
    def validator(cls, item, item_schema):
        """Validator of the Regex."""
        regex = re.compile(item_schema.replace("regex:", ""))
        return True if regex.match(item) else False


class AnyValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Accept anything

    Possible formats:
        "any"

    Ex:
        "any"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("any")

    @classmethod
    def validator(cls, item, item_schema):
        """How can anything ever return True?"""
        return True


class NullValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the value is "null"

    Possible formats:
        "null"

    Ex:
        "null"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema == "null"

    @classmethod
    def validator(cls, item, item_schema):
        """How can anything ever return True?"""
        return item is None


class PythonValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the value passes in a defined python expression

    Possible formats:
        "Python: python_code"

    Ex:
        "python:value.upper() == value"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("python:")

    @classmethod
    def validator(cls, item, item_schema):
        """Test the python code."""
        src = item_schema.replace("python:", "")
        src = """def temporary_function(value):\n    return %s""" % src
        try:
            exec(src)
            return temporary_function(item)
        except:
            return False


class DatetimeValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the value confers on a datetime.strptime

    Possible formats:
        "datetime:datetime string formatter"

    Ex:
        "datetime:%Y-%m-%d"
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("datetime:")

    @classmethod
    def validator(cls, item, item_schema):
        """Tests the datetime.strptime ()."""
        string_formater = item_schema.replace("datetime:", "")
        try:
            datetime.strptime(item, string_formater)
            return True
        except:
            return False


class EmptyValidator:

    """
    Class only for grouping the validator methods.

    Validation:
        Check if the value is empty

    Possible formats:
        "Empty: list"
        "Empty: dict"
        "Empty: hash"
        "Empty: object"

    Dict, hash and object are synonymous.
    """

    @classmethod
    def schema_lookout(cls, schema):
        """Check if given schema must be validated by this Validator."""
        return schema.startswith("empty:")

    @classmethod
    def validator(cls, item, item_schema):
        """Tests whether the item is of type data and is empty."""
        tipo = item_schema.replace("empty:", "")
        tipos = {"dict": dict, "hash": dict, "object": dict, "list": list}
        return isinstance(item, tipos[tipo]) and len(item) == 0
