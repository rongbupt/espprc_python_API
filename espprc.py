# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_espprc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_espprc')
    _espprc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_espprc', [dirname(__file__)])
        except ImportError:
            import _espprc
            return _espprc
        try:
            _mod = imp.load_module('_espprc', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _espprc = swig_import_helper()
    del swig_import_helper
else:
    import _espprc
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _espprc.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _espprc.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _espprc.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _espprc.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _espprc.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _espprc.SwigPyIterator_equal(self, x)

    def copy(self):
        return _espprc.SwigPyIterator_copy(self)

    def next(self):
        return _espprc.SwigPyIterator_next(self)

    def __next__(self):
        return _espprc.SwigPyIterator___next__(self)

    def previous(self):
        return _espprc.SwigPyIterator_previous(self)

    def advance(self, n):
        return _espprc.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _espprc.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _espprc.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _espprc.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _espprc.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _espprc.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _espprc.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _espprc.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _espprc.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _espprc.IntVector___nonzero__(self)

    def __bool__(self):
        return _espprc.IntVector___bool__(self)

    def __len__(self):
        return _espprc.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _espprc.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _espprc.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _espprc.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _espprc.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _espprc.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _espprc.IntVector___setitem__(self, *args)

    def pop(self):
        return _espprc.IntVector_pop(self)

    def append(self, x):
        return _espprc.IntVector_append(self, x)

    def empty(self):
        return _espprc.IntVector_empty(self)

    def size(self):
        return _espprc.IntVector_size(self)

    def swap(self, v):
        return _espprc.IntVector_swap(self, v)

    def begin(self):
        return _espprc.IntVector_begin(self)

    def end(self):
        return _espprc.IntVector_end(self)

    def rbegin(self):
        return _espprc.IntVector_rbegin(self)

    def rend(self):
        return _espprc.IntVector_rend(self)

    def clear(self):
        return _espprc.IntVector_clear(self)

    def get_allocator(self):
        return _espprc.IntVector_get_allocator(self)

    def pop_back(self):
        return _espprc.IntVector_pop_back(self)

    def erase(self, *args):
        return _espprc.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _espprc.new_IntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _espprc.IntVector_push_back(self, x)

    def front(self):
        return _espprc.IntVector_front(self)

    def back(self):
        return _espprc.IntVector_back(self)

    def assign(self, n, x):
        return _espprc.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _espprc.IntVector_resize(self, *args)

    def insert(self, *args):
        return _espprc.IntVector_insert(self, *args)

    def reserve(self, n):
        return _espprc.IntVector_reserve(self, n)

    def capacity(self):
        return _espprc.IntVector_capacity(self)
    __swig_destroy__ = _espprc.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _espprc.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _espprc.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _espprc.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _espprc.DoubleVector___bool__(self)

    def __len__(self):
        return _espprc.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _espprc.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _espprc.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _espprc.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _espprc.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _espprc.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _espprc.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _espprc.DoubleVector_pop(self)

    def append(self, x):
        return _espprc.DoubleVector_append(self, x)

    def empty(self):
        return _espprc.DoubleVector_empty(self)

    def size(self):
        return _espprc.DoubleVector_size(self)

    def swap(self, v):
        return _espprc.DoubleVector_swap(self, v)

    def begin(self):
        return _espprc.DoubleVector_begin(self)

    def end(self):
        return _espprc.DoubleVector_end(self)

    def rbegin(self):
        return _espprc.DoubleVector_rbegin(self)

    def rend(self):
        return _espprc.DoubleVector_rend(self)

    def clear(self):
        return _espprc.DoubleVector_clear(self)

    def get_allocator(self):
        return _espprc.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _espprc.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _espprc.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _espprc.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _espprc.DoubleVector_push_back(self, x)

    def front(self):
        return _espprc.DoubleVector_front(self)

    def back(self):
        return _espprc.DoubleVector_back(self)

    def assign(self, n, x):
        return _espprc.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _espprc.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _espprc.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _espprc.DoubleVector_reserve(self, n)

    def capacity(self):
        return _espprc.DoubleVector_capacity(self)
    __swig_destroy__ = _espprc.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _espprc.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def caculate(filename, fixed_rand):
    return _espprc.caculate(filename, fixed_rand)
caculate = _espprc.caculate
# This file is compatible with both classic and new-style classes.


