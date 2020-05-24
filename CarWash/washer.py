class Washer:
    def __init__(self, washing_strategy):
        self.__washing_strategy = washing_strategy

    def __call__(self):
        self.__washing_strategy.wash()
