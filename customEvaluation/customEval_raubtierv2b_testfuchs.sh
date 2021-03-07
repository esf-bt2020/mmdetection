

echo Params: 1=folderModelPath, 2=bestEpoch



#folderImages=$1
#fileAnnotationsTransTest=$2
folderModel=$1

bestEpoch=$2

modelConfig="${folderModel}/train_config.py"



outputfolderknown="${folderModel}/test_raubtierv2b_fuchsdataset"
echo Creating Folder: $outputfolderknown
mkdir $outputfolderknown
fileEpoch="${folderModel}/epoch_${bestEpoch}.pth"
#python tools/test.py $modelConfig $fileEpoch --show-dir $outputfolderknown --eval bbox > "${folderModel}/test_known_best_ep${bestEpoch}.log"
python tools/test.py $modelConfig $fileEpoch --show-dir $outputfolderknown --cfg-options data.test.img_prefix="customDataTestFuchsEmpty/images_fuchs" data.test.ann_file="customDataTestFuchsEmpty/FVA_210304_v2_COCO_Fuchs_200.zip.json" --eval bbox > "${folderModel}/test_raubtierv2b_testfuchs_best_ep${bestEpoch}.log"

