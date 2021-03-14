# The new config inherits a base config to highlight the necessary modification
_base_ = '../cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_20e_coco.py'


model = dict(

backbone=dict(
		#frozen_stages=4
		),

    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=3,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
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
                num_classes=3,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
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
                num_classes=3,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.033, 0.033, 0.067, 0.067]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type='CrossEntropyLoss',
                    use_sigmoid=False,
                    loss_weight=1.0),
                loss_bbox=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1.0))
        ]
        
        
        ))


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
        
#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

evaluation = dict(classwise=True, interval=1, metric='bbox')

total_epochs = 40

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/raubtierv2a/cascade_rcnn_x101_64x4d_fpn_20e_coco_raubtierv2a_nofreeze_4gpu'

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/cascade_rcnn_x101_64x4d_fpn_20e_coco_20200509_224357-051557b1.pth'
