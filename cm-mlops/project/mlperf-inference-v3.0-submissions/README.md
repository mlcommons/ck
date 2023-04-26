Graphs:
 https://cknowledge.org/cm-gui-graph/?tags=mlperf-inference,all,open,edge,image-classification,singlestream
 https://cknowledge.org/cm-gui-graph/?tags=mlperf-inference,v3.0,open,edge,image-classification,singlestream&x=Result&y=Accuracy

 http://localhost:8501/?tags=mlperf-inference,v3.0,open,edge,image-classification,singlestream&x=Result&y=Accuracy
 http://localhost:8501/?tags=mlperf-inference,all,open,edge,image-classification,singlestream&x=Result&y=Accuracy

Local:
 cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.1" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.1
 cm run script "gui _graph"
