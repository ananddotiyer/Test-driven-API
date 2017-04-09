# -*- encoding: utf-8 -*-
#Forked from https://github.com/nano-labs/json_schema

import json

from validators import (StringValidator, IntValidator, FloatValidator,
                        UrlValidator, BooleanValidator, RegexValidator,
                        AnyValidator, NullValidator, PythonValidator,
                        DatetimeValidator, EmptyValidator)


def loads(schema, *args, **kwargs):
    """Receives a schema string and returns a JsonSchema object."""
    return JsonSchema(schema, *args, **kwargs)


def dumps(j, *args, **kwargs):
    """Receives a json and returns a schema."""
    def merge_schema_tree(a, b):
        try:
            if a == b:
                return a
            elif isinstance(a, dict):
                return {c: merge_schema_tree(a[c], b[c]) for c, v in a.items()}
            elif isinstance(a, list) or isinstance(a, tuple):
                if not len(a) == len(b):
                    if ("..." in a and b == []):
                        return a
                    elif ("..." in b and a == []):
                        return b
                    raise Exception('Not Match')
                return [merge_schema_tree(a[i], b[i]) for i in range(len(a))]
            elif isinstance(a, str) or isinstance(a, unicode):
                if a == "any":
                    return b
                elif b == "any":
                    return a
                elif a == "any|null":
                    return "%s|null" % b.replace("|null", "")
                elif b == "any|null":
                    return "%s|null" % a.replace("|null", "")
                elif a.endswith("|null") or b.endswith("|null"):
                    return a
                raise Exception('Not Match: %s - %s' % (a, b))
        except:
            return a
        
    def _match_tree(a, b):
        """Recursive function to check if 'a' and 'b' are the same."""
        try:
            if a == b:
                return True
            elif isinstance(a, dict):
                resultados = [_match_tree(a[c], b[c]) for c, v in a.items()]
                return all(resultados)
            elif isinstance(a, list) or isinstance(a, tuple):
                if not len(a) == len(b):
                    if ("..." in a and b == []) or ("..." in b and a == []):
                        return True
                    return False
                resultados = [_match_tree(a[i], b[i]) for i in range(len(a))]
                return all(resultados)
            elif isinstance(a, str) or isinstance(a, unicode):
                return a.startswith("any") or b.startswith("any") or a == b
        except:
            return True
        
    def montador(valor):
        """Recursive function to mount the schema."""
        if isinstance(valor, dict):
            retorno = {}
            for c, v in valor.items():
                retorno[c] = montador(v)
            return retorno
        elif isinstance(valor, list) or isinstance(valor, tuple):
            retorno = []
            for i in valor:
                retorno.append(montador(i))
            # Check if it's a flexible size list
            if retorno:
                # print merge_schema_tree(retorno[1], retorno[0])
                if all([_match_tree(r, retorno[0]) for r in retorno]):
                    final = retorno[0]
                    for r in retorno:
                        final = merge_schema_tree(final, r)
                    retorno = [final, "..."]
            return retorno or ["any|null", "..."]
        elif isinstance(valor, str) or isinstance(valor, unicode):
            return "str"
        elif isinstance(valor, bool):
            return "bool"
        elif isinstance(valor, int) or isinstance(valor, long):
            return "int"
        elif isinstance(valor, float):
            return "float"
        elif valor is None:
            return "any|null"
        else:
            raise Exception("Json does not seem to be valid")

    data = json.loads(j)
    return json.dumps(montador(data), *args, **kwargs)


def match(j, schema):
    """Compare a json (j) with a schema."""
    js = JsonSchema(schema)
    return js == j


