import zmq
import msgpack

def get_user_input():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão de ponto flutuante")
    print("5. Divisão de inteiros")
    print("6. Raiz quadrada")
    operation = input("Digite o número da operação: ")

    if operation in ['1', '2', '3', '4', '5']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return operation, num1, num2
    elif operation == '6':
        num = float(input("Digite o número: "))
        return operation, num
    else:
        print("Operação inválida")
        return None

ctx = zmq.Context()
client = ctx.socket(zmq.REQ)
client.connect("tcp://localhost:5555")

while True:
    user_input = get_user_input()
    if user_input:
        operation, *numbers = user_input
        msg = {"operation": operation, "numbers": numbers}
        msg_p = msgpack.packb(msg)
        client.send(msg_p)

        reply_p = client.recv()
        reply = msgpack.unpackb(reply_p)
        print(f"Received reply: {reply}")

client.close()
ctx.close()