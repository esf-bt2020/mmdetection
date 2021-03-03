

echo Params: 1=folderImagesPath, 2=fileTransTest, 3=folderModelPath, 4=bestEpochKnown, 5=bestEpochTrans 



folderImages=$1
fileAnnotationsTransTest=$2
folderModel=$3

bestEpochKnown=$4
bestEpochTrans=$5

modelConfig="${folderModel}/train_config.py"



outputfolderknown="${folderModel}/test_known"
echo Creating Folder: $outputfolderknown
mkdir $outputfolderknown
fileEpoch="${folderModel}/epoch_${bestEpochKnown}.pth"
#python tools/test.py $modelConfig $fileEpoch --show-dir $outputfolderknown --eval bbox > "${folderModel}/test_known_best_ep${bestEpochKnown}.log"
python tools/test.py $modelConfig $fileEpoch --show-dir $outputfolderknown --cfg-options data.test.img_prefix=$folderImages --eval bbox > "${folderModel}/test_known_best_ep${bestEpochKnown}.log"


outputfoldertrans="${folderModel}/test_trans"
echo Creating Folder: $outputfoldertrans
mkdir $outputfoldertrans
fileEpoch="${folderModel}/epoch_${bestEpochTrans}.pth"
python tools/test.py $modelConfig $fileEpoch --show-dir $outputfoldertrans --cfg-options data.test.ann_file=$fileAnnotationsTransTest data.test.img_prefix=$folderImages --eval bbox > "${folderModel}/test_trans_best_ep${bestEpochTrans}.log"


#Save Test
#python tools/test.py $configfile $checkpointfile --out resultfile.pkl


#Evaluierung auf Testdatenset
#python ./tools/test.py $configfile $checkpointfile --eval bbox
 
#Training => bbox_mAP plotten
#echo python tools/analyze_logs.py plot_curve $logfile --keys bbox_mAP #–-legend bbox_mAP
#python tools/analyze_logs.py plot_curve $logfile --keys bbox_mAP #–-legend bbox_mAP
 

#Training => loss_cls und loss_bbox plotten
#python tools/analyze_logs.py plot_curve $logfile --keys loss_cls loss_bbox --legend loss_cls loss_bbox
 

#Testdaten anzeigen

# python ./tools/test.py \
# $configfile \
# $checkpointfile \
# --out resultfile.pkl \
# --show

