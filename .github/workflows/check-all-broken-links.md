name: Check .md README files for broken links

on:
  push: [master]

jobs:
  markdown-link-check:
    runs-on: ubuntu-latest
    # check out the latest version of the code
    steps:
    - uses: actions/checkout@v3

    # Checks the status of hyperlinks in .md files in verbose mode
    - name: Check links
      uses: gaurav-nelson/github-action-markdown-link-check@v1
      with:
        use-quiet-mode: 'yes'
