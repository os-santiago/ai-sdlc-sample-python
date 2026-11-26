# ai-sdlc-sample-python

A small Python package set used as an external sample repository for
[ai-sdlc](https://github.com/os-santiago/ai-sdlc): issues on this repository
are delivered end to end by the runtime (verification with the repository's
own tests, independent review, pull request and merge). It is the Python
counterpart of [ai-sdlc-sample](https://github.com/os-santiago/ai-sdlc-sample).

```bash
python3 -I -m unittest discover -s . -t . -p 'test_*.py'
```

It needs Python 3.12 or later and uses only the standard library, so its
tests run offline.

## Layout

Each package (`mathutil`, `textutil`, `kv`) keeps one function per module,
re-exported from the package's `__init__.py`, with its tests beside it in
`test_<module>.py`.
