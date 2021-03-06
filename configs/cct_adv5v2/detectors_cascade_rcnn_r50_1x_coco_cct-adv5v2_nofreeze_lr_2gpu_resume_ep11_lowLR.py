# Basiskonfigurationsfile
_base_ = '../detectors/detectors_cascade_rcnn_r50_1x_coco.py'

dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes


model = dict(

		backbone=dict(
			frozen_stages=1

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
    train=dict(
    	type='CocoDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
	#img_prefix='/home/azureuser/cct_images_bbox_all',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/azureuser/cct_images_bbox_all',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
	#img_prefix='/home/felice/Datasets/cct_images',
	#img_prefix='/home/azureuser/cct_images_bbox_all',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))


#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4) standard für 2 GPU
optimizer = dict(type='SGD', lr=0.0005, momentum=0.9, weight_decay=0.0001) #finetuning with 2 GPUs, 1/10 von 0.005


evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/detectorsR50_cct_adv5_coco'
work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/detectors_cascade_rcnn_r50_1x_coco_cct-adv5v2_nofreeze_lr_2gpu_resume_ep11_low10LR'

total_epochs = 21 #ep11 plus 10 mit lowLR

# Pretrained model laden
#load_from = 'checkpoints/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth'

resume_from = 'checkpoints/detectoRS_nofreeze_cct-adv5v2_ep11.pth'

#http://download.openmmlab.com/mmdetection/v2.0/detectors/detectors_cascade_rcnn_r50_1x_coco/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth

