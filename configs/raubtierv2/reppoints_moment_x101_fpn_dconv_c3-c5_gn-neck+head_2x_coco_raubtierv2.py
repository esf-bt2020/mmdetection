# Basiskonfigurationsfile
_base_ = '../reppoints/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck+head_2x_coco.py'

model = dict(
    		bbox_head=dict(
        	num_classes=3)
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
        ann_file='customData/test/_annotation.coco.json'))

# Pretrained model laden

total_epochs = 48

load_from = 'checkpoints/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck%2Bhead_2x_coco_20200329-f87da1ea.pth'

#http://download.openmmlab.com/mmdetection/v2.0/reppoints/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck%2Bhead_2x_coco/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck%2Bhead_2x_coco_20200329-f87da1ea.pth

