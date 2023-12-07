# PySummarize
PySummarize is a Python/Flask web-application providing a REST service for large text summarization. It's using the [Huggingface facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) model.

The runnable application is containerized and available on [docker.io](https://hub.docker.com/repository/docker/domenicopiol/pysummarize/general). Use it as follows:

    https://pysummarize-runtime.example.net:443/summarize/"ARTICLE TO SUMMARIZE"

Be aware, due to its size this Git repo does NOT contain the pre-built model itself. That can be obtained from Huggingface using:

    wget https://huggingface.co/facebook/bart-large-cnn/resolve/main/pytorch_model.bin

Place it in the `fb-bart-large-cnn` folder.

## How-to run
You can run the application locally by simply:

    python summarize.py
or

    python3 summarize.py
depending on your environment.

For creating the container image, use:

    podman build -t mydomain/pysummarize .

Run the container in Podman:

    podman run --name pysummarize -it -d -p 443:5443 mydomain/pysummarize

or in OpenShift by using the deployment descriptor in th e`k8s`folder.`