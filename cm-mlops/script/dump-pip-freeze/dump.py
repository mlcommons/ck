from pip._internal.operations import freeze

pkgs = freeze.freeze()
with open('tmp-pip-freeze', "w") as f:
    for pkg in pkgs:
        f.write(pkg+"\n")
