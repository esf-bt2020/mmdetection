# Basiskonfigurationsfile
_base_ = '../hrnet/cascade_rcnn_hrnetv2p_w40_20e_coco.py'


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

load_from = 'checkpoints/cascade_rcnn_hrnetv2p_w40_20e_coco_20200512_161112-75e47b04.pth'

