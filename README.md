# inhouse-grpc

To generate server and client python base code from the calculator protobuf:

``` bash
mkdir calculator
cd calculator
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/calculator.proto
```
