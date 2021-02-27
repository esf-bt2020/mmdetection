# Basiskonfigurationsfile
_base_ = '../centripetalnet/centripetalnet_hourglass104_mstest_16x6_210e_coco.py'

dataset_type = 'CocoDataset'
classes = ('bobcat', 'coyote', 'raccoon', 'bird', 'dog', 'cat', 'squirrel','rabbit', 'deer', 'fox') #10 classes

model = dict(
    type='CornerNet',
    backbone=dict(
        type='HourglassNet',
        downsample_times=5,
        num_stacks=2,
        stage_channels=[256, 256, 384, 384, 384, 512],
        stage_blocks=[2, 2, 2, 2, 2, 4],
        norm_cfg=dict(type='BN', requires_grad=True)),
    neck=None,
    bbox_head=dict(
        type='CentripetalHead',
        num_classes=10,
        in_channels=256,
        num_feat_levels=2,
        corner_emb_channels=0,
        loss_heatmap=dict(
            type='GaussianFocalLoss', alpha=2.0, gamma=4.0, loss_weight=1),
        loss_offset=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1),
        loss_guiding_shift=dict(
            type='SmoothL1Loss', beta=1.0, loss_weight=0.05),
        loss_centripetal_shift=dict(
            type='SmoothL1Loss', beta=1.0, loss_weight=1))
            )



# Modify dataset related settings

data = dict(
	samples_per_gpu=3, #default 6
	workers_per_gpu=3, #default 3

    train=dict(
    	type='CocoDataset',
        #img_prefix='customDataCaltech/caltech_halfsize_adv',
        #img_prefix='/media/Pool/Thesis/Datensets/cct_images',
 	#img_prefix='/home/felice/Datasets/cct_images',
	img_prefix='/media/SSD2project/WilLiCam/datasets/caltech/cct_images',
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
# Pretrained model laden

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #8 GPUs => 8*6=48
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #2 GPUs => 2*3=6 => 6/48= 1/8 cheetah
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x6=6)

evaluation = dict(classwise=True, interval=4, metric='bbox')

load_from = 'checkpoints/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth'

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/centripetalnet_hourglass104_mstest_16x6_210e_coco_cct-adv5v2_2gpu'


#http://download.openmmlab.com/mmdetection/v2.0/centripetalnet/centripetalnet_hourglass104_mstest_16x6_210e_coco/centripetalnet_hourglass104_mstest_16x6_210e_coco_20200915_204804-3ccc61e5.pth

