# Basiskonfigurationsfile
_base_ = '../centripetalnet/centripetalnet_hourglass104_mstest_16x6_210e_coco.py'


model = dict(
    type='CornerNet',
    backbone=dict(
        type='HourglassNet',
        downsample_times=5,
        num_stacks=2,
        stage_channels=[256, 256, 384, 384, 384, 512],
        stage_blocks=[2, 2, 2, 2, 2, 4],
        norm_cfg=dict(type='BN', requires_grad=True)),
    neck=None,
    bbox_head=dict(
        type='CentripetalHead',
        num_classes=3,
        in_channels=256,
        num_feat_levels=2,
        corner_emb_channels=0,
        loss_heatmap=dict(
            type='GaussianFocalLoss', alpha=2.0, gamma=4.0, loss_weight=1),
        loss_offset=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1),
        loss_guiding_shift=dict(
            type='SmoothL1Loss', beta=1.0, loss_weight=0.05),
        loss_centripetal_shift=dict(
            type='SmoothL1Loss', beta=1.0, loss_weight=1))
            )



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

optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

evaluation = dict(classwise=True, interval=1, metric='bbox')

load_from = 'checkpoints/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth'

#http://download.openmmlab.com/mmdetection/v2.0/centripetalnet/centripetalnet_hourglass104_mstest_16x6_210e_coco/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth

