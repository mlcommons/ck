#!/bin/bash
brew install rclone
test $? -eq 0 || exit 1
