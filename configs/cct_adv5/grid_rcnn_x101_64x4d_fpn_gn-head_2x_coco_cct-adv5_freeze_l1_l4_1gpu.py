# Basiskonfigurationsfile
_base_ = '../grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco.py'

dataset_type = 'CaltechDataset'
classes = ('racoon', 'squirrel', 'bobcat', 'dog', 'coyote', 'rabbit', 'bird', 'cat', 'deer', 'fox') #10 classes

model = dict(
		backbone=dict(
       
        		frozen_stages=4
        	),
    		roi_head=dict(
    			bbox_head=dict(
    			 num_classes=10
    			)
        	)
       )


data = dict(
    train=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        ann_file='customDataCaltech/caltech_adv/eccv_train_adv.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_adv.json'),
    test=dict(
    	type='CocoDataset',
        #img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/caltech_adv/eccv_val_TEST_adv.json'))


#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) original (2x8=16)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)

evaluation = dict(classwise=True, interval=1, metric='bbox')

# Pretrained model laden
load_from = 'checkpoints/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth'

#http://download.openmmlab.com/mmdetection/v2.0/grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth

