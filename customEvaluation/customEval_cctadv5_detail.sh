
folderModel="/media/RED/FFHS_BT/_TrainedModels/cct_adv5v2/12_LibraFasterRCNN_X101/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_cct-adv5v2_freeze_l1_l4_1gpu"

#folderImages="/home/felice/Datasets/cct_images"
folderImages="media/Pool/Thesis/Datensets/cct_images"

fileAnnotationsTransTest='customDataCaltech/adv5/adv5_trans_test.json'

bestEpochKnown=12
bestEpochTrans=12

modelConfig="${folderModel}/train_config.py"



outputfolderknown="${folderModel}/test_known"
echo Creating Folder: $outputfolderknown
mkdir $outputfolderknown
fileEpoch="${folderModel}/epoch_${bestEpochKnown}.pth"
python tools/test.py $modelConfig $fileEpoch --show-dir $outputfolderknown --eval bbox > "${folderModel}/test_known_best_ep${i}.log"



outputfoldertrans="${folderModel}/test_trans"
echo Creating Folder: $outputfoldertrans
mkdir $outputfoldertrans
fileEpoch="${folderModel}/epoch_${bestEpochTrans}.pth"
python tools/test.py $modelConfig $fileEpoch --show-dir $outputfoldertrans --cfg-options data.test.ann_file=$fileAnnotationsTransTest --eval bbox > "${folderModel}/test_trans_best_ep${i}.log"


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

