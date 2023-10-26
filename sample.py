import mlogs

# logging.basicConfig(
#    filename="test1.log", 
#    level=logging.INFO,
#    format="%(asctime)s:%(levelname)s:%(message)s"
#    Añadimos línea de texto en el comentario MAIN
#    )
logger = mlogs.get_logger("experimental")

class porra():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.info("porra creada: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logger.warning("Haz {} porra(s) {}".format(quantity, self.name))

    def eat(self, quantity=1):
        logger.critical("come {} porra(s) {} ".format(quantity, self.name))

porra_01 = porra("Sencillo", 15)
porra_01.make(5)
porra_01.eat(4)

porra_02 = porra("Relleno", 16)
porra_02.make(2)
porra_02.eat(2)
