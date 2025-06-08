import time
import psutil
import platform
import subprocess
from PySide6 import QtWidgets, QtGui, QtCore
from ui.monitor_form import Ui_Form

class SystemMonitorThread(QtCore.QThread):
    update_system_info = QtCore.Signal(str)
    update_processes = QtCore.Signal(list)
    update_services = QtCore.Signal(list)
    update_scheduler_tasks = QtCore.Signal(tuple)

    def __init__(self):
        super().__init__()
        self.delay = None

    def run(self):
        if self.delay is None:
            self.delay = 1

        while True:
            system_info = self.get_system_info()
            self.update_system_info.emit(system_info)

            processes = self.get_processes()
            self.update_processes.emit(processes)

            services = self.get_services()
            self.update_services.emit(services)

            tasks_info = self.get_task()
            self.update_scheduler_tasks.emit(tasks_info)

            time.sleep(self.delay)


    def get_system_info(self):
        cpu_info = f"Процессор: {self.get_cpu_model()}\n"
        cpu_info += f"Ядра: {psutil.cpu_count(logical=False)} физических, {psutil.cpu_count(logical=True)} логических\n"
        cpu_info += f"Текущая загрузка: {psutil.cpu_percent()}%\n\n"


        mem = psutil.virtual_memory()
        mem_info = f"Оперативная память: {self.format_size(mem.total)}\n"
        mem_info += f"Используется: {self.format_size(mem.used)} ({mem.percent}%)\n\n"

        disks_info = ""
        disks_info += f"Количество дисков {psutil.disk_partitions().__len__()}\n"
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disks_info += f"Диск {partition.mountpoint}\n"
                disks_info += f"Общий объем: {self.format_size(usage.total)}\n"
                disks_info += f"Использовано: {self.format_size(usage.used)} ({usage.percent}%)\n\n"
            except:
                continue
        return cpu_info + mem_info + disks_info

    def get_cpu_model(self):
        try:
            if platform.system() == "Windows":
                cmd = 'wmic cpu get name'
                output = subprocess.check_output(cmd, shell=True).decode().strip()
                return output.split('\n')[1] if '\n' in output else "Unknown"
        except:
            return "Unknown"

    def get_processes(self):
        processes = []
        for proc in psutil.process_iter(['name', 'status', 'cpu_percent', 'memory_percent']):
            try:
                processes.append([
                    proc.info['name'],
                    proc.info['status'],
                    f"{proc.info['cpu_percent']:.1f}",
                    f"{proc.info['memory_percent']:.1f}",
                ])
            except:
                continue
        return processes

    def get_services(self):
        services = []
        for service in psutil.win_service_iter():
            try:
                info = service.as_dict()
                services.append([
                    info['name'],
                    str(info['pid']),
                    info['description'],
                    info['status'],
                ])
            except:
                continue
        return services

    def get_task(self):
        try:
            result = subprocess.check_output(
                'schtasks /query /fo LIST /v',
                shell=True,
                text=True,
                encoding='cp866'
            )

            tasks = []
            current = {}
            for line in result.splitlines():
                if ':' in line:
                    key, val = line.split(':', 1)
                    current[key.strip()] = val.strip()
                elif not line.strip():
                    if current:
                        tasks.append(current)
                        current = {}

            return tasks
        except Exception as e:
            print(f"Ошибка: {e}")
            return []


    def format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.monitor_thread = SystemMonitorThread()
        self.monitor_thread.update_system_info.connect(self.update_system_info_display)
        self.monitor_thread.update_processes.connect(self.update_processes_display)
        self.monitor_thread.update_services.connect(self.update_services_display)
        self.monitor_thread.update_scheduler_tasks.connect(self.update_scheduler_display)
        self.monitor_thread.start()
        self.ui.comboBox.currentIndexChanged.connect(self.change_update_interval)

    def change_update_interval(self):
        self.monitor_thread.delay = int(self.ui.comboBox.currentText())

    def update_system_info_display(self, info):
        self.ui.plainTextEdit_info.setPlainText(info)

    def update_processes_display(self, processes):
        self.ui.tableWidget_processes.setRowCount(len(processes))
        for row, process in enumerate(processes):
            for col, data in enumerate(process):
                item = QtWidgets.QTableWidgetItem(data)
                self.ui.tableWidget_processes.setItem(row, col, item)

    def update_services_display(self, services):
        self.ui.tableWidget_services.setRowCount(len(services))
        for row, service in enumerate(services):
            for col, data in enumerate(service):
                item = QtWidgets.QTableWidgetItem(data)
                self.ui.tableWidget_services.setItem(row, col, item)

    def update_scheduler_display(self, info):
        self.ui.tableWidget_task.setRowCount(len(info))
        for row, task in enumerate(info):
            value = task.get('Имя задачи')
            item = QtWidgets.QTableWidgetItem(value)
            self.ui.tableWidget_task.setItem(row, 0, item)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
