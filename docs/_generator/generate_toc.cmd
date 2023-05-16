cd ../tutorials

cm create-toc-from-md utils --input=sc22-scc-mlperf.md
cm create-toc-from-md utils --input=sc22-scc-mlperf-part2.md
cm create-toc-from-md utils --input=sc22-scc-mlperf-part3.md
cm create-toc-from-md utils --input=mlperf-inference-submission.md
cm create-toc-from-md utils --input=concept.md

cd ../

cm create-toc-from-md utils --input=taskforce.md
cm create-toc-from-md utils --input=installation.md
cm create-toc-from-md utils --input=README.md

cd ../
cd cm-mlops/project/mlperf-inference-v3.0-submissions/docs
cm create-toc-from-md utils --input=crowd-benchmark-mlperf-bert-inference-cuda.md
