import grpc
from calculator.calculator_pb2 import CalcRequest
from calculator.calculator_pb2_grpc import CalculatorStub
from google.protobuf.json_format import MessageToDict
if __name__ == '__main__':
    request = CalcRequest(numberA=1, numberB=2)
    print(request)
    channel = grpc.insecure_channel("localhost:5000")
    client = CalculatorStub(channel)
    sub_response = client.SubtractNumbers(request)
    print(f"Response type: {type(sub_response)}")
    print(f"Sub response: {sub_response}")

    sum_response = client.SumNumbers(request)
    print(f"Sum response: {sum_response}")

    # Fail: print(dict(sum_response))

    print(MessageToDict(sum_response))
