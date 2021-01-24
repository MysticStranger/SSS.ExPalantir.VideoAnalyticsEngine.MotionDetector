# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import MotionDetectionService_pb2 as MotionDetectionService__pb2


class MotionDetectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Analyze = channel.unary_unary(
                '/MotionDetectionService/Analyze',
                request_serializer=MotionDetectionService__pb2.MotionDetectionRequest.SerializeToString,
                response_deserializer=MotionDetectionService__pb2.MotionDetectionResponse.FromString,
                )


class MotionDetectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Analyze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MotionDetectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Analyze': grpc.unary_unary_rpc_method_handler(
                    servicer.Analyze,
                    request_deserializer=MotionDetectionService__pb2.MotionDetectionRequest.FromString,
                    response_serializer=MotionDetectionService__pb2.MotionDetectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MotionDetectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MotionDetectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Analyze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MotionDetectionService/Analyze',
            MotionDetectionService__pb2.MotionDetectionRequest.SerializeToString,
            MotionDetectionService__pb2.MotionDetectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)