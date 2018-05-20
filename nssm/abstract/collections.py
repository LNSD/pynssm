from enum import Enum


class AbstractDict(object):
    """
    This is an abstract class which implements an dictionary like object with
    some additional features.
    """
    __marker = object()

    def __init__(self):
        self.dictionary = {}

    def __getitem__(self, key):
        return self.dictionary[self._keytransformer(key)]

    def __setitem__(self, key, value):
        self.dictionary[self._keytransformer(key)] = value

    def __delitem__(self, key):
        del self.dictionary[self._keytransformer(key)]

    def __iter__(self):
        return iter(self.dictionary)

    def __len__(self):
        return len(self.dictionary)

    def __str__(self):
        return str(self.dictionary)

    def __repr__(self):
        return str(self.dictionary)

    def update(self, d):
        self._recursive_update(self.dictionary, d)

    def iterkeys(self):
        return iter(self)

    def iteritems(self):
        for key in self:
            yield (key, self[key])

    def itervalues(self):
        for key in self:
            yield self[key]

    def keys(self):
        return self.dictionary.keys()

    def items(self):
        return [(key, self[key]) for key in self]

    def values(self):
        return [self[key] for key in self]

    def pop(self, key, default=__marker):
        try:
            value = self[key]
        except KeyError:
            if default is self.__marker:
                raise
            return default
        else:
            del self[key]
            return value

    def popitem(self):
        try:
            key = next(iter(self))
        except StopIteration:
            raise KeyError
        value = self[key]
        del self[key]
        return key, value

    def clear(self):
        try:
            while True:
                self.popitem()
        except KeyError:
            pass

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
        return default

    def pretty_print(self):
        return self._recursive_print(self.dictionary, 0)

    def _recursive_update(self, d1, d2):
        for k, v in sorted(d2.items()):
            if k in d1.keys() and type(v) == dict:
                self._recursive_update(d1[k], v)
            else:
                d1[k] = v

    def _recursive_print(self, d, nesting):
        result = ""

        for k, v in sorted(d.items()):
            if type(v) == dict:
                continue

            result += " "*nesting + "%-30s" % (str(k),) + ": " + str(v) + "\n"

        for k, v in sorted(d.items()):
            if type(v) != dict:
                continue

            result += " "*nesting + "%s" % (str(k),) + "...\n"
            result += self._recursive_print(d[k], nesting+4)

        return result

    def _keytransformer(self, key):
        """When overridden permits manipulation of the key before accessing
        the dictionary"""
        return key


class AbstractEnum(Enum):
    """
    Python has built-in support for Enum class types from 3.4 on, backport
    is provided in enum34 package. This class further extends this Enum class
    with an easy method to get the defined symbolic enumerations.
    """

    @classmethod
    def coerce(cls, val):
        """
        Return the desired enum object or throw an error, the enum object will
        be searched based on its name or value.

        :param val: the value or name of the desired enum
        :return: the enum object
        """
        try:
            return cls[val]
        except KeyError:
            try:
                return cls(val)
            except ValueError:
                msg = '"{0}" not a valid enum value or name of {1}, possible' \
                      ' names are {2} and possible values are {3}.'
                raise ValueError(msg.format(val, cls.__name__,
                                            ','.join(cls.get_names()),
                                            str(cls.get_values())))

    @classmethod
    def get_names(cls):
        """
        Returns all the names of the symbolic enumerations defined. Including
        the aliases.

        :return: list of all enum names
        """
        names = []
        for name, member in cls.__members__.items():
            names.append(name)
        return names

    @classmethod
    def get_values(cls):
        """
        Returns all the values of the defined symbolic enumerations.

        :return: list of values
        """
        values = []
        for member in list(cls):
            values.append(member.value)
        return values
