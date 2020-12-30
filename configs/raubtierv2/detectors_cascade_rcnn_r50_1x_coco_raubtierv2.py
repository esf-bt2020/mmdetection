# Basiskonfigurationsfile
_base_ = '../detectors/detectors_cascade_rcnn_r50_1x_coco.py'

#model = dict(
#    		bbox_head=dict(
#        	num_classes=3)
#       )


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

load_from = 'checkpoints/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth'

#http://download.openmmlab.com/mmdetection/v2.0/detectors/detectors_cascade_rcnn_r50_1x_coco/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth

