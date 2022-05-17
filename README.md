# inhouse-grpc

## Important

In order to keep codes generated from different protobuf on different folders, the protobuffers should be kept in different folders as well (<https://github.com/grpc/grpc/issues/9575#issuecomment-293934506>)

## Steps

### Calculator
To generate server and client python base code from the calculator protobuf:

``` bash
python -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/calculator/calculator.proto
```

### Dummy Trainer
To generate server and client python base code from dummy trainer protobuf:
``` bash
python -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. /protobufs/trainer/dummy_trainer.proto
```
