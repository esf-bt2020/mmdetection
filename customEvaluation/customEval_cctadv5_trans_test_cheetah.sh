
echo Params: 1=folderModelPath, 2=epochStart, 3=epochEnd 

folderImages="/media/SSD2project/WilLiCam/datasets/caltech/cct_images"
folderModel=$1
fileAnnotationsTransTest='customDataCaltech/adv5/adv5_trans_test.json'
fileAnnotationsTransVal='customDataCaltech/adv5/adv5_trans_val.json'
epochStart=$2
epochEnd=$3

customEvaluation/customEval_trans_test_intern.sh $folderImages $fileAnnotationsTransVal $fileAnnotationsTransTest $folderModel $epochStart $epochEnd

