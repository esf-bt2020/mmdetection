# Basiskonfigurationsfile
_base_ = '../libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco.py'

model = dict(
	
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

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('luchs', 'rotfuchs', 'wolf')
data = dict(
    train=dict(
        img_prefix='customData/train/',
        classes=classes,
        ann_file='customData/train/_annotations.coco.json'),
    val=dict(
        img_prefix='customData/valid/',
        classes=classes,
        ann_file='customData/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='customData/test/',
        classes=classes,
        ann_file='customData/test/_annotations.coco.json'))

# Pretrained model laden

load_from = 'checkpoints/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth'

#http://download.openmmlab.com/mmdetection/v2.0/libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco/libra_faster_rcnn_x101_64x4d_fpn_1x_coco_20200315-3a7d0488.pth

