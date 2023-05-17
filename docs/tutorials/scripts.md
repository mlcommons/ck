[ [Back to index](../README.md) ]

# Tutorial: adding new CM scripts and workflows




One of the main goals of the CM meta-framework is to make it easier for the new users 
to add their own artifacts, scripts and workflows in the CM format:

For example, you can now add your own native script with some tags to CM 
and run it with a minimal effort as follows:

```bash
cm add script my-cool-component --tags=my,cool-component,prototype
cm run script my-cool-component
cm run script --tags=my,cool-component
```

You can then find this component and just add there your own script with the name *run.sh* 
on Linux/MacOS or *run.bat* on Windows:
```bash
cd `cm find script my-cool-component`

cat > run.sh
echo "My cool component"

cm run script my-cool-component

...
My cool component
```

You can then extend *_cm.json* and add more tags or dependencies to reuse environment variables and files
in your script prepared by other CM scripts from public or private projects.

Finally, you can add the *customize.py* script with *preprocess* and *postprocess* functions to implement more
complex logic to customize the execution of a given CM script based on previous dependencies, flags, platform and CPU info, etc.


## Extending CM scripts as a collaborative playground

We have developed CM as a collaborative playground to work with the community and gradually unify the APIs of diverse DevOps and MLOps scripts and tools,
and interconnect them to simplify the development, optimization, deployment and usage of complex applications into intelligent "CM" components.

Our next steps:
* agreeing on and unifying tags that describe different CM scripts in a unique way
* agreeing on and unifying scripts, env variables and state of different CM scripts
* adding support for different CM scripts versions and ranges similar to Pypi
* adding support to run CM script scripts for a specific host OS version and CPU
* implementing MLPerf benchmark as a pipeline of CM scripts

Please follow our [GitHub tickets]( https://github.com/mlcommons/ck/issues ) 
and [public meetings](https://github.com/mlcommons/ck/tree/master/cm/meetings) 
or get in touch if you want 
to join this collaborative effort to unify DevOps and MLOps 
and make them more portable, interoperable and deterministic.

Also feel free to check the article with the [original CK concept](https://arxiv.org/abs/2011.01149)
and another [CM tutorial about sharing and reusing any artifacts in a unified format](tutorial-concept.md).
