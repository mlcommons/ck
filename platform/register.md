# Register for Collective Knowledge challenges

Since the [MLCommons CK playground](https://access.cKnowledge.org) 
is still in the heavy development stage, the registration is not yet automated via CK GUI.

You can add yourself to this [GitHub repository](https://github.com/mlcommons/ck/tree/master/cm-mlops/contributor)
using our [CM automation language](https://doi.org/10.5281/zenodo.8105339) from the command line as follows.

Install [CM](../docs/installation.md) on your system.

Fork https://github.com/mlcommons/ck .

Pull it via CM as follows:

```bash
cm pull repo --url={URL of the fork of github.com/mlcommons/ck}
```

Note that if you already have `mlcommons@ck` repository installed via CM, 
you need to delete it and then install your fork:
```bash
cm rm repo mlcommons@ck --all
cm pull repo --url={URL of the fork of github.com/mlcommons/ck}
```
Create a new contributor with your name:
```bash
cm add contributor "your name"
```

CM will ask you a few questions and will create a new CM contributor entry with your name.

You can commit this entry to your fork and create a PR to https://github.com/mlcommons/ck .

You name will be added to the [CK leaderboard](https://access.cknowledge.org/playground)
with 1 point after your PR is accepted (to support your intent to participate in our collaborative effort).

Note that you will need CM and your fork of https://github.com/mlcommons/ck to participate in challenges, 
so please keep and use it.

Finally, you can also add your name, organization and URL via [GitHub ticket](https://github.com/mlcommons/ck/issues/855).

Happy hacking!

## Discussions

You can now join the [public Discord server](https://discord.gg/JjWNWXKxwT) 
from the [MLCommons Task Force on Automation and Reproducibility](../docs/taskforce.md) 
to ask any questions, provide feedback and discuss challenges!

## Our mission

You can learn more about our mission [here](https://doi.org/10.5281/zenodo.8105339).

## Organizers

* [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
  ([MLCommons](https://mlcommons.org), [cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org))
