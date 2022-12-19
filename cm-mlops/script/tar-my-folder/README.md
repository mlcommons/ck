# Compress using tar
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) compresses a given folder and generates a tar.gz file

## How To
```bash
cm run script --tags=run,tar --input_dir=[DIR_PATH]
```


### Additional Options
* `--output_dir:` Directory in which to generate the output file. Default is current working directory
* `--outfile:`: Output filename. Default is inputfoldername".gz"
