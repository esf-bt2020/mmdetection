# Basiskonfigurationsfile
_base_ = '../grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco.py'


model = dict(
		backbone=dict(
       
        		#frozen_stages=4
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


#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) original (2x8=16)
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)

evaluation = dict(classwise=True, interval=1, metric='bbox')

total_epochs = 48

work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/raubtierv2a/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_raubtierv2a_nofreeze_4gpu'

# Pretrained model laden
load_from = 'checkpoints/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth'

#http://download.openmmlab.com/mmdetection/v2.0/grid_rcnn/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco/grid_rcnn_x101_64x4d_fpn_gn-head_2x_coco_20200204-ec76a754.pth

