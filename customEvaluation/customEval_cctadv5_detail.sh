
folderModel="/home/felice/Work/Git_Ext/esf-bt2020_mmdetection/work_dirs/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_cct-adv5_1gpu"

folderImages="/home/felice/Datasets/cct_images"

fileAnnotationsTransTest='customDataCaltech/adv5/adv5_trans_test.json'

fileToTest=$fileAnnotationsTransVal

bestEpochKnown=27
bestEpochTrans=26

modelConfig="${folderModel}/train_config.py"



outputfolderknown = "${folderModel}/test_known"
mkdir outputfolderknown
fileEpoch="${folderModel}/epoch_${bestEpochKnown}.pth"
python tools/test.py $modelConfig $fileEpoch --show-dir outputfolderknown --eval bbox > "${folderModel}/test_known_best_ep${i}.log"



outputfoldertrans = "${folderModel}/test_trans"
mkdir outputfoldertrans
fileEpoch="${folderModel}/epoch_${bestEpochTrans}.pth"
python tools/test.py $modelConfig $fileEpoch --show-dir outputfoldertrans --eval bbox > "${folderModel}/test_trans_best_ep${i}.log"


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

