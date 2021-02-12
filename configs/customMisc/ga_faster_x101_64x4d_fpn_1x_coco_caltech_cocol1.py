# Basiskonfigurationsfile
_base_ = '../guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco.py'

model = dict(
	roi_head=dict(
		bbox_head=dict(
		num_classes=22
		)

	)

)


dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

data = dict(
    train=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))

# Pretrained model laden
load_from = 'checkpoints/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth'
#http://download.openmmlab.com/mmdetection/v2.0/guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth

evaluation = dict(classwise=True, interval=1, metric='bbox')

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/ga_faster_caltech_cocol1'

