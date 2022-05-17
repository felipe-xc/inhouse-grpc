import grpc
from concurrent import futures
from calculator.calculator_pb2 import CalcRequest, NumericResult
from calculator import calculator_pb2_grpc


class CalcService(calculator_pb2_grpc.CalculatorServicer):

    def SumNumbers(self, request, context):
        return NumericResult(result=request.numberA + request.numberB)

    def SubtractNumbers(self, request, context):
        return NumericResult(result=request.numberA - request.numberB)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalcService(), server
    )
    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
