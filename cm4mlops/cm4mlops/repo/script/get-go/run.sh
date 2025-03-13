#!/bin/bash
go version  > tmp-ver.out
test $? -eq 0 || exit 1
