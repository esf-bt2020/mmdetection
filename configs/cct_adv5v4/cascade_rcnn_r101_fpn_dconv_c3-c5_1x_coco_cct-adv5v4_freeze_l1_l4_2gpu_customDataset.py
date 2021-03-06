# The new config inherits a base config to highlight the necessary modification
_base_ = '../dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py'

dataset_type = 'CustomDataset'
#classes = ( 'customEmpty', 'bobcat','coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #11 classes
classes = ( 'bobcat','coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

model = dict(

backbone=dict(
       
        	num_stages=4,
        	frozen_stages=4
        	),

	roi_head=dict(

		bbox_head=[
			    dict(
				type='Shared2FCBBoxHead',
				in_channels=256,
				fc_out_channels=1024,
				roi_feat_size=7,
				num_classes=10,
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
				num_classes=10,
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
				num_classes=10,
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
	filter_empty_gt=False,
    train=dict(
    	type='CustomDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5v4/adv5v4_train.json'),
	filter_empty_gt=False,
    val=dict(
    	type='CustomDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5v4/adv5v4_known_val.json'),
	filter_empty_gt=False,
    test=dict(
    	type='CustomDataset',
	#img_prefix='/home/felice/Datasets/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5v4/adv5v4_known_test.json'))

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)

total_epochs = 16 #default=12

evaluation = dict(classwise=True, interval=1, metric='bbox')

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth'

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_cct-adv5v4_freeze_l1_l4_2gpu_customDataset'

#http://download.openmmlab.com/mmdetection/v2.0/dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth
