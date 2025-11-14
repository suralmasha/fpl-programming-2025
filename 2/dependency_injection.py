from typing import overload


class Service:
    def get_data(self):
        return "data"


# class Controller:
#     def __init__(self):
#         self.service = Service()
#
#     def handle(self):
#         return self.service.get_data()

class Controller:
    def __init__(self, service):
        self.service = service

    def handle(self):
        return self.service.get_data()

    @overload
    def reform_data(self, val: str) -> int:
        pass

    @overload
    def reform_data(self, val: int) -> str:
        pass

    def reform_data(self, val: str | int) -> int | str:
        if isinstance(val, int):
            return str(val)
        if isinstance(val, str):
            return int(val)


if __name__ == "__main__":
    service_obj = Service()
    controller = Controller(service_obj)

    x = controller.reform_data(1)
