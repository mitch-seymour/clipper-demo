# clipper-demo
Basic example of deploying a [clipper server](https://github.com/ucbrise/clipper), and deploying an update to an existing
prediction model.

## Pre-requisites
- [anaconda](https://www.anaconda.com/download/#macos)
- [autoenv](https://github.com/kennethreitz/autoenv) (optional)

## Setup
```bash
# clone this repo
$ git clone git@github.com:mitch-seymour/clipper-demo.git
$ cd clipper-demo

# install the dependencies
$ conda create --name clipper --file requirements.txt
```

## Example
- Runs a clipper server locally ([server.py](server.py))
- Deploys a prediction model ([server.py](server.py))
- Updates the prediction model ([update_model.py](update_model.py))

```bash
# activate our anaconda environment for this project
# pro tip, if you setup autoenv, the clipper project should be set automatically
# when you cd into this directory
$ source activate clipper

# install clipper directly from github
$ pip install git+https://github.com/ucbrise/clipper.git@develop#subdirectory=clipper_admin
```

Okay, now start the clipper server. This will take several minutes the first time since the necessary Docker images will
need to be installed.
```bash
$ python server.py
```

Once the server is running, you should be able to hit the query API to run a prediction:
```bash
$ curl -X POST --header "Content-Type:application/json" -d '{"input": [1.1, 2.2, 3.3]}' 127.0.0.1:1337/hello-world/predict

# output
{"query_id":3,"output":6.6,"default":false}
```

Notice the output above has a value of `6.6`. Now, lets deploy an update to the model, and simply multiply the current output
by `2`. In a separate window, run the following:

```bash
# always do this first unless you have autoenv installed
$ source activate clipper

# deploy an update to the model
$ python update_model.py
```

Finally, run the `curl` command, and notice how the results changed (because our model was updated).

```bash
$ curl -X POST --header "Content-Type:application/json" -d '{"input": [1.1, 2.2, 3.3]}' 127.0.0.1:1337/hello-world/predict

# output
{"query_id":4,"output":13.2,"default":false}
```
