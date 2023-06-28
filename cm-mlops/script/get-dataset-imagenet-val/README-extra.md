## Notes

The ImageNet 2012 validation data set is no longer publicly available [here](https://image-net.org/download.php).

However, it seems that you can still download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5).
You can then register in the MLCommons CM using this portable CM script as follows:

```bash
cm pull repo mlcommons@ck
```

```bash
cm run script "get validation dataset imagenet _2012 _full" --input={directory with ILSVRC2012_val_00000001.JPEG}
```

Alternatively, you can download the imagenet validation dataset via torrent by giving the torrent URL as follows.

```bash
cm run script "get validation dataset imagenet _2012 _full" --torrent={Torrent URL}
```

It can now be automatically plugged into other portable CM scripts for image classification including MLPerf inference vision benchmarks.

You can also find the images and use them directly as follows:

```bash
cm find cache --tags=dataset,validation,imagenet,_full
```
