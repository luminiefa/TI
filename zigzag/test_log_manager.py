import os

import pytest

from log import Log
from log_manager import LogManager
from program_not_found import ProgramNotFound
from main import load_log_from_file, load

CONTENU_STR = """systemd:
=======
Oct 25 02:34:27 kali systemd[1]: logrotate.service: Succeeded.
Oct 25 02:34:27 kali systemd[1]: Finished Rotate log files.
Oct 25 02:34:28 kali systemd[1]: man-db.service: Succeeded.
Oct 25 02:34:28 kali systemd[1]: Finished Daily man-db regeneration.
Oct 25 02:34:29 kali systemd[1]: Startup finished in 4.123s (kernel) + 29.624s (userspace) = 33.747s.
lightdm:
=======
Oct 25 02:34:29 kali lightdm[701]: Error getting user list from org.freedesktop.Accounts: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.Accounts was not provided by any .service files
TOTAL LOGS: 6
"""


def test_init_without_params(folder_structure):
    log_manager = LogManager()
    assert log_manager.logs == {}


def test_init_with_logs(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    assert isinstance(log_manager.logs, dict), "l'attribut log devrait être un dictionnaire"
    assert len(list(log_manager.logs.keys())) == 2


def test_clear_logs(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    log_manager.clear()
    assert log_manager.logs == {}


def test_add_logs(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    log_manager.add_logs(load_log_from_file(folder_structure.joinpath('sous_dossier2/syslog.log')))
    assert log_manager.nbr_logs == 12


def test_search_logs(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    logs = log_manager.search_logs("systemd")
    assert isinstance(logs, list), "La fonction devrait renvoyer une liste"
    for log in logs:
        assert isinstance(log, Log), "La liste devrait contenir des instance de Log"
    assert len(logs) == 5


def test_search_logs_with_exception(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    with pytest.raises(ProgramNotFound):
        log_manager.search_logs("ProgramNotExists")


def test_nbr_logs(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    assert log_manager.nbr_logs == 6


def test_str(folder_structure):
    log_manager = LogManager(load_log_from_file(folder_structure.joinpath('sous_dossier1/syslog.log')))
    assert str(log_manager).splitlines() == CONTENU_STR.splitlines()
