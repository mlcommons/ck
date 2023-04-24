# Notes

Users extend the CK functionality via external [GitHub reposities](https://cknow.io/repos) in the CK format. 
See [docs](https://ck.readthedocs.io/en/latest/src/typical-usage.html) for more details.

If you want to extend the CK core, please note that we plan to completely rewrite it based on the OO principles
(we wrote the first prototype without OO to be able to port to bare-metal devices in C but we decided not to do it at the end).
We also plan to relicense the framework to Apache 2.0.
In the meantime, please check [this documentation](https://ck.readthedocs.io/en/latest/src/how-to-contribute.html).

# How to contribute

Current Collective Knowledge framework (CK) uses standard Apache 2.0 license. 
Contributions are very welcome to improve the existing functionality 
of the CK framework, CK modules, and CK components.

You can easily contribute to CK and all related repositories by forking them 
on GitHub and then submitting a pull request. We strongly suggest you 
to discuss your PR with the community using the [public CK google group](https://groups.google.com/forum/#!forum/collective-knowledge).

Since most CK modules and components are reused in different projects, 
please make sure that you thoroughly tested your contributions 
and they are backward compatible!

When sending PRs, please briefly explain why they are needed,
how their work, and how you tested backward compatibility
to make sure that dependent projects continue working correctly.

Please submit bug reports, feedback, and ideas as [GitHub issues](https://github.com/mlcommons/ck/issues).

*Note that we plan to rewrite the CK kernel and make it more pythonic
when we have more resources! Feel free to [get in touch](https://cKnowledge.org/contacts.html)
if you would like to know more about our future R&D plans.*

**Thank you very much for supporting this community project!**

