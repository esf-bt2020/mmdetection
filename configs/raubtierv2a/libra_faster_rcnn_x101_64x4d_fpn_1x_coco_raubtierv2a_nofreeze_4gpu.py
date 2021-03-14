# Basiskonfigurationsfile
_base_ = '../libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco.py'


model = dict(

backbone=dict(
		frozen_stages=4
	),
	
	roi_head=dict(
	
		bbox_head=dict(
		    type='Shared2FCBBoxHead',
		    in_channels=256,
		    fc_out_channels=1024,
		    roi_feat_size=7,
		    num_classes=3,
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

dataset_type = 'COCODataset'
classes = ('luchs', 'rotfuchs', 'wolf')
data = dict(
    train=dict(
        img_prefix='raubtierv2a/train/',
        classes=classes,
        ann_file='raubtierv2a/train/_annotations.coco.json'),
    val=dict(
        img_prefix='raubtierv2a/valid/',
        classes=classes,
        ann_file='raubtierv2a/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='raubtierv2a/test/',
        classes=classes,
        ann_file='raubtierv2a/test/_annotations.coco.json'))


#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) original (2x8=16)
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #1gpu (1x2=2)
#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)

total_epochs=24 #default 12

evaluation = dict(classwise=True, interval=1, metric='bbox')

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/raubtierv2a/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_raubtierv2a_nofreeze_4gpu'

load_from = 'checkpoints/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth'

#http://download.openmmlab.com/mmdetection/v2.0/libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth


