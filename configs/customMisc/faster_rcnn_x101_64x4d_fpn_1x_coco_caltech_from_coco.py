_base_ = '../faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py'


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

#http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth


load_from = 'checkpoints/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth'

work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/faster_rcnn_x101_64x4d_fpn_1x_coco_from_coco'
