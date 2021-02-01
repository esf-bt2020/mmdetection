# Basiskonfigurationsfile
_base_ = '../grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco.py'

dataset_type = 'CaltechDataset'
classes = ('bobcat', 'opossum', 'empty', 'coyote', 'racoon', 'bird', 'dog', 'cat', 'squirrel', 'rabbit', 'skunk', 'lizard', 'rodent', 'badger', 'deer', 'cow', 'car', 'fox', 'pig','mountain_lion', 'bat', 'insect')

model = dict(
    		roi_head=dict(
    			bbox_head=dict(
    			 num_classes=22
    			)
        	)
       )


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

total_epochs = 40

# Pretrained model laden
#load_from = 'checkpoints/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth'

#http://download.openmmlab.com/mmdetection/v2.0/grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/grid_rcnn_caltech_clean'
