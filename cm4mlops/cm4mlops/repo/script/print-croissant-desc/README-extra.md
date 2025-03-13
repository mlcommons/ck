# MLCommons CM automation recipe

## Print [Croissant](https://github.com/mlcommons/croissant) description from metadata URL

```bash
pip intstall cmind

cm pull repo ctuning@mlcommons-ck

cmr "print croissant desc" --url="https://raw.githubusercontent.com/mlcommons/croissant/main/datasets/1.0/gpt-3/metadata.json"
```

## About

* Code snippet taken from https://github.com/mlcommons/croissant/pull/564/files ([@mkuchnik](https://github.com/mkuchnik))
* CM automation recipe added by [@gfursin](https://github.com/gfursin).