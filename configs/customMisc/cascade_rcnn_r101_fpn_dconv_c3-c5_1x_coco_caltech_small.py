# The new config inherits a base config to highlight the necessary modification
_base_ = '../dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py'

# Modify dataset related settings
dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

data = dict(
    train=dict(
    	type='CaltechDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_halfsize_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_halfsize_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
         img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_halfsize_adv/eccv_val_TEST_adv.json'))

total_epochs = 50

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth'

#http://download.openmmlab.com/mmdetection/v2.0/dcn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco_20200203-3b2f0594.pth
