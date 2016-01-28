################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################

from __future__ import print_function
import os, sys
from ctypes import *
from ctypes.util import find_library
import czmq

# malamute
try:
    # If LD_LIBRARY_PATH or your OSs equivalent is set, this is the only way to
    # load the library.  If we use find_library below, we get the wrong result.
    if os.name == 'posix':
        if sys.platform == 'darwin':
            lib = cdll.LoadLibrary('libmlm.0.dylib')
        else:
            lib = cdll.LoadLibrary("libmlm.so.0")
    elif os.name == 'nt':
        lib = cdll.LoadLibrary('libmlm.dll')
except OSError:
    libpath = find_library("malamute")
    if not libpath:
        raise ImportError("Unable to find libmlm")
    lib = cdll.LoadLibrary(libpath)

class mlm_proto_t(Structure):
    pass # Empty - only for type checking
mlm_proto_p = POINTER(mlm_proto_t)

class mlm_client_t(Structure):
    pass # Empty - only for type checking
mlm_client_p = POINTER(mlm_client_t)


# mlm_proto
lib.mlm_proto_new.restype = mlm_proto_p
lib.mlm_proto_new.argtypes = []
lib.mlm_proto_destroy.restype = None
lib.mlm_proto_destroy.argtypes = [POINTER(mlm_proto_p)]
lib.mlm_proto_recv.restype = c_int
lib.mlm_proto_recv.argtypes = [mlm_proto_p, czmq.zsock_p]
lib.mlm_proto_send.restype = c_int
lib.mlm_proto_send.argtypes = [mlm_proto_p, czmq.zsock_p]
lib.mlm_proto_print.restype = None
lib.mlm_proto_print.argtypes = [mlm_proto_p]
lib.mlm_proto_routing_id.restype = czmq.zframe_p
lib.mlm_proto_routing_id.argtypes = [mlm_proto_p]
lib.mlm_proto_set_routing_id.restype = None
lib.mlm_proto_set_routing_id.argtypes = [mlm_proto_p, czmq.zframe_p]
lib.mlm_proto_id.restype = c_int
lib.mlm_proto_id.argtypes = [mlm_proto_p]
lib.mlm_proto_set_id.restype = None
lib.mlm_proto_set_id.argtypes = [mlm_proto_p, c_int]
lib.mlm_proto_command.restype = c_char_p
lib.mlm_proto_command.argtypes = [mlm_proto_p]
lib.mlm_proto_address.restype = c_char_p
lib.mlm_proto_address.argtypes = [mlm_proto_p]
lib.mlm_proto_set_address.restype = None
lib.mlm_proto_set_address.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_stream.restype = c_char_p
lib.mlm_proto_stream.argtypes = [mlm_proto_p]
lib.mlm_proto_set_stream.restype = None
lib.mlm_proto_set_stream.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_pattern.restype = c_char_p
lib.mlm_proto_pattern.argtypes = [mlm_proto_p]
lib.mlm_proto_set_pattern.restype = None
lib.mlm_proto_set_pattern.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_subject.restype = c_char_p
lib.mlm_proto_subject.argtypes = [mlm_proto_p]
lib.mlm_proto_set_subject.restype = None
lib.mlm_proto_set_subject.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_content.restype = czmq.zmsg_p
lib.mlm_proto_content.argtypes = [mlm_proto_p]
lib.mlm_proto_get_content.restype = czmq.zmsg_p
lib.mlm_proto_get_content.argtypes = [mlm_proto_p]
lib.mlm_proto_set_content.restype = None
lib.mlm_proto_set_content.argtypes = [mlm_proto_p, POINTER(czmq.zmsg_p)]
lib.mlm_proto_sender.restype = c_char_p
lib.mlm_proto_sender.argtypes = [mlm_proto_p]
lib.mlm_proto_set_sender.restype = None
lib.mlm_proto_set_sender.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_tracker.restype = c_char_p
lib.mlm_proto_tracker.argtypes = [mlm_proto_p]
lib.mlm_proto_set_tracker.restype = None
lib.mlm_proto_set_tracker.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_timeout.restype = c_int
lib.mlm_proto_timeout.argtypes = [mlm_proto_p]
lib.mlm_proto_set_timeout.restype = None
lib.mlm_proto_set_timeout.argtypes = [mlm_proto_p, c_int]
lib.mlm_proto_status_code.restype = c_short
lib.mlm_proto_status_code.argtypes = [mlm_proto_p]
lib.mlm_proto_set_status_code.restype = None
lib.mlm_proto_set_status_code.argtypes = [mlm_proto_p, c_short]
lib.mlm_proto_status_reason.restype = c_char_p
lib.mlm_proto_status_reason.argtypes = [mlm_proto_p]
lib.mlm_proto_set_status_reason.restype = None
lib.mlm_proto_set_status_reason.argtypes = [mlm_proto_p, c_char_p]
lib.mlm_proto_amount.restype = c_short
lib.mlm_proto_amount.argtypes = [mlm_proto_p]
lib.mlm_proto_set_amount.restype = None
lib.mlm_proto_set_amount.argtypes = [mlm_proto_p, c_short]
lib.mlm_proto_test.restype = None
lib.mlm_proto_test.argtypes = [c_bool]

class MlmProto(object):
    """
    Set the content field, transferring ownership from caller
    """

    SUCCESS = 200 # 
    STORED = 201 # 
    DELIVERED = 202 # 
    NOT_DELIVERED = 300 # 
    CONTENT_TOO_LARGE = 301 # 
    TIMEOUT_EXPIRED = 302 # 
    CONNECTION_REFUSED = 303 # 
    RESOURCE_LOCKED = 400 # 
    ACCESS_REFUSED = 401 # 
    NOT_FOUND = 404 # 
    COMMAND_INVALID = 500 # 
    NOT_IMPLEMENTED = 501 # 
    INTERNAL_ERROR = 502 # 
    CONNECTION_OPEN = 1 # 
    CONNECTION_PING = 2 # 
    CONNECTION_PONG = 3 # 
    CONNECTION_CLOSE = 4 # 
    STREAM_WRITE = 5 # 
    STREAM_READ = 6 # 
    STREAM_SEND = 7 # 
    STREAM_DELIVER = 8 # 
    MAILBOX_SEND = 9 # 
    MAILBOX_DELIVER = 10 # 
    SERVICE_SEND = 11 # 
    SERVICE_OFFER = 12 # 
    SERVICE_DELIVER = 13 # 
    OK = 14 # 
    ERROR = 15 # 
    CREDIT = 16 # 
    CONFIRM = 17 # 
    allow_destruct = False
    def __init__(self, *args):
        """
        Create a new empty mlm_proto
        """
        if len(args) == 2 and type(args[0]) is c_void_p and isinstance(args[1], bool):
            self._as_parameter_ = cast(args[0], mlm_proto_p) # Conversion from raw type to binding
            self.allow_destruct = args[1] # This is a 'fresh' value, owned by us
        elif len(args) == 2 and type(args[0]) is mlm_proto_p and isinstance(args[1], bool):
            self._as_parameter_ = args[0] # Conversion from raw type to binding
            self.allow_destruct = args[1] # This is a 'fresh' value, owned by us
        else:
            assert(len(args) == 0)
            self._as_parameter_ = lib.mlm_proto_new() # Creation of new raw type
            self.allow_destruct = True

    def __del__(self):
        """
        Destroy a mlm_proto instance
        """
        if self.allow_destruct:
            lib.mlm_proto_destroy(byref(self._as_parameter_))

    def __bool__(self):
        "Determine whether the object is valid by converting to boolean" # Python 3
        return self._as_parameter_.__bool__()

    def __nonzero__(self):
        "Determine whether the object is valid by converting to boolean" # Python 2
        return self._as_parameter_.__nonzero__()

    def recv(self, input):
        """
        Receive a mlm_proto from the socket. Returns 0 if OK, -1 if
there was an error. Blocks if there is no message waiting.
        """
        return lib.mlm_proto_recv(self._as_parameter_, input)

    def send(self, output):
        """
        Send the mlm_proto to the output socket, does not destroy it
        """
        return lib.mlm_proto_send(self._as_parameter_, output)

    def print(self):
        """
        Print contents of message to stdout
        """
        return lib.mlm_proto_print(self._as_parameter_)

    def routing_id(self):
        """
        Get the message routing id, as a frame
        """
        return czmq.Zframe(lib.mlm_proto_routing_id(self._as_parameter_), False)

    def set_routing_id(self, routing_id):
        """
        Set the message routing id from a frame
        """
        return lib.mlm_proto_set_routing_id(self._as_parameter_, routing_id)

    def id(self):
        """
        Get the mlm_proto message id
        """
        return lib.mlm_proto_id(self._as_parameter_)

    def set_id(self, id):
        """
        Set the mlm_proto message id
        """
        return lib.mlm_proto_set_id(self._as_parameter_, id)

    def command(self):
        """
        Get the mlm_proto message id as printable text
        """
        return lib.mlm_proto_command(self._as_parameter_)

    def address(self):
        """
        Get the address field
        """
        return lib.mlm_proto_address(self._as_parameter_)

    def set_address(self, address):
        """
        Set the address field
        """
        return lib.mlm_proto_set_address(self._as_parameter_, address)

    def stream(self):
        """
        Get the stream field
        """
        return lib.mlm_proto_stream(self._as_parameter_)

    def set_stream(self, stream):
        """
        Set the stream field
        """
        return lib.mlm_proto_set_stream(self._as_parameter_, stream)

    def pattern(self):
        """
        Get the pattern field
        """
        return lib.mlm_proto_pattern(self._as_parameter_)

    def set_pattern(self, pattern):
        """
        Set the pattern field
        """
        return lib.mlm_proto_set_pattern(self._as_parameter_, pattern)

    def subject(self):
        """
        Get the subject field
        """
        return lib.mlm_proto_subject(self._as_parameter_)

    def set_subject(self, subject):
        """
        Set the subject field
        """
        return lib.mlm_proto_set_subject(self._as_parameter_, subject)

    def content(self):
        """
        Get a copy of the content field
        """
        return czmq.Zmsg(lib.mlm_proto_content(self._as_parameter_), False)

    def get_content(self):
        """
        Get the content field and transfer ownership to caller
        """
        return czmq.Zmsg(lib.mlm_proto_get_content(self._as_parameter_), False)

    def set_content(self, content_p):
        """
        
        """
        return lib.mlm_proto_set_content(self._as_parameter_, byref(czmq.zmsg_p.from_param(content_p)))

    def sender(self):
        """
        Get the sender field
        """
        return lib.mlm_proto_sender(self._as_parameter_)

    def set_sender(self, sender):
        """
        Set the sender field
        """
        return lib.mlm_proto_set_sender(self._as_parameter_, sender)

    def tracker(self):
        """
        Get the tracker field
        """
        return lib.mlm_proto_tracker(self._as_parameter_)

    def set_tracker(self, tracker):
        """
        Set the tracker field
        """
        return lib.mlm_proto_set_tracker(self._as_parameter_, tracker)

    def timeout(self):
        """
        Get the timeout field
        """
        return lib.mlm_proto_timeout(self._as_parameter_)

    def set_timeout(self, timeout):
        """
        Set the timeout field
        """
        return lib.mlm_proto_set_timeout(self._as_parameter_, timeout)

    def status_code(self):
        """
        Get the status_code field
        """
        return lib.mlm_proto_status_code(self._as_parameter_)

    def set_status_code(self, status_code):
        """
        Set the status_code field
        """
        return lib.mlm_proto_set_status_code(self._as_parameter_, status_code)

    def status_reason(self):
        """
        Get the status_reason field
        """
        return lib.mlm_proto_status_reason(self._as_parameter_)

    def set_status_reason(self, status_reason):
        """
        Set the status_reason field
        """
        return lib.mlm_proto_set_status_reason(self._as_parameter_, status_reason)

    def amount(self):
        """
        Get the amount field
        """
        return lib.mlm_proto_amount(self._as_parameter_)

    def set_amount(self, amount):
        """
        Set the amount field
        """
        return lib.mlm_proto_set_amount(self._as_parameter_, amount)

    @staticmethod
    def test(verbose):
        """
        Self test of this class.
        """
        return lib.mlm_proto_test(verbose)


# mlm_client
lib.mlm_client_new.restype = mlm_client_p
lib.mlm_client_new.argtypes = []
lib.mlm_client_destroy.restype = None
lib.mlm_client_destroy.argtypes = [POINTER(mlm_client_p)]
lib.mlm_client_actor.restype = czmq.zactor_p
lib.mlm_client_actor.argtypes = [mlm_client_p]
lib.mlm_client_msgpipe.restype = czmq.zsock_p
lib.mlm_client_msgpipe.argtypes = [mlm_client_p]
lib.mlm_client_connected.restype = c_bool
lib.mlm_client_connected.argtypes = [mlm_client_p]
lib.mlm_client_set_plain_auth.restype = c_int
lib.mlm_client_set_plain_auth.argtypes = [mlm_client_p, c_char_p, c_char_p]
lib.mlm_client_connect.restype = c_int
lib.mlm_client_connect.argtypes = [mlm_client_p, c_char_p, c_int, c_char_p]
lib.mlm_client_set_producer.restype = c_int
lib.mlm_client_set_producer.argtypes = [mlm_client_p, c_char_p]
lib.mlm_client_set_consumer.restype = c_int
lib.mlm_client_set_consumer.argtypes = [mlm_client_p, c_char_p, c_char_p]
lib.mlm_client_set_worker.restype = c_int
lib.mlm_client_set_worker.argtypes = [mlm_client_p, c_char_p, c_char_p]
lib.mlm_client_send.restype = c_int
lib.mlm_client_send.argtypes = [mlm_client_p, c_char_p, POINTER(czmq.zmsg_p)]
lib.mlm_client_sendto.restype = c_int
lib.mlm_client_sendto.argtypes = [mlm_client_p, c_char_p, c_char_p, c_char_p, c_int, POINTER(czmq.zmsg_p)]
lib.mlm_client_sendfor.restype = c_int
lib.mlm_client_sendfor.argtypes = [mlm_client_p, c_char_p, c_char_p, c_char_p, c_int, POINTER(czmq.zmsg_p)]
lib.mlm_client_recv.restype = czmq.zmsg_p
lib.mlm_client_recv.argtypes = [mlm_client_p]
lib.mlm_client_command.restype = c_char_p
lib.mlm_client_command.argtypes = [mlm_client_p]
lib.mlm_client_status.restype = c_int
lib.mlm_client_status.argtypes = [mlm_client_p]
lib.mlm_client_reason.restype = c_char_p
lib.mlm_client_reason.argtypes = [mlm_client_p]
lib.mlm_client_address.restype = c_char_p
lib.mlm_client_address.argtypes = [mlm_client_p]
lib.mlm_client_sender.restype = c_char_p
lib.mlm_client_sender.argtypes = [mlm_client_p]
lib.mlm_client_subject.restype = c_char_p
lib.mlm_client_subject.argtypes = [mlm_client_p]
lib.mlm_client_content.restype = czmq.zmsg_p
lib.mlm_client_content.argtypes = [mlm_client_p]
lib.mlm_client_tracker.restype = c_char_p
lib.mlm_client_tracker.argtypes = [mlm_client_p]
lib.mlm_client_sendx.restype = c_int
lib.mlm_client_sendx.argtypes = [mlm_client_p, c_char_p, c_char_p]
lib.mlm_client_sendtox.restype = c_int
lib.mlm_client_sendtox.argtypes = [mlm_client_p, c_char_p, c_char_p, c_char_p]
lib.mlm_client_sendforx.restype = c_int
lib.mlm_client_sendforx.argtypes = [mlm_client_p, c_char_p, c_char_p, c_char_p]
lib.mlm_client_recvx.restype = c_int
lib.mlm_client_recvx.argtypes = [mlm_client_p, POINTER(c_char_p), POINTER(c_char_p)]
lib.mlm_client_test.restype = None
lib.mlm_client_test.argtypes = [c_bool]

class MlmClient(object):
    """
    
    """

    allow_destruct = False
    def __init__(self, *args):
        """
        Create a new mlm_client, return the reference if successful, or NULL
if construction failed due to lack of available memory.
        """
        if len(args) == 2 and type(args[0]) is c_void_p and isinstance(args[1], bool):
            self._as_parameter_ = cast(args[0], mlm_client_p) # Conversion from raw type to binding
            self.allow_destruct = args[1] # This is a 'fresh' value, owned by us
        elif len(args) == 2 and type(args[0]) is mlm_client_p and isinstance(args[1], bool):
            self._as_parameter_ = args[0] # Conversion from raw type to binding
            self.allow_destruct = args[1] # This is a 'fresh' value, owned by us
        else:
            assert(len(args) == 0)
            self._as_parameter_ = lib.mlm_client_new() # Creation of new raw type
            self.allow_destruct = True

    def __del__(self):
        """
        Destroy the mlm_client and free all memory used by the object.
        """
        if self.allow_destruct:
            lib.mlm_client_destroy(byref(self._as_parameter_))

    def __bool__(self):
        "Determine whether the object is valid by converting to boolean" # Python 3
        return self._as_parameter_.__bool__()

    def __nonzero__(self):
        "Determine whether the object is valid by converting to boolean" # Python 2
        return self._as_parameter_.__nonzero__()

    def actor(self):
        """
        Return actor, when caller wants to work with multiple actors and/or
input sockets asynchronously.
        """
        return czmq.Zactor(lib.mlm_client_actor(self._as_parameter_), False)

    def msgpipe(self):
        """
        Return message pipe for asynchronous message I/O. In the high-volume case,
we send methods and get replies to the actor, in a synchronous manner, and
we send/recv high volume message data to a second pipe, the msgpipe. In
the low-volume case we can do everything over the actor pipe, if traffic
is never ambiguous.
        """
        return czmq.Zsock(lib.mlm_client_msgpipe(self._as_parameter_), False)

    def connected(self):
        """
        Return true if client is currently connected, else false. Note that the
client will automatically re-connect if the server dies and restarts after
a successful first connection.
        """
        return lib.mlm_client_connected(self._as_parameter_)

    def set_plain_auth(self, username, password):
        """
        Set PLAIN authentication username and password. If you do not call this, the
client will use NULL authentication. TODO: add "set curve auth".
Returns >= 0 if successful, -1 if interrupted.
        """
        return lib.mlm_client_set_plain_auth(self._as_parameter_, username, password)

    def connect(self, endpoint, timeout, address):
        """
        Connect to server endpoint, with specified timeout in msecs (zero means wait
forever). Constructor succeeds if connection is successful. The caller may
specify its address.
Returns >= 0 if successful, -1 if interrupted.
        """
        return lib.mlm_client_connect(self._as_parameter_, endpoint, timeout, address)

    def set_producer(self, stream):
        """
        Prepare to publish to a specified stream. After this, all messages are sent to
this stream exclusively.
Returns >= 0 if successful, -1 if interrupted.
        """
        return lib.mlm_client_set_producer(self._as_parameter_, stream)

    def set_consumer(self, stream, pattern):
        """
        Consume messages with matching subjects. The pattern is a regular expression
using the CZMQ zrex syntax. The most useful elements are: ^ and $ to match the
start and end, . to match any character, \s and \S to match whitespace and
non-whitespace, \d and \D to match a digit and non-digit, \a and \A to match
alphabetic and non-alphabetic, \w and \W to match alphanumeric and
non-alphanumeric, + for one or more repetitions, * for zero or more repetitions,
and ( ) to create groups. Returns 0 if subscription was successful, else -1.
Returns >= 0 if successful, -1 if interrupted.
        """
        return lib.mlm_client_set_consumer(self._as_parameter_, stream, pattern)

    def set_worker(self, address, pattern):
        """
        Offer a particular named service, where the pattern matches request subjects
using the CZMQ zrex syntax.
Returns >= 0 if successful, -1 if interrupted.
        """
        return lib.mlm_client_set_worker(self._as_parameter_, address, pattern)

    def send(self, subject, content_p):
        """
        Send STREAM SEND message to server, takes ownership of message
and destroys message when done sending it.
        """
        return lib.mlm_client_send(self._as_parameter_, subject, byref(czmq.zmsg_p.from_param(content_p)))

    def sendto(self, address, subject, tracker, timeout, content_p):
        """
        Send MAILBOX SEND message to server, takes ownership of message
and destroys message when done sending it.
        """
        return lib.mlm_client_sendto(self._as_parameter_, address, subject, tracker, timeout, byref(czmq.zmsg_p.from_param(content_p)))

    def sendfor(self, address, subject, tracker, timeout, content_p):
        """
        Send SERVICE SEND message to server, takes ownership of message
and destroys message when done sending it.
        """
        return lib.mlm_client_sendfor(self._as_parameter_, address, subject, tracker, timeout, byref(czmq.zmsg_p.from_param(content_p)))

    def recv(self):
        """
        Receive message from server; caller destroys message when done
        """
        return czmq.Zmsg(lib.mlm_client_recv(self._as_parameter_), False)

    def command(self):
        """
        Return last received command. Can be one of these values:
    "STREAM DELIVER"
    "MAILBOX DELIVER"
    "SERVICE DELIVER"
        """
        return lib.mlm_client_command(self._as_parameter_)

    def status(self):
        """
        Return last received status
        """
        return lib.mlm_client_status(self._as_parameter_)

    def reason(self):
        """
        Return last received reason
        """
        return lib.mlm_client_reason(self._as_parameter_)

    def address(self):
        """
        Return last received address
        """
        return lib.mlm_client_address(self._as_parameter_)

    def sender(self):
        """
        Return last received sender
        """
        return lib.mlm_client_sender(self._as_parameter_)

    def subject(self):
        """
        Return last received subject
        """
        return lib.mlm_client_subject(self._as_parameter_)

    def content(self):
        """
        Return last received content
        """
        return czmq.Zmsg(lib.mlm_client_content(self._as_parameter_), False)

    def tracker(self):
        """
        Return last received tracker
        """
        return lib.mlm_client_tracker(self._as_parameter_)

    def sendx(self, subject, content, *args):
        """
        Send multipart string message to stream, end list with NULL
Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return lib.mlm_client_sendx(self._as_parameter_, subject, content, *args)

    def sendtox(self, address, subject, content, *args):
        """
        Send multipart string to mailbox, end list with NULL
Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return lib.mlm_client_sendtox(self._as_parameter_, address, subject, content, *args)

    def sendforx(self, address, subject, content, *args):
        """
        Send multipart string to service, end list with NULL
Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return lib.mlm_client_sendforx(self._as_parameter_, address, subject, content, *args)

    def recvx(self, subject_p, string_p, *args):
        """
        Receive a subject and string content from the server. The content may be
1 or more string frames. This method is orthogonal to the sendx methods.
End the string arguments with NULL. If there are not enough frames in
the received message, remaining strings are set to NULL. Returns number
of string contents received, or -1 in case of error. Free the returned
subject and content strings when finished with them. To get the type of
the command, use mlm_client_command ().
        """
        return lib.mlm_client_recvx(self._as_parameter_, byref(c_char_p.from_param(subject_p)), byref(c_char_p.from_param(string_p)), *args)

    @staticmethod
    def test(verbose):
        """
        Self test of this class.
        """
        return lib.mlm_client_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################
if __name__ == "__main__":
    c = MlmClient()
    print("1")
    #c.verbose()
    print('2')
    c.connect("tcp://192.168.1.223:9999", 1000, "PythonTest")
    print("3")
    c.set_consumer("stream", ".+")
    print(c.connected())
    #import time
    msg = c.recv().popstr()
    while (msg == "hello"):
        print(msg)
        msg = c.recv().popstr()
    #print(msg.popstr())
    MlmClient.test(False)

