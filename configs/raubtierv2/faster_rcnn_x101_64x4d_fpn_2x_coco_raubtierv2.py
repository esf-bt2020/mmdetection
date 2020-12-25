_base_ = '../faster_rcnn/faster_rcnn_x101_64x4d_fpn_2x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=[

        ]
        
        
        ))

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

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth'
