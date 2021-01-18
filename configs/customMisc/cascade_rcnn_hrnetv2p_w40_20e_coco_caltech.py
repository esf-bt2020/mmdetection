# Basiskonfigurationsfile
_base_ = '../hrnet/cascade_rcnn_hrnetv2p_w40_20e_coco.py'


# Modify dataset related settings
dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

data = dict(
    train=dict(
    	type='CaltechDataset',
        img_prefix='customDataCaltech/eccv_18_all_images_sm/',
        classes=classes,
        #ann_file='customDataCaltech/eccv_18_annotations/train_annotations.json'),
        ann_file='customDataCaltech/caltech_bboxes_20200316.json'),
    val=dict(
    	type='CaltechDataset',
        img_prefix='customDataCaltech/eccv_18_all_images_sm/',
        classes=classes,
        ann_file='customDataCaltech/caltech_bboxes_20200316.json'),
    test=dict(
    	type='CaltechDataset',
        img_prefix='customDataCaltech/eccv_18_all_images_sm/',
        classes=classes,
        ann_file='customDataCaltech/eccv_18_annotations/cis_test_annotations.json'))

# Pretrained model laden

load_from = 'checkpoints/cascade_rcnn_hrnetv2p_w40_20e_coco_20200512_161112-75e47b04.pth'

