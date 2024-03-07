import os
import sys

import grpc

FILE = __file__ if "__file__" in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, "../../../utils/pb/fraud_detection"))
sys.path.insert(0, utils_path)

# ruff : noqa: E402
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

_FRAUD_DETECTION_SERVICE = "fraud_detection:50051"


def greet(name="you"):
    with grpc.insecure_channel(_FRAUD_DETECTION_SERVICE) as channel:
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting


def health_check():
    with grpc.insecure_channel(_FRAUD_DETECTION_SERVICE) as channel:
        stub = fraud_detection_grpc.FraudDetectionServiceStub(channel)
        response = stub.HealthCheck(fraud_detection.HealthCheckRequest())
    return response.status
