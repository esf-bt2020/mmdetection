# Basiskonfigurationsfile
_base_ = '../guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco.py'

model = dict(

backbone=dict(
		frozen_stages=1
	),
	
	roi_head=dict(
		bbox_head=dict(
		num_classes=10
		)

	)

)


dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

data = dict(
    train=dict(
    	type='CocoDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
 	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	#img_prefix='/content/drive/MyDrive/_Dataset/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	#img_prefix='/content/drive/MyDrive/_Dataset/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
	#img_prefix='/home/felice/Datasets/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
	#img_prefix='/content/drive/MyDrive/_Dataset/cct_images_bbox_all',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)

total_epochs = 16 #default=12

# Pretrained model laden
load_from = 'checkpoints/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth'
#http://download.openmmlab.com/mmdetection/v2.0/guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth

evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/content/drive/MyDrive/Colab_Export/ga_faster_x101_cct-adv5v2'
work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/ga_faster_x101_64x4d_fpn_1x_coco_cct-adv5v2_nofreeze_2gpu'

