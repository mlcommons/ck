cd ../tutorials

cm create-toc-from-md utils --input=scc23-mlperf-inference-bert.md
cm create-toc-from-md utils --input=sc22-scc-mlperf.md
cm create-toc-from-md utils --input=sc22-scc-mlperf-part2.md
cm create-toc-from-md utils --input=sc22-scc-mlperf-part3.md
cm create-toc-from-md utils --input=mlperf-inference-submission.md
cm create-toc-from-md utils --input=concept.md
cm create-toc-from-md utils --input=reproduce-mlperf-tiny.md
cm create-toc-from-md utils --input=automate-mlperf-tiny.md
cm create-toc-from-md utils --input=reproduce-mlperf-training.md
cm create-toc-from-md utils --input=common-interface-to-reproduce-research-projects.md

cd ../artifact-evaluation

cm create-toc-from-md utils --input=faq.md

cd ../

cm create-toc-from-md utils --input=taskforce.md
cm create-toc-from-md utils --input=installation.md
cm create-toc-from-md utils --input=faq.md
cm create-toc-from-md utils --input=README.md
cm create-toc-from-md utils --input=getting-started.md

cd mlperf/inference

cm create-toc-from-md utils --input=README.md

cd ../../../
cd cm-mlops/project/mlperf-inference-v3.0-submissions/docs
cm create-toc-from-md utils --input=crowd-benchmark-mlperf-bert-inference-cuda.md

cd ../../../automation/script
cm create-toc-from-md utils --input=README-extra.md

cd ../experiment
cm create-toc-from-md utils --input=README-extra.md
