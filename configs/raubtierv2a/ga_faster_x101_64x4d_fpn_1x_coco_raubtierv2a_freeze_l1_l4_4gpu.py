# Basiskonfigurationsfile
_base_ = '../guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco.py'

model = dict(

backbone=dict(
		frozen_stages=4
	),
	
	roi_head=dict(
		bbox_head=dict(
		num_classes=3
		)

	)

)


dataset_type = 'COCODataset'
classes = ('luchs', 'rotfuchs', 'wolf')
data = dict(
    train=dict(
        img_prefix='raubtierv2a/train/',
        classes=classes,
        ann_file='raubtierv2a/train/_annotations.coco.json'),
    val=dict(
        img_prefix='raubtierv2a/valid/',
        classes=classes,
        ann_file='raubtierv2a/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='raubtierv2a/test/',
        classes=classes,
        ann_file='raubtierv2a/test/_annotations.coco.json'))

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001) #cheetah (2x2=4)
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

total_epochs = 24 #default=12

# Pretrained model laden
load_from = 'checkpoints/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth'
#http://download.openmmlab.com/mmdetection/v2.0/guided_anchoring/ga_faster_x101_64x4d_fpn_1x_coco/ga_faster_x101_64x4d_fpn_1x_coco_20200215-0fa7bde7.pth

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/raubtierv2a/ga_faster_x101_64x4d_fpn_1x_coco_raubtierv2a_freeze_l1_l4_4gpu'

evaluation = dict(classwise=True, interval=1, metric='bbox')


