from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_ibm_runtime import QiskitRuntimeService
 
 
token = 'bb1d4f76d97ab2490f97129e211e44de6d771025a34b5866c287315d757c8d95a4c01b7e4e35d3eaafc2f56959162444dd22563b97edf26294dea21b91fe8146'
 
print(token)
QiskitRuntimeService.save_account(
  token=token,
  channel="ibm_quantum",
  overwrite=True
)
 
# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
 
sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")