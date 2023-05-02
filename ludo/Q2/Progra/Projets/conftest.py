"""
Ensemble des fixtures communs à la session de test
"""
import os

import pytest

CONTENU_LOG = """Oct 25 02:34:27 kali systemd[1]: logrotate.service: Succeeded.
Oct 25 02:34:27 kali systemd[1]: Finished Rotate log files.
Oct 25 02:34:28 kali systemd[1]: man-db.service: Succeeded.
Oct 25 02:34:28 kali systemd[1]: Finished Daily man-db regeneration.
Oct 25 02:34:29 kali systemd[1]: Startup finished in 4.123s (kernel) + 29.624s (userspace) = 33.747s.
Oct 25 02:34:29 kali lightdm[701]: Error getting user list from org.freedesktop.Accounts: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.Accounts was not provided by any .service files"""


@pytest.fixture(scope="session")
def folder_structure(tmp_path_factory):
    """
    Création de la structure des dossiers et fichiers dans un dossier temporaire
    propre au système d'exploitation
    Structure de test:
        dossier/
        ├─ sous_dossier1/
        │  ├─ syslog.log
        ├─ sous_dossier2/
        │  ├─ syslog.log
    :param tmp_path_factory:
    :return: objet Path
    """
    try:
        path = tmp_path_factory.mktemp("dossier", False)
        os.mkdir(path.joinpath('sous_dossier1'))
        with open(path.joinpath('sous_dossier1/syslog.log'), "w") as file:
            file.write(CONTENU_LOG)
        os.mkdir(path.joinpath('sous_dossier2'))
        with open(path.joinpath('sous_dossier2/syslog.log'), "w") as file:
            file.write(CONTENU_LOG)
        return path
    except FileExistsError:
        return tmp_path_factory.getbasetemp().joinpath("dossier")
