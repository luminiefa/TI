import os
from log import Log
from program_not_found import ProgramNotFound
from datetime import datetime

class LogManager:
    @staticmethod
    def sort_by_program(logs):
        sorted_logs = {}
        for log in logs:
            program = log.get_program()
            if program not in sorted_logs:
                sorted_logs[program] = []
            sorted_logs[program].append(log)
        return sorted_logs

    def __init__(self, logs=None):
        if logs is None:
            logs = []
        self.logs = self.sort_by_program(logs)

    def clear(self):
        self.logs = {}

    def add_logs(self, logs):
        new_logs = self.sort_by_program(logs)
        for program, log_list in new_logs.items():
            if program not in self.logs:
                self.logs[program] = []
            self.logs[program].extend(log_list)

    def search_logs(self, program_name):
        if program_name in self.logs:
            return self.logs[program_name]
        else:
            raise ProgramNotFound(program_name, list(self.logs.keys()))

    @property
    def nbr_logs(self):
        return sum([len(logs) for logs in self.logs.values()])

    def __str__(self):
        output = []
        for program, logs in self.logs.items():
            output.append(program + ":")
            output.append("=" * len(program))
            for log in logs:
                output.append(str(log))
        output.append("TOTAL LOGS: " + str(self.nbr_logs))
        return "\n".join(output)