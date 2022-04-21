# Enhancements

## Planned enhancements

* [Timeline for Q2 and Q3 2022](https://github.com/mlcommons/ck/issues/189)

## Ideas

### Speeding up search action

In the CK1, we used explicit indexing of all entries using .cm directories. 
Such mechanism provided a very fast search but it was not very user friendly:
if a user forgot to add .cm to Git or Zip, the search function was broken.

In the CK2 (CM), we decided to simplify the overall architecture and removed
explicit indexing by default. Now, CM will be searching recursively for entries
based on UID and alias in their meta description (_cm.yaml | _cm.json).

We want to add implicit indexing later similar to Git to let CM auto-index repositories.
