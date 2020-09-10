https://www.zhihu.com/question/25536695/answer/36197244

https://www.jb51.net/article/153923.htm

https://grpc.io/docs/languages/python/basics/

https://blog.csdn.net/gx864102252/article/details/81349093/
https://juejin.im/user/3104676535872733

码农之家:
https://www.xz577.com/e/279.html
https://www.xz577.com/e/rzks/


编译protobuf文件：使用以下命令生成Python代码：

python3 -m grpc_tools.protoc -I<目标路径目录> --python_out=. --grpc_python_out=<目标文件所在目录路径> <目标文件data.proto>

eg:
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto # 在 example 目录中执行编译，会生成：data_pb2.py 与 data_pb2_grpc.py


python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. data.proto

注意：protobuf文件，为定义服务接口代码文件，这里是data.proto

会生成：data_pb2.py 与 data_pb2_grpc.py

data_pb2.py是服务接口映射

data_pb2_grpc.py方法映射