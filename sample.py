import mlogs

# logging.basicConfig(
#    filename="test.log", 
#    level=logging.INFO,
#    format="%(asctime)s:%(levelname)s:%(message)s"
#    )
logger = mlogs.get_logger("experimental")

class churro():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.info("Churro creado: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logger.warning("Haz {} churro(s) {}".format(quantity, self.name))

    def eat(self, quantity=1):
        logger.critical("come {} churro(s) {} ".format(quantity, self.name))

churro_01 = churro("Sencillo", 15)
churro_01.make(5)
churro_01.eat(4)

churro_02 = churro("Relleno", 16)
churro_02.make(2)
churro_02.eat(2)
