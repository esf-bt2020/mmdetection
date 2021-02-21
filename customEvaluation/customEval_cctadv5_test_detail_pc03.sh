
echo Params: 1=folderModelPath, 2=bestEpochKnown, 3=bestEpochTrans 


folderImages="/media/Pool/Thesis/Datensets/cct_images"
fileAnnotationsTransTest='customDataCaltech/adv5/adv5_trans_test.json'
folderModel=$1

bestEpochKnown=$2
bestEpochTrans=$3

#echo customEval_cctadv5_test_detail_intern.sh Params: 1=folderImagesPath, 2=fileTransTest, 3=folderModelPath, 4=bestEpochKnown, 5=bestEpochTrans 
customEvaluation/customEval_cctadv5_detail_intern.sh $folderImages $fileAnnotationsTransTest $folderModel $bestEpochKnown $bestEpochTrans

