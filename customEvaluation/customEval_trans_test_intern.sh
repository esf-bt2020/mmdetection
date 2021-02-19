
echo Params: 1=folderImagesPath, 2=fileTransVal, 3=fileTransTest, 4=folderModelPath, 5=epochStart, 6=epochEnd 

#folderImages="/home/felice/Datasets/cct_images"
#folderModel="/home/felice/Work/Git_Ext/esf-bt2020_mmdetection/work_dirs/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_cct-adv5_1gpu"
#fileAnnotationsTransTest='customDataCaltech/adv5/adv5_trans_test.json'
#fileAnnotationsTransVal='customDataCaltech/adv5/adv5_trans_val.json'
#epochStart=1
#epochEnd=36

folderImages=$1
fileAnnotationsTransVal=$2
fileAnnotationsTransTest=$3
folderModel=$4
epochStart=$5
epochEnd=$6

fileToTest=$fileAnnotationsTransVal

modelConfig="${folderModel}/train_config.py"

#fileEpoch="${folderModel}/epoch_${epochStart}.pth"


#Test on TransVal
for i in $(seq $epochStart $epochEnd)
do
	fileEpoch="${folderModel}/epoch_${i}.pth"
	#python tools/test.py $modelConfig $fileEpoch --cfg-options data.test.ann_file=$fileToTest --eval bbox > "${folderModel}/test_transval_ep${i}.log"
	python tools/test.py $modelConfig $fileEpoch --cfg-options data.test.ann_file=$fileToTest data.test.img_prefix=$folderImages --eval bbox > "${folderModel}/test_transval_ep${i}.log"
	#python tools/test.py $modelConfig $fileEpoch --cfg-options data.test.ann_file=$fileToTest --eval bbox
done

fileToTest=$fileAnnotationsTransTest

#Test on TransTest
for i in $(seq $epochStart $epochEnd)
do
	fileEpoch="${folderModel}/epoch_${i}.pth"
	python tools/test.py $modelConfig $fileEpoch --cfg-options data.test.ann_file=$fileToTest data.test.img_prefix=$folderImages --eval bbox > "${folderModel}/test_transtest_ep${i}.log"
done
