#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsEvaluation/

cd evaluation/

grep ExecutedCycles way*/*.xml | grep -v way[^v]*chbin | sort -V | sed -e 's/\(way[0-9]*\)-.*coremark./\1 /g' -e 's/bin.xml.*"\(.*\)"/ \1/' | awk 'NR==1{a=$3}NR%3==1{printf($1)}{printf(" "a/$3)}NR%3==0{print""}' > PerformanceImprovement.dat
echo 'set terminal png; set out "PerformanceImprovement.png"; set style histogram clustered; plot [] [0:2] "PerformanceImprovement.dat" using 2:xtic(1) with histogram title "R", "PerformanceImprovement.dat" using 3 with histogram title "S", "PerformanceImprovement.dat" using 4 with histogram title "C";' | gnuplot

grep Retirer -B3 way8-*/*.xml | grep NumOpCode | grep -v way[^v]*chbin | sed 'y/",/  /' | awk 'NR==1{for(i=3;i<37;++i){a+=$(i)}}{for(i=3;i<37;++i){$(i)/=a}}{print (NR==1?"R":NR==2?"S":"C"),$4+$5,$9,$7,$10+$20,$11+$21,$14+$15,$16+$17,$22+$23+$24+$25+$26+$27+$28+$29,$13,$33,$30+$31}' > InstructionBreakdown.dat
echo 'set terminal png; set out "InstructionBreakdown.png"; set style histogram rowstacked; set key invert; plot "InstructionBreakdown.dat" using 2:xtic(1) with histogram title "Call+Ret", "InstructionBreakdown.dat" using 3 with histogram title "Jump", "InstructionBreakdown.dat" using 4 with histogram title "CondBr", "InstructionBreakdown.dat" using 5 with histogram title "Load", "InstructionBreakdown.dat" using 6 with  histogram title "Store", "InstructionBreakdown.dat" using 7 with histogram title "ALU", "InstructionBreakdown.dat" using 8 with histogram title "Mul+Div", "InstructionBreakdown.dat" using 9 with histogram title "FLOPs", "InstructionBreakdown.dat" using 10 with histogram title "Move", "InstructionBreakdown.dat" using 11 with histogram title "NOP", "InstructionBreakdown.dat" using 12 with histogram title "Others";' | gnuplot

cat <(grep SkippedInsns skip-result/*.chbin.xml) <(grep 'Register.*Frequency' skip-result/*.chbin.xml) | sed 'y/",/  /' | awk 'NR==1{insns=$2}NR!=1{for(s=t=u=v=i=0;i<16;++i){s+=$(2+i);t+=$(18+i);u+=$(34+i);v+=$(50+i)}print (NR==2?"Write":"Read"),s/insns,t/insns,u/insns,v/insns,(NR==2?(insns-s-t-u-v)/insns:0)}' > HandBreakdown.dat
echo 'set terminal png; set out "HandBreakdown.png"; set style histogram rowstacked; set key invert; plot "HandBreakdown.dat" using 2:xtic(1) with histogram title "s hand", "HandBreakdown.dat" using 3 with histogram title "t hand", "HandBreakdown.dat" using 4 with histogram title "u hand", "HandBreakdown.dat" using 5 with histogram title "v hand", "HandBreakdown.dat" using 6 with histogram title "no dst hand";' | gnuplot

cat <(grep SkippedInsns skip-result/*.chbin.xml) <(grep LifetimeDistributionKey skip-result/*.chbin.xml) <(grep LifetimeDistributionCount skip-result/*.chbin.xml) | sed 'y/",/  /' | awk 'NR==1{insns=$2}NR==2{for(i=2;i<700;++i){a[i]=$(i)}}NR>2{sum=1e-300;for(i=699;i>1;--i){sum+=$(i);b[NR][i]=sum/insns}}END{for(i=2;i<700;++i){print a[i],b[3][i],b[4][i],b[5][i],b[6][i]}}' > LifetimeByHand.dat
echo 'set terminal png; set out "LifetimeByHand.png"; set logscale x; set logscale y; plot [1:1e6] [1e-6:1] "LifetimeByHand.dat" using 1:2 with line title "v", "LifetimeByHand.dat" using 1:3 with line title "u", "LifetimeByHand.dat" using 1:4 with line title "t", "LifetimeByHand.dat" using 1:5 with line title "s";' | gnuplot

cat <(grep SkippedInsns skip-result/*.rvbin.xml) <(grep LifetimeDistributionKey skip-result/*.rvbin.xml) <(grep LifetimeDistributionCountAll skip-result/*.rvbin.xml) | sed 'y/",/  /' | awk 'NR==1{insns=$2}NR==2{for(i=2;i<700;++i){a[i]=$(i)}}NR==3{for(i=699;i>1;--i){sum+=$(i);print a[i],sum/insns}}' > Lifetime-RV.dat
echo 'set terminal png; set out "Lifetime-RV.png"; set logscale x; set logscale y; plot [1:1e6] [1e-6:1] "Lifetime-RV.dat" using 1:2 with line title "RV";' | gnuplot
cat <(grep SkippedInsns skip-result/*.stbin.xml) <(grep LifetimeDistributionKey skip-result/*.stbin.xml) <(grep LifetimeDistributionCountAll skip-result/*.stbin.xml) | sed 'y/",/  /' | awk 'NR==1{insns=$2}NR==2{for(i=2;i<700;++i){a[i]=$(i)}}NR==3{for(i=699;i>1;--i){sum+=$(i);print a[i],sum/insns}}' > Lifetime-ST.dat
echo 'set terminal png; set out "Lifetime-ST.png"; set logscale x; set logscale y; plot [1:1e6] [1e-6:1] "Lifetime-ST.dat" using 1:2 with line title "ST";' | gnuplot
cat <(grep SkippedInsns skip-result/*.chbin.xml) <(grep LifetimeDistributionKey skip-result/*.chbin.xml) <(grep LifetimeDistributionCountAll skip-result/*.chbin.xml) | sed 'y/",/  /' | awk 'NR==1{insns=$2}NR==2{for(i=2;i<700;++i){a[i]=$(i)}}NR==3{for(i=699;i>1;--i){sum+=$(i);print a[i],sum/insns}}' > Lifetime-CH.dat
echo 'set terminal png; set out "Lifetime-CH.png"; set logscale x; set logscale y; plot [1:1e6] [1e-6:1] "Lifetime-CH.dat" using 1:2 with line title "CH";' | gnuplot

echo "see $(pwd)/*.png!"
