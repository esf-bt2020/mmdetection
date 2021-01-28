# Basiskonfigurationsfile
_base_ = '../libra_rcnn/libra_faster_rcnn_x101_64x4d_fpn_1x_coco.py'


# Modify dataset related settings
dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

model = dict(
	
	roi_head=dict(
	
		bbox_head=dict(
		    type='Shared2FCBBoxHead',
		    in_channels=256,
		    fc_out_channels=1024,
		    roi_feat_size=7,
		    num_classes=22,
		    bbox_coder=dict(
		        type='DeltaXYWHBBoxCoder',
		        target_means=[0.0, 0.0, 0.0, 0.0],
		        target_stds=[0.1, 0.1, 0.2, 0.2]),
		    reg_class_agnostic=False,
		    loss_cls=dict(
		        type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
		    loss_bbox=dict(
		        type='BalancedL1Loss',
		        alpha=0.5,
		        gamma=1.5,
		        beta=1.0,
		        loss_weight=1.0)
		 )
	)

)

data = dict(
    train=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CaltechDataset',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CaltechDataset',
         img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/libra_fasterrcnn_caltechclean'

