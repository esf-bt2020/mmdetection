# The new config inherits a base config to highlight the necessary modification
_base_ = '../gfl/gfl_x101_32x4d_fpn_dconv_c4-c5_mstrain_2x_coco.py'

model = dict(
        bbox_head=dict(num_classes=3)
        )

train_cfg = dict(
    assigner=dict(type='ATSSAssigner', topk=2),
    allowed_border=-1,
    pos_weight=-1,
    debug=False)

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


# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/gfl_x101_32x4d_fpn_dconv_c4-c5_mstrain_2x_coco_20200630_102002-14a2bf25.pth'

#http://download.openmmlab.com/mmdetection/v2.0/gfl/gfl_x101_32x4d_fpn_dconv_c4-c5_mstrain_2x_coco/gfl_x101_32x4d_fpn_dconv_c4-c5_mstrain_2x_coco_20200630_102002-14a2bf25.pth
