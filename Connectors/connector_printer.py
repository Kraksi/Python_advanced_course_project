import serial
import time


class Printer:
    def __init__(self, port, baud_rate=115200, timeout=2):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.printer = None

    def connect(self):

        """Подключение к принтеру через USB"""

        try:
            # Создание объекта для последовательного соединения
            self.printer = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            print(f"Подключение к принтеру на {self.port} со скоростью {self.baud_rate} успешно!")
        except serial.SerialException as e:
            print(f"Ошибка подключения: {e}")

    def send_command(self, command):

        """Отправка одной команды на принтер."""

        if self.printer is None:
            print("Принтер не подключен!")
            return

        try:
            # Отправка команды
            print(f"Отправка команды: {command}")
            self.printer.write(command.encode('utf-8'))
            time.sleep(1)

            # Чтение ответа от принтера
            while self.printer.in_waiting > 0:
                response = self.printer.readline().decode('utf-8').strip()
                print(f"Ответ от принтера: {response}")

        except Exception as e:
            print(f"Ошибка при отправке команды: {e}")

    def close(self):

        """Закрытие соединения с принтером."""

        if self.printer:
            self.printer.close()
            print("Соединение с принтером закрыто.")
