_base_ = '../gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco.py'

model = dict(

	backbone=dict(
        	frozen_stages=4
        ),

        bbox_head=dict(num_classes=10)
        

#train_cfg = dict(
#    assigner=dict(type='ATSSAssigner', topk=2),
#    allowed_border=-1,
#    pos_weight=-1,
#    debug=False)
    )

dataset_type = 'CocoDataset'
classes = ('raccoon', 'squirrel', 'bobcat', 'dog', 'coyote', 'rabbit', 'bird', 'cat', 'deer', 'fox') #10 classes

data = dict(
    train=dict(
    	type='CocoDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	img_prefix='/home/felice/Datasets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_train.json'),
    val=dict(
    	type='CocoDataset',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
	img_prefix='/home/felice/Datasets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_val.json'),
    test=dict(
    	type='CocoDataset',
	img_prefix='/home/felice/Datasets/cct_images',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
        classes=classes,
        ann_file='customDataCaltech/adv5/adv5_known_test.json'))

total_epochs = 36 #default 24epochs

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/xyz'

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth'

#http://download.openmmlab.com/mmdetection/v2.0/gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth
