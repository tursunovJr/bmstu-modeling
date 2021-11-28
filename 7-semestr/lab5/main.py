from system.distribution import RandomGenerator
from system.generator import GenerateRequest
from system.processor import ProcessRequest
from system.modeller import Model


def main():

    clients_number = int(input("Input number of clients: "))

    for i in range(10):
        time_clients = 10
        delta_time_clients = 2

        first_operator = 20
        second_operator = 40
        third_operator = 40

        first_computer = 15
        second_computer = 30

        delta_first_operators = 5
        delta_second_operators = 10
        delta_third_operators = 20

        
        generator = GenerateRequest(
            RandomGenerator(time_clients, delta_time_clients),
            clients_number,
        )

        operators = [
            ProcessRequest(
                RandomGenerator(first_operator, delta_first_operators),
                max_queue_size=1,
            ),
            ProcessRequest(
                RandomGenerator(second_operator, delta_second_operators),
                max_queue_size=1,
            ),
            ProcessRequest(
                RandomGenerator(third_operator, delta_third_operators),
                max_queue_size=1,
            ),
        ]

        computers = [
            ProcessRequest(RandomGenerator(first_computer)),
            ProcessRequest(RandomGenerator(second_computer)),
        ]

        model = Model(generator, operators, computers)
        result = model.event_mode()

    print("Процент отказа: [{0}]"
          .format(result['refusal_percentage']))
    print("Кол-во отклонённых клиентов: [{0}]"
          .format(result['refusals']))


if __name__ == "__main__":
    main()