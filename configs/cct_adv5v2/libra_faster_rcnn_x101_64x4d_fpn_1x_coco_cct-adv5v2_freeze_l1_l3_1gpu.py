# Basiskonfigurationsfile
_base_ = '../libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco.py'


# Modify dataset related settings
dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

model = dict(

backbone=dict(
		frozen_stages=3
	),
	
	roi_head=dict(
	
		bbox_head=dict(
		    type='Shared2FCBBoxHead',
		    in_channels=256,
		    fc_out_channels=1024,
		    roi_feat_size=7,
		    num_classes=10,
		    bbox_coder=dict(
		        type='DeltaXYWHBBoxCoder',
		        target_means=[0.0, 0.0, 0.0, 0.0],
		        target_stds=[0.1, 0.1, 0.2, 0.2]),
		    reg_class_agnostic=False,
		    loss_cls=dict(
		        type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
		    loss_bbox=dict(
		        type='BalancedL1Loss',
		        alpha=0.5,
		        gamma=1.5,
		        beta=1.0,
		        loss_weight=1.0)
		 )
	)

)

data = dict(
    train=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))


#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) original (2x8=16)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #1gpu (1x2=2)
#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)

total_epochs=16 #default 12

evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_cct-adv5_freeze_l1_l4_LR2gpu'

load_from = 'checkpoints/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth'

#http://download.openmmlab.com/mmdetection/v2.0/libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth


