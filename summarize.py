#from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from transformers import pipeline

#model_name = "fb-bart-large-cnn"
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSequenceClassification.from_pretrained(model_name)

summarizer = pipeline("summarization", model="fb-bart-large-cnn")

ARTICLE = """In the evolving landscape of hybrid cloud infrastructure, organizations are confronting the complexities of deploying and managing applications across various regions and zones due to latency, availability, compliance, sovereignty, and security concerns. As demand for multitenancy and specialized workload management grows, the limitations of single-cluster setups become evident, pushing businesses towards a multicluster approach. As organizations navigate this shift, they encounter the daunting task of orchestrating and administering multiple clusters efficiently. The need for a cost-effective, scalable, and holistic multicluster Red Hat OpenShift architecture arises as a business priority to maintain a competitive edge and build innovative applications. Recognizing this, a year ago, we introduced a technology preview of hosted control planes for OpenShift, tailored for efficient multicluster deployments. Hosted control planes, which architecturally decouples the control plane from workloads, presents a scalable and economical solution for multicluster management. It helps streamline cluster provisioning and improves resource allocation by leveraging existing OpenShift management infrastructure and tooling. After a year of valuable feedback from our customers and partners, we are happy to announce that hosted control planes for Red Hat OpenShift is now generally available on two critical on-premises platforms: Baremetal via the agent provider and the Red Hat OpenShift Virtualization provider, marking our first milestone in a long and exciting journey."""

print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))