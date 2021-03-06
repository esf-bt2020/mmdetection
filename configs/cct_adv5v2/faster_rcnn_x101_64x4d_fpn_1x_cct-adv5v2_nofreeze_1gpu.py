_base_ = '../faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py'

dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

model = dict(

backbone=dict(
       
        	num_stages=4,
        	frozen_stages=1
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
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
	#img_prefix='/home/felice/Datasets/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))
        
#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)
#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)

total_epochs=48

evaluation = dict(classwise=True, interval=1, metric='bbox')

#http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/faster_rcnn_x101_64x4d_fpn_1x_cct-adv5v2_nofreeze_1gpu'


load_from = 'checkpoints/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth'
