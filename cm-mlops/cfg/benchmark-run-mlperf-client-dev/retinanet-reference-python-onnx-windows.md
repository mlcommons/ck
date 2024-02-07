# Under preparation

Test MLPerf inference on Windows x64 via CM:

```bash
 pip install cmind

 cm pull repo mlcommons@ck
 
 cm run script ^
	--tags=generate-run-cmds,inference,_populate-readme,_all-scenarios ^
	--model=retinanet ^
	--device=cpu ^
	--implementation=reference ^
	--backend=onnxruntime ^
	--execution-mode=valid ^
	--results_dir="d:/MlperfInference/results_dir" ^
	--category=edge ^
	--division=open ^
	--quiet
```
