# ml_pipeline

A data pipeline that loads data, trains a model, and deploys the model to a web service.

This example assumes you have Docker installed. A virtual environment should also be used to install python 3.6+ and the dependencies in requirements.txt.

Before running the pipeline, the webserver that uses the model should be started by running the start_server.sh script.

## Explanation

The pipeline is split into three stages:

* etl
* train
* deploy

The etl stage starts by downloading the winequality-red dataset as a csv file. It then runs etl.py which abstracts away the details of converting the csv file to a feather file.

The train stage abstracts away details about training a model based on the data in the feather file. This allows for flexibility in defining a model by providing a single interface (train.py) that can accept input arguments from the command line for building the model. The output of train.py is written to a text file and the model, as a pickle file, is gpg signed and encrypted for improved security. This step is likely unnecessary when running the webserver on the same machine where the model is generated, but is recommend when uploading the model to a different machine.

The deploy stage will remove the model currently being used by the webserver, and gpg decrypt and verify the new model. The webserver is then restarted and will pick up and use the new model.
