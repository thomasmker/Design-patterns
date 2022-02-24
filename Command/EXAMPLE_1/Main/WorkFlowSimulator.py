from Command.EXAMPLE_1.Models.CustomRequest import CustomRequest
from Command.EXAMPLE_1.Models.WorkFlow import WorkFlow
from Command.EXAMPLE_1.Models.RequestCommands import RequestConclusion, RequestPayment


def main():
    request1 = CustomRequest('John Doe', 100)
    request2 = CustomRequest('Maria Doe', 150)

    print("--- Before ---")
    print(request1)
    print(request2)

    work_flow = WorkFlow()
    work_flow.add(RequestPayment(request1))
    work_flow.add(RequestPayment(request2))
    work_flow.add(RequestConclusion(request1))

    work_flow.process()

    print("--- After ---")
    print(request1)
    print(request2)


if __name__ == '__main__':
    main()
