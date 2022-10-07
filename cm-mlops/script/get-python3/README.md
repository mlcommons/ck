# Detect or install python

# CLI

## Default
```bash
cm run script "get python"
```
or
```bash
cm run script --tags=get,python
```

## Version

```bash
cm run script "get python" --version=3.10.6
```

## Version min
```bash
cm run script "get python" --version_min=3.9
```

## Version max
```bash
cm run script "get python" --version_max=3.9.999 --version_max_usable=3.9.12
```

## Detect python3 in non-standard path
```bash
cm run script "get python" --path={directory with python3}
```

### Detect python with non-standard name
```bash
cm run script "get python" --input={full path to python}
```

## Force new detection even if python is already found and cached
```bash
cm run script "get python" --new
```

## Test

```bash
cm run script "print python hello-world"
```
