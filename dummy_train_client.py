import grpc
from trainer.dummy_trainer_pb2_grpc import DummyTrainerStub
from trainer.dummy_trainer_pb2 import StartTrainRequest
from google.protobuf.json_format import MessageToDict

if __name__ == '__main__':
    channel = grpc.insecure_channel("localhost:5000")
    trainer_client = DummyTrainerStub(channel)
    request = StartTrainRequest(data_path="test/data/path")
    for res in trainer_client.StartTrain(request):
        print(MessageToDict(res))
