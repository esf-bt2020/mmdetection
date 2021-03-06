_base_ = '../gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco.py'

model = dict(

	backbone=dict(
        	frozen_stages=1
        ),

        bbox_head=dict(num_classes=10)
        

#train_cfg = dict(
#    assigner=dict(type='ATSSAssigner', topk=2),
#    allowed_border=-1,
#    pos_weight=-1,
#    debug=False)
    )

dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

data = dict(
    train=dict(
    	type='CocoDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
	#img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	#img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
	#img_prefix='/home/felice/Datasets/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))

total_epochs = 30 #default 24epochs

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #(2x2=4)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_cct-adv5v2_nofreeze_2gpu'

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth'

#http://download.openmmlab.com/mmdetection/v2.0/gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth
