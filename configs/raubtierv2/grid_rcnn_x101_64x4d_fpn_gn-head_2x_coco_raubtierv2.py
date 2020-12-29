# Basiskonfigurationsfile
_base_ = '../grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco.py'



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

load_from = 'checkpoints/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth'

#http://download.openmmlab.com/mmdetection/v2.0/grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth

