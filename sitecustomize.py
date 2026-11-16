"""Compatibility shim for the legacy nose runner on modern Python.

nose 1.3.7 still references collections.Callable, removed in Python 3.10.
This restores the alias without changing application behavior.
"""
import collections
import collections.abc

if not hasattr(collections, "Callable"):
    collections.Callable = collections.abc.Callable
