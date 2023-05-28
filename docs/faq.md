[ [Back to index](README.md) ]

## CM/CK FAQ

<details>
<summary>Click here to see the table of contents.</summary>

  * [CM FAQ](#cm-faq)
    * [How to use CM scripts without affecting native Python installation?](#how-to-use-cm-scripts-without-affecting-native-python-installation?)
    * [What is the difference between Repeatability, Reproducibility and Replicability?](#what-is-the-difference-between-repeatability-reproducibility-and-replicability?)
  * [Discussions](#discussions)

</details>


### How to use CM scripts without affecting native Python installation?

We've created CM automation to help users set up multiple virtual Python environments
without altering current Python installation. Please follow [this guide](../cm-mlops/automation/script/README-extra.md#using-python-virtual-environments)
to set up Python virtual environment on your system.

### What is the difference between Repeatability, Reproducibility and Replicability?

We use the following definitions [adopted by ACM and NISO](https://www.acm.org/publications/policies/artifact-review-badging):

* *Repeatability (Same team, same experimental setup)*

  The measurement can be obtained with stated precision by the same team using the same measurement procedure, 
  the same measuring system, under the same operating conditions, in the same location on multiple trials. 
  For computational experiments, this means that a researcher can reliably repeat her own computation.

* *Reproducibility (Different team, different experimental setup)*

  The measurement can be obtained with stated precision by a different team using the same measurement procedure, 
  the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. 
  For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts.

* *Replicability (Different team, same experimental setup)*

  The measurement can be obtained with stated precision by a different team, a different measuring system, 
  in a different location on multiple trials. For computational experiments, this means that an independent group 
  can obtain the same result using artifacts which they develop completely independently.



## Discussions

Feel free to ask your questions at our [public Discord server](https://discord.gg/JjWNWXKxwT).
Join our [MLCommons taskforce on automation and reproducibility](taskforce.md) to participate
in collaborative developments and optimization challenges.
