import HarassmentDetector as ihd

hd = ihd.HarassmentDetector()
hd.init()

hd.detect([0., 0.92, 0., 0., 0., 0.98, 0., 0., 0., 0.])
hd.detect([0.92, 0., 0., 0., 0., 0., 0.98, 0., 0., 0.])
