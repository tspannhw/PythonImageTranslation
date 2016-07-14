from sailfish.config import MachineSpec

nodes = [
	MachineSpec('ssh=ubuntu@192.168.1.3', 'hosta', cuda_nvcc='/usr/local/cuda/bin/nvcc', gpus=[0]),
	MachineSpec('ssh=ubuntu@localhost', 'hostb', cuda_nvcc='/usr/local/cuda/bin/nvcc', gpus=[0], block_size=256)
]