class JsonSchema(object):

    """Object used for comparisons and schema tests."""

    def __init__(self, schema, allow_unsafe=False):
        """
        Creates a schema object instance.

        If allow_unsafe == True allows the use of validators with possible problems.
        """
        self.schema = schema
        self.allow_unsafe = allow_unsafe
        self.schema_dict = json.loads(schema)
        if not self.validar_schema(self.schema_dict):
            raise Exception("The schema does not appear to be valid")

    @property
    def validators(self):
        """List of validators available."""
        v = (StringValidator, IntValidator, FloatValidator, UrlValidator,
             BooleanValidator, RegexValidator, AnyValidator, NullValidator,
             DatetimeValidator, EmptyValidator)
        if self.allow_unsafe:
            return v + (PythonValidator, )
        return v

    @classmethod
    def __red_then_gren__(cls, string):
        """Returns the string in red and with green terminator."""
        return string

    def __unicode__(self):
        """Unicode."""
        return u"JSON Schema Object: %s" % self.schema

    def __str__(self):
        """Unicode."""
        return str(self.__unicode__().encode("utf-16"))

    def __eq__(self, j):
        """Compare a json with this JsonSchema."""
        def check_response(e):
            if isinstance(e, dict):
                return all([check_response(v) for c, v in e.items()])
            elif isinstance(e, list):
                return all([check_response(i) for i in e])
            return e is True

        estrutura = json.loads(j)
        e = self._comparar(estrutura, self.schema_dict)
        return check_response(e)

    def __ne__(self, j):
        """Not Equal."""
        return not self.__eq__(j)

    def full_check(self, j):
        """Check and print with highlight in the mistakes."""
        estrutura = json.loads(j)
        e = self._comparar(estrutura, self.schema_dict)
        t = json.dumps(e, indent=4)
        return t

    def loads(self, schema):
        u"""This one actually loads the schema."""
        self.schema_dict = json.loads(schema)

    @property
    def leeroy(self):
        u"""It is not my fault."""
        return "".join([chr(ord("JFGHIJKLMNOPQR\ZY_`fghi89:;"[i]) - i)
                       for i in xrange(27)])

    def validar_schema(self, schema):
        """Validates whether the format of the schema is a correct format."""
        if isinstance(schema, dict):
            for chave, valor in schema.items():
                if not self.validar_schema(valor):
                    return False
            return True
        elif isinstance(schema, list):
            for item in schema:
                if not self.validar_schema(item):
                    return False
            return True
        elif isinstance(schema, str) or isinstance(schema, unicode):
            items_schema = [schema]
            if "|" in schema:
                items_schema = schema.split("|")
            for schema in items_schema:
                if any([v.schema_lookout(schema)
                        for v in self.validators] + [schema == "..."]):
                    return True
            return False
        else:
            return False

    def _comparar(self, item, item_schema):
        """Make the comparison recursive."""
        cls = self.__class__
        # If it's a dictionary
        if isinstance(item_schema, dict):
            if not isinstance(item, dict):
                msg = u"fail: '%s' should be a key-value structure" % item
                return cls.__red_then_gren__(msg)
            item_schema_keys_set = set(item_schema.keys())
            item_keys_set = set(item.keys())
            if item_schema_keys_set != item_keys_set:
                if item_schema_keys_set.issubset(item_keys_set):
                    msg = u"fail: This dict should not have keys %s" % (
                          str(list(item_keys_set - item_schema_keys_set)), )
                elif item_keys_set.issubset(item_schema_keys_set):
                    msg = u"fail: This dict should have keys %s" % (
                          str(list(item_schema_keys_set - item_keys_set)), )
                else:
                    msg = u"fail: This dict should have keys %s but have %s" % (
                          str(item_schema.keys()), str(item.keys()))
                return cls.__red_then_gren__(msg)
            return {chave: self._comparar(item[chave], valor_schema)
                    for chave, valor_schema in item_schema.items()}
        # If it's a list
        elif isinstance(item_schema, list):
            # If it is an empty list, any value
            if len(item_schema) == 0:
                return True
            # If it is a variable-length list
            if len(item_schema) == 2 and item_schema[1] == "...":
                item_schema_repetido = item_schema[0]
                return [self._comparar(item_lista, item_schema_repetido) for item_lista in item]
            # If it is a fixed-length list
            if not len(item_schema) == len(item):
                msg = u"fail: This list have %s items but should have %s" % (
                      len(item), len(item_schema))
                return cls.__red_then_gren__(msg)
            return [self._comparar(item_lista, item_schema_list)
                    for item_lista, item_schema_list in zip(item, item_schema)]
        # If it is a string or unicode
        elif isinstance(item_schema, str) or isinstance(item_schema, unicode):
            all_results = []
            items_schema = [item_schema]
            if "|" in item_schema:
                items_schema = item_schema.split("|")
            for item_schema in items_schema:
                for validator in self.validators:
                    if validator.schema_lookout(item_schema):
                        valid = validator.validator(item, item_schema)
                        if valid:
                            all_results.append(valid)
                            break
            all_clear = any(all_results)
            if not all_clear:
                return cls.__red_then_gren__(u"fail: '%s' should match '%s'" % (
                                             item, item_schema))
            else:
                return "pass"