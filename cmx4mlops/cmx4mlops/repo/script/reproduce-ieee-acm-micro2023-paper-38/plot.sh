#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to G10 repo: ${CM_GIT_REPO_G10_CHECKOUT_PATH}"
cd "${CM_GIT_REPO_G10_CHECKOUT_PATH}"

cd src/resources

# Collect all the numbers, store it in raw_output/data.json
${CM_PYTHON_BIN_WITH_PATH} gatherKernelInfo.py

# Gather data for figure 11
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepOverallPerformance.py  # The gathered data is stored in figure_drawing/overall_performance

# Gather data for figure 12
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepBreakdown.py  # The gathered data is stored in figure_drawing/overall_breakdown

# Gather data for figure 13
./figureDrawingDataPrepKernelCDF.sh  # The gathered data is stored in figure_drawing/overall_slowdown_cdf

# Gather data for figure 14
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepTraffic.py  # The gathered data is stored in figure_drawing/overall_traffic

# Gather data for figure 15
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrep.py  # The gathered data is stored in figure_drawing/overall_batchsize

# Gather data for figure 16
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepCPUsensitivity.py  # The gathered data is stored in figure_drawing/sensitivity_cpumem

# Gather data for figure 17
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepCPUSensitivityCombined.py  # The gathered data is stored in figure_drawing/sensitivity_cpumem_combined

# Gather data for figure 18
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepSSD.py  # The gathered data is stored in figure_drawing/sensitivity_ssdbw

# Gather data for figure 19
${CM_PYTHON_BIN_WITH_PATH} figureDrawingDataPrepVariation.py  # The gathered data is stored in figure_drawing/sensitivity_variation

cd figure_drawing

# Plot figures for Figure 2-4, and Figure 20-21 (Appendix)

${CM_PYTHON_BIN_WITH_PATH} plot_mem_consumption.py  # Figure 2 is output/dnn_memconsumption.pdf

${CM_PYTHON_BIN_WITH_PATH} plot_tensor_time_cdf.py  # Figure 3 is output/tensor_time_cdf.pdf

${CM_PYTHON_BIN_WITH_PATH} plot_tensor_period_distribution.py  # Figure 4 is output/tensor_periods_distribution.pdf

${CM_PYTHON_BIN_WITH_PATH} plot_detail_mem_breakdown_live.py  # Figure 20 is output/dnn_mem_consumption_breakdown_live.pdf

${CM_PYTHON_BIN_WITH_PATH} plot_detail_mem_breakdown_active.py  # Figure 21 is output/dnn_mem_consumption_breakdown_active.pdf

# Draw Figure 11
${CM_PYTHON_BIN_WITH_PATH} overallPerf.py  # Figure 11 is output/OverallPerfNew.pdf

# Draw Figure 12
${CM_PYTHON_BIN_WITH_PATH} overallBreakdown.py  # Figure 12 is output/Breakdown.pdf

# Draw Figure 13
${CM_PYTHON_BIN_WITH_PATH} overallSlowdownCDF.py  # Figure 13 is output/KernelTimeCDF.pdf

# Draw Figure 14
${CM_PYTHON_BIN_WITH_PATH} overallTraffic.py  # Figure 14 is output/OverallTraffic.pdf

# Draw Figure 15
${CM_PYTHON_BIN_WITH_PATH} overallBatchSize.py  # Figure 15 is output/OverallPerfBatchSize.pdf

# Draw Figure 16
${CM_PYTHON_BIN_WITH_PATH} sensitivityCPUMem.py  # Figure 16 is output/OverallPerfCPUMem.pdf

# Draw Figure 17
${CM_PYTHON_BIN_WITH_PATH} sensitivityCPUMemCombined.py  # Figure 17 is output/OverallPerfCPUMemCombined.pdf

# Draw Figure 18 
${CM_PYTHON_BIN_WITH_PATH} sensitivitySSDbw.py  # Figure 18 is output/OverallPerfSSDBW.pdf 

# Draw Figure 19
${CM_PYTHON_BIN_WITH_PATH} SensitivityKernelVariation.py # Figure 19 is output/SensitivityVariation.pdf
