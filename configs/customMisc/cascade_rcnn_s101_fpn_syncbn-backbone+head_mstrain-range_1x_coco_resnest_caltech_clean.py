# Basiskonfigurationsfile
_base_ = '../resnest/cascade_rcnn_s101_fpn_syncbn-backbone+head_mstrain-range_1x_coco.py'

model = dict(

	backbone=dict(
		norm_cfg=dict(type='BN', requires_grad=True),
	
	),

	roi_head=dict(
	
		bbox_head=[
            dict(
                type='Shared4Conv1FCBBoxHead',
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                norm_cfg=dict(type='BN', requires_grad=True),
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
                type='Shared4Conv1FCBBoxHead',
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                norm_cfg=dict(type='BN', requires_grad=True),
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
                type='Shared4Conv1FCBBoxHead',
                in_channels=256,
                conv_out_channels=256,
                fc_out_channels=1024,
                norm_cfg=dict(type='BN', requires_grad=True),
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

norm_cfg = dict(type='BN', requires_grad=True)


dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

data = dict(
    train=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))
    
total_epochs = 30

# Pretrained model laden

#load_from = 'checkpoints/cascade_rcnn_s101_fpn_syncbn-backbone%2Bhead_mstrain-range_1x_coco_20201005_113242-b9459f8f.pth'

#http://download.openmmlab.com/mmdetection/v2.0/resnest/cascade_rcnn_s101_fpn_syncbn-backbone%2Bhead_mstrain-range_1x_coco/cascade_rcnn_s101_fpn_syncbn-backbone%2Bhead_mstrain-range_1x_coco_20201005_113242-b9459f8f.pth

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/cascadercnn_s101_resnest_caltech_clean'
