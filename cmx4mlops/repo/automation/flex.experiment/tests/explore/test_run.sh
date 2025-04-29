echo "$VAR1 --batch_size=$VAR3 $VAR2"

echo "{\"choices\":{\"x\":${VAR1}, \"y\":\"${VAR2}\"}, \"measurements\":{\"z\":${VAR3}}}" > cmx-output.json
