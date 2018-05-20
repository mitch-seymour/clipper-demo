from clipper_admin import ClipperConnection, DockerContainerManager
from clipper_admin.deployers import python as python_deployer
import time

def feature_sum(xs):
    return [str(sum(x)) for x in xs]

if __name__ == "__main__":
	
	try:
		# create a connection to our clipper cluster
		clipper_conn = ClipperConnection(DockerContainerManager())
		clipper_conn.stop_all()
		clipper_conn.start_clipper()

		# register the prediction service
		clipper_conn.register_application(name="hello-world", input_type="doubles", default_output="-1.0", slo_micros=100000)

		# deploy the prediction service
		python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=1, input_type="doubles", func=feature_sum)

		# link the prediction service to the query API
		clipper_conn.link_model_to_app(app_name="hello-world", model_name="sum-model")
		
		while True:
			time.sleep(2)
	except KeyboardInterrupt:
		print('interrupted!')
		clipper_conn.stop_all()
	except Exception as e:
		clipper_conn.stop_all()
		raise e
