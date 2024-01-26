import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("entrada,esperado", [
    ([1,1,2,2,3,3], [1,2,3]),
    ([], []),
    (["a","a","b","a"], ["a","b"]),
])
def test_dedup(entrada, esperado):
    assert mod.dedup(entrada) == esperado
