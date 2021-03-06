# The new config inherits a base config to highlight the necessary modification
_base_ = '../dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py'

# Modify dataset related settings
dataset_type = 'CaltechDataset'

classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

model = dict(

backbone=dict(
       
        	num_stages=4,
        	frozen_stages=2
        	),

	roi_head=dict(

		bbox_head=[
			    dict(
				type='Shared2FCBBoxHead',
				in_channels=256,
				fc_out_channels=1024,
				roi_feat_size=7,
				num_classes=22,
				bbox_coder=dict(
				    type='DeltaXYWHBBoxCoder',
				    target_means=[0.0, 0.0, 0.0, 0.0],
				    target_stds=[0.1, 0.1, 0.2, 0.2]),
				reg_class_agnostic=True,
				loss_cls=dict(
				    type='CrossEntropyLoss',
				    use_sigmoid=False,
				    loss_weight=1.0),
				loss_bbox=dict(type='SmoothL1Loss', beta=1.0,
				               loss_weight=1.0)),
			    dict(
				type='Shared2FCBBoxHead',
				in_channels=256,
				fc_out_channels=1024,
				roi_feat_size=7,
				num_classes=22,
				bbox_coder=dict(
				    type='DeltaXYWHBBoxCoder',
				    target_means=[0.0, 0.0, 0.0, 0.0],
				    target_stds=[0.05, 0.05, 0.1, 0.1]),
				reg_class_agnostic=True,
				loss_cls=dict(
				    type='CrossEntropyLoss',
				    use_sigmoid=False,
				    loss_weight=1.0),
				loss_bbox=dict(type='SmoothL1Loss', beta=1.0,
				               loss_weight=1.0)),
			    dict(
				type='Shared2FCBBoxHead',
				in_channels=256,
				fc_out_channels=1024,
				roi_feat_size=7,
				num_classes=22,
				bbox_coder=dict(
				    type='DeltaXYWHBBoxCoder',
				    target_means=[0.0, 0.0, 0.0, 0.0],
				    target_stds=[0.033, 0.033, 0.067, 0.067]),
				reg_class_agnostic=True,
				loss_cls=dict(
				    type='CrossEntropyLoss',
				    use_sigmoid=False,
				    loss_weight=1.0),
				loss_bbox=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1.0))
		]

	)
)


data = dict(
    train=dict(
    	type='CaltechDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        #img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))

total_epochs = 30

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth'

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/cascadercnn_r101_dconvc3c5_caltech_from_coco_freeze_l1_l2'

#http://download.openmmlab.com/mmdetection/v2.0/dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth
