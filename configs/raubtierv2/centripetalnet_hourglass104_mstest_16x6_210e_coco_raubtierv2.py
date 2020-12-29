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
            type='SmoothL1Loss', beta=1.0, loss_weight=1)))



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
        ann_file='customData/test/_annotation.coco.json'))

# Pretrained model laden

load_from = 'checkpoints/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth'

#http://download.openmmlab.com/mmdetection/v2.0/centripetalnet/centripetalnet_hourglass104_mstest_16x6_210e_coco/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth

