import zmq
import msgpack
import math

def perform_operation(operation, numbers):
    try:
        if operation == '1':
            result = sum(numbers)
        elif operation == '2':
            result = numbers[0] - numbers[1]
        elif operation == '3':
            result = numbers[0] * numbers[1]
        elif operation == '4':
            result = numbers[0] / numbers[1]
        elif operation == '5':
            quotient = numbers[0] // numbers[1]
            remainder = numbers[0] % numbers[1]
            result = (quotient, remainder)
        elif operation == '6':
            result = math.sqrt(numbers[0])
        else:
            return {"status": "error", "message": "Operação inválida"}
        return {"status": "ok", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

ctx = zmq.Context()
server = ctx.socket(zmq.REP)
server.bind("tcp://*:5555")

while True:
    msg_p = server.recv()
    msg = msgpack.unpackb(msg_p)
    operation = msg.get("operation")
    numbers = msg.get("numbers")
    response = perform_operation(operation, numbers)
    ans_p = msgpack.packb(response)
    server.send(ans_p)

server.close()
ctx.close()