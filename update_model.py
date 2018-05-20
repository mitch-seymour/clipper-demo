from clipper_admin import ClipperConnection, DockerContainerManager
from clipper_admin.deployers import python as python_deployer
import time

def feature_sum(xs):
    return [str(sum(x)*2) for x in xs]

if __name__ == "__main__":
	
	# create a connection to our clipper cluster
	clipper_conn = ClipperConnection(DockerContainerManager())
	clipper_conn.connect()

	# deploy v2 of the prediction service
	python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=2, input_type="doubles", func=feature_sum)
