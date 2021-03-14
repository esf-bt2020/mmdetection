_base_ = '../gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco.py'

model = dict(

	backbone=dict(
        	#frozen_stages=4
        ),

        bbox_head=dict(num_classes=3)
        

#train_cfg = dict(
#    assigner=dict(type='ATSSAssigner', topk=2),
#    allowed_border=-1,
#    pos_weight=-1,
#    debug=False)
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

total_epochs = 48 #default 24epochs

#optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001) #original (8x2=16)
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001) #(4x2=8) 4 GPUs
#optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #(1x2=2)

evaluation = dict(classwise=True, interval=1, metric='bbox')

#work_dir = '/media/SSD2project/WilLiCam/checkpoint_workdir/xyz'
work_dir = '/media/storage1/projects/WilLiCam/checkpoint_workdir/raubtierv2a/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_raubtierv2a_nofreeze_4gpu'

# Use the pre-trained model to obtain higher performance
load_from = 'checkpoints/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth'

#http://download.openmmlab.com/mmdetection/v2.0/gfl/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco/gfl_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20200630_102002-134b07df.pth
