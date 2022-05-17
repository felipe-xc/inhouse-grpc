import random
from time import sleep
import grpc
from concurrent import futures
from calculator.calculator_pb2 import CalcRequest, NumericResult
from calculator import calculator_pb2_grpc
from trainer.dummy_trainer_pb2 import (StartTrainRequest, TrainStartResponse,
                                       TrainResponse, TrainProgressResponse,
                                       TrainCompletionResponse, TrainErrorResponse)
from trainer import dummy_trainer_pb2_grpc


class CalcService(calculator_pb2_grpc.CalculatorServicer):

    def SumNumbers(self, request, context):
        return NumericResult(result=request.numberA + request.numberB)

    def SubtractNumbers(self, request, context):
        return NumericResult(result=request.numberA - request.numberB)


class TrainerService(dummy_trainer_pb2_grpc.DummyTrainerServicer):

    def StartTrain(self, request: StartTrainRequest, context):
        print(request)
        yield TrainResponse(start_response=TrainStartResponse(success=True))
        for epoch in range(10):
            sleep(2)
            if random.random() < 0.05:
                yield TrainResponse(
                    error_response=TrainErrorResponse(
                        error_type=TrainErrorResponse.ErrorType.OTHER, error_message="dummy error"))
                return

            yield TrainResponse(progress_response=TrainProgressResponse(epoch=epoch))
        yield TrainResponse(completion_response=TrainCompletionResponse(model_path="saved/path"))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalcService(), server
    )
    dummy_trainer_pb2_grpc.add_DummyTrainerServicer_to_server(TrainerService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
