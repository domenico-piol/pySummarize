# PySummarize
PySummarize is a Python/Flask web-application providing a REST service for large text summarization. It's using the [Huggingface facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) model.

The runnable application is containerized and available on [docker.io](https://hub.docker.com/repository/docker/domenicopiol/pysummarize/general). Use it as follows:

    https://pysummarize-runtime.example.net:443/summarize/"ARTICLE TO SUMMARIZE"

Be aware, due to its size this Git repo does NOT contain the pre-built model itself. That can be obtained from Huggingface e.g. using:

    wget https://huggingface.co/facebook/bart-large-cnn/resolve/main/pytorch_model.bin

For local usage, place it e.g. in the `fb-bart-large-cnn` (or any other) folder and configure the Python app accordingly.

However, during runtime on OpenShift (or any k8s flavor), the model will be obtained via a init-container!

## How-to run
### Locally with Podman
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

### On OpenShift (or any k8s flavor)
For deploying the demo-app to OpenShift, use the `k8s/summarize.yaml` deployment descriptor.

    oc deploy -f k8s/summarize.yaml

The deployment will use an init-container for obtaining the model from Huggingface using the huggingface-cli.
The init-container starts the model-downloader script `dl.sh` which expects some parameters:

    -m the model
    -d the directory where to place the model
    -f a list of files to download

The `summarize.yaml` descriptor file contains already a comprehensive working example.


## Example
Let's take an announcement made by Red Hat some time back:

> In the evolving landscape of hybrid cloud infrastructure, organizations are confronting the complexities of deploying and managing applications across various regions and zones due to latency, availability, compliance, sovereignty, and security concerns. As demand for multitenancy and specialized workload management grows, the limitations of single-cluster setups become evident, pushing businesses towards a multicluster approach. 
>
>As organizations navigate this shift, they encounter the daunting task of orchestrating and administering multiple clusters efficiently. The need for a cost-effective, scalable, and holistic multicluster Red Hat OpenShift architecture arises as a business priority to maintain a competitive edge and build innovative applications. Recognizing this, a year ago, we introduced a technology preview of hosted control planes for OpenShift, tailored for efficient multicluster deployments. Hosted control planes, which architecturally decouples the control plane from workloads, presents a scalable and economical solution for multicluster management. It helps streamline cluster provisioning and improves resource allocation by leveraging existing OpenShift management infrastructure and tooling. 
>
>After a year of valuable feedback from our customers and partners, we are happy to announce that hosted control planes for Red Hat OpenShift is now generally available on two critical on-premises platforms: Baremetal via the agent provider and the Red Hat OpenShift Virtualization provider, marking our first milestone in a long and exciting journey.

The output is then something like:

    {
        "summary_text":
            "Hosted control planes for Red Hat OpenShift is now generally available on two critical on-premises platforms. It helps streamline cluster provisioning and improves resource allocation by leveraging existing OpenShift management infrastructure."
    }