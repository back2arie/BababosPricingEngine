# system_architecture.py
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.programming.framework import React
from diagrams.aws.security import WAF
from diagrams.aws.general import Users
from diagrams.aws.mobile import APIGateway
from diagrams.aws.integration import SQS

with Diagram("Bababos Architecture Diagram", show=False, filename="system_architecture_diagram", direction="TB"):
    users = Users("Users")
    waf = WAF("WAF")
    lb = ELB("Load Balancer")
    react = React("Frontend")
    api_gateway = APIGateway("API Gateway")

    with Cluster("Existing System"):
        existing_app = EC2("Service/ API")
        existing_db = RDS("DB")
        existing_app >> existing_db

    with Cluster("Product Service") as product_service:
        product_service = EC2("Service/ API")
        product_db = RDS("Product DB")
        product_service >> product_db

    with Cluster("User Service"):
        user_service = EC2("Service/ API")
        user_db = RDS("User DB")
        user_service >> user_db

    with Cluster("Payment Service"):
        payment_service = EC2("Service/ API")
        payment_db = RDS("Payment DB")
        payment_service >> payment_db

    with Cluster("Supplier Service"):
        supplier_service = EC2("Service/ API")
        supplier_db = RDS("Supplier DB")
        supplier_service >> supplier_db

    with Cluster("Order Service"):
        order_service = EC2("Service/ API")
        order_db = RDS("Order DB")
        order_service >> order_db

    with Cluster("Shipment Service"):
        shipment_service = EC2("Service/ API")
        shipment_db = RDS("Shipment DB")
        shipment_service >> shipment_db

    with Cluster("Message Queue"):
        sqs = SQS("Amazon SQS")

    users >> waf
    waf >> lb
    lb >> react
    react >> api_gateway

    api_gateway >> existing_app
    api_gateway >> product_service
    api_gateway >> user_service
    api_gateway >> payment_service
    api_gateway >> supplier_service
    api_gateway >> order_service
    api_gateway >> shipment_service

    existing_app - sqs
    product_service - sqs
    user_service - sqs
    payment_service - sqs
    supplier_service - sqs
    order_service - sqs
    shipment_service - sqs

