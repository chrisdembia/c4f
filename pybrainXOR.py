from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork( 2, 4, 1)

ds = SupervisedDataSet(2,1)

ds.addSample( (0,0), (0,) )
ds.addSample( (0,1), (1,) )
ds.addSample( (1,0), (1,) )
ds.addSample( (1,1), (0,) )

trainer = BackpropTrainer(net,  learningrate = 0.01, momentum = .99)

print 'MSE before', trainer.testOnData(ds)
trainer.trainOnDataset(ds,1000)
print 'MSE after',trainer.testOnData(ds)

