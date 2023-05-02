from io import StringIO

from main import menu, load_log_from_file, load_logs_from_folder, get_folders_and_subfolders, load, main

choix = {
    1: "Logs d'un program",
    2: "Charger les logs",
    9: "Terminer le programme"
}


def test_menu_with_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1'))
    number = menu(choix)
    assert number == 1


def test_menu_with_retry(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('abc\n1'))
    number = menu(choix)
    assert number == 1


def test_load_log_from_file_not_found(capsys):
    load_log_from_file("/notexist.log")
    captured = capsys.readouterr()
    assert "Le chemin du fichier n'existe pas" in captured.out, \
        "La fonction devrait afficher un message pour avertir que le fichier n'existe pas"


def test_load_log_from_file(folder_structure):
    logs = load_log_from_file(str(folder_structure.joinpath('sous_dossier1/syslog.log')))
    assert isinstance(logs, list), "La fonction devrait renvoyer une liste"
    for log in logs:
        assert isinstance(log, str), "La liste devrait être composée d'instances de String"
    assert len(logs) == 6


def test_load_logs_from_folder_not_found(capsys):
    load_logs_from_folder('./foldernotexist')
    captured = capsys.readouterr()
    assert "Le chemin du dossier n'existe pas" in captured.out, \
        "La fonction devrait afficher un message pour avertir que le dossier n'existe pas"


def test_load_logs_from_folder(folder_structure):
    logs = load_logs_from_folder(str(folder_structure.joinpath('sous_dossier1')))
    assert isinstance(logs, list), "La fonction devrait renvoyer une liste"
    for log in logs:
        assert isinstance(log, str), "La liste devrait être composée d'instances de String"
    assert len(logs) == 6


def test_get_folders_and_subfolders_not_found(capsys):
    load_logs_from_folder('./foldernotexist')
    captured = capsys.readouterr()
    assert "Le chemin du dossier n'existe pas" in captured.out, \
        "La fonction devrait afficher un message pour avertir que le dossier n'existe pas"


def test_get_folders_and_subfolders(folder_structure):
    paths = get_folders_and_subfolders(str(folder_structure))
    assert isinstance(paths, list), "La fonction devrait renvoyer une liste"
    for path in paths:
        assert isinstance(path, str), "La liste devrait être composée d'instances de String"
    assert len(paths) == 3


def test_load(folder_structure):
    logs = load(str(folder_structure))
    assert isinstance(logs, list), "La fonction devrait renvoyer une liste"
    for log in logs:
        assert isinstance(log, str), "La liste devrait être composée d'instances de String"
    assert len(logs) == 12
