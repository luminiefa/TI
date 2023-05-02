from log import Log

CONTENU = "Oct 25 02:34:27 kali systemd[1]: logrotate.service: Succeeded."
SOURCE = "/fichier.log"
log = Log(CONTENU, SOURCE)


def test_init():
    assert log.text == CONTENU
    assert log.source == SOURCE
    assert isinstance(log, Log), "Log devrait être une classe"


def test_string():
    assert log.text == log.__str__()


def test_get_program():
    assert log.get_program() == "systemd"
