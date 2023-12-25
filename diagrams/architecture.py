# architecture.py
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.programming.framework import React, Django
from diagrams.onprem.queue import Celery
from diagrams.aws.security import WAF
from diagrams.aws.general import Users
from diagrams.aws.mobile import APIGateway

with Diagram("Bababos Architecture Diagram", show=False, filename="architecture_diagram", direction="LR"):
    users = Users("Users")
    waf = WAF("WAF")
    lb = ELB("Load Balancer")
    react = React("Frontend")
    api_gateway = APIGateway("API Gateway")

    with Cluster("Existing System"):
        existing_app = EC2("Service/ API")
        existing_db = RDS("DB")
        existing_app >> existing_db

    with Cluster("Pricing Engine"):
        django = Django("REST API")
        celery = Celery("Celery Worker")
        db = RDS("Pricing DB")
        django >> celery
        django >> db

    users >> waf
    waf >> lb
    lb >> react
    react >> api_gateway

    api_gateway >> django
    api_gateway >> existing_app