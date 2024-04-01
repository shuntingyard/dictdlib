# dictdlib

Forked from <https://github.com/jgoerzen/dictdlib> and adapted for Python 3

## Bugs

### Python open()

Even in modern Python 3 versions default encoding when opening text files is
assumed to be `cp1252` as can be verified with

```python
import locale
locale.getpreferredencoding()
```

A quick workaround for Powershell when dictionary is in UTF-8: `$Env:PYTHONUTF8=1`
