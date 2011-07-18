from pybrain.rl.environments.ode import CCRLEnvironment
from pybrain.rl.environments.ode.tasks import CCRLGlasTask
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules.tanhlayer import TanhLayer
from pybrain.optimization import PGPE
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment

environment = CCRLEnvironment()
task = CCRLGlasTask(environment)
net = buildNetwork(len(task.getObservation()),4,environment.indim,outclass=TanhLayer)

agent = OptimizationAgent(net,PGPE())
experiment = EpisodicExperiment(task,agent)
for updates in range(20000):
    experiment.doEpisode()

