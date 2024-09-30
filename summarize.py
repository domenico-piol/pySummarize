from transformers import pipeline
import logging
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/')
def show_complaints_page():
    app.logger.info('Summarizer application root called')
    htmlPageHeader = "<!DOCTYPE html><html><body>"
    htmlPageContent = "<h1>Welcome to our complaints summarizer</h1>"
    htmlPageContent += "<p>"
    htmlPageContent += "You can use this summarization model by calling:" + "</p>"
    htmlPageContent += "<code>https://{URL}}:443/summarize/'ARTICLE TO SUMMARIZE'<code>"
    htmlPageFooter = "</body></html>"

    return htmlPageHeader + htmlPageContent + htmlPageFooter, 200


@app.route('/summarize/', methods=['GET'])
@app.route('/summarize/<article>', methods=['GET'])
def get_summarization(article=""):
    app.logger.info('Summarizing an article')
    summarizer = pipeline("summarization", model="/opt/bart-large-cnn")

    DUMMY = """In the evolving landscape of hybrid cloud infrastructure, organizations are confronting the complexities of deploying and managing applications across various regions and zones due to latency, availability, compliance, sovereignty, and security concerns. As demand for multitenancy and specialized workload management grows, the limitations of single-cluster setups become evident, pushing businesses towards a multicluster approach. As organizations navigate this shift, they encounter the daunting task of orchestrating and administering multiple clusters efficiently. The need for a cost-effective, scalable, and holistic multicluster Red Hat OpenShift architecture arises as a business priority to maintain a competitive edge and build innovative applications. Recognizing this, a year ago, we introduced a technology preview of hosted control planes for OpenShift, tailored for efficient multicluster deployments. Hosted control planes, which architecturally decouples the control plane from workloads, presents a scalable and economical solution for multicluster management. It helps streamline cluster provisioning and improves resource allocation by leveraging existing OpenShift management infrastructure and tooling. After a year of valuable feedback from our customers and partners, we are happy to announce that hosted control planes for Red Hat OpenShift is now generally available on two critical on-premises platforms: Baremetal via the agent provider and the Red Hat OpenShift Virtualization provider, marking our first milestone in a long and exciting journey."""

    if article == "":
        article = DUMMY

    responseJson = summarizer(article, max_length=130, min_length=30, do_sample=False)

    if len(responseJson) > 0:
        return jsonify(responseJson[0]), 200
    else:
        app.logger.error('an error occurred')
        return "No summarization was possible", 500


app.run(host="0.0.0.0", port=5443, ssl_context="adhoc")
