from Connectors.connector_printer import Printer

if __name__ == "__app__":
    # Подключение к принтеру
    printer = Printer(port="COM3")
    printer.connect()
    printer.close()
