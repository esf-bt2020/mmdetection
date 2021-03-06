# Basiskonfigurationsfile
_base_ = '../detectors/detectors_cascade_rcnn_r50_1x_coco.py'

dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')


model = dict(

		backbone=dict(
			frozen_stages=4

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
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	img_prefix='/home/azureuser/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	img_prefix='/home/azureuser/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	img_prefix='/home/azureuser/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))

optimizer = dict(type='SGD', lr=0.005, momentum=0.4, weight_decay=0.0001)

#total_epochs = 30

#work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/detectorsR50_caltech_coco'

# Pretrained model laden

load_from = 'checkpoints/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth'

#http://download.openmmlab.com/mmdetection/v2.0/detectors/detectors_cascade_rcnn_r50_1x_coco/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth

