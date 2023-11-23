name: Check .md README files for broken links

on: [pull_request]

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
        check-modified-files-only: 'yes'
