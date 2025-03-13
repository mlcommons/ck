echo "====================== Atifacts Evaluation for MICRO23 paper=========================="
echo "Sparse-DySta: Sparsity-Aware Dynamic and Static Scheduling for Sparse Multi-DNN Workloads"
container="docker"

echo "==================  Run a container test to make sure container works =================="
${container} run docker.io/hello-world

echo "====================================================================================="

echo "==================  Pulling the Docker image to run the experiments =================="
${container} pull hxfan/spar-dysta-micro23:ae

echo "==================  Creating Container to run the experiments =================="
sudo ${container} run -it -d --name spar-dysta --gpus all  hxfan/spar-dysta-micro23:ae /bin/bash # Create container


echo "================== Generate Figure-12, Attention  =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/attnn/dysta_comparison_sanger_tradeoff_analysis.sh
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/Sanger_Tradeoff_slo10.0.pdf .
echo "================== Generate Figure-12, CNN  =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/cnn/dysta_comparison_eyerissv2_tradeoff_analysis.sh
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/EyerissV2_Tradeoff_slo10.0.pdf .

echo "================== Generate Figure-13, Attention  =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/attnn/effect_sparsity_sanger.sh
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/Sanger_Sparsity_Effect30_sample1000_across_slo10.0_prema.pdf .
echo "================== Generate Figure-13  CNN =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/cnn/effect_sparsity_eyerissv2.sh 
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/EyerissV2_Sparsity_Effect3_sample1000_across_slo10.0_prema.pdf .


echo "================== Generate Table5 & Figure-14, Attention  =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/attnn/dysta_comparison_sanger_across_slo.sh
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/Sanger_Metrics_rate30_sample1000_across_slo.pdf .
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/Sanger_Metrics_rate40_sample1000_across_slo.pdf .
echo "================== Generate Table5 & Figure-14  CNN =================="
sudo ${container} exec --workdir /workspace/dysta-sparse/dysta_scheduler spar-dysta script/cnn/dysta_comparison_eyerissv2_across_slo.sh
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/EyerissV2_Metrics_rate3_sample1000_across_slo.pdf .
${container} cp -r spar-dysta:/workspace/dysta-sparse/dysta_scheduler/EyerissV2_Metrics_rate4_sample1000_across_slo.pdf .

test $? -eq 0 || exit 1
