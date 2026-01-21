# project.py
# Database module for Basic Banking System
# Uses JSON file for permanent storage

import json
import os

FILENAME = "bank_db.json"

# In-memory database structures
accs = []
accdetail = {}
acc_name = {}
acc_address = {}
acc_idproof = {}
acc_passwords = {}


def load_db():
    global accs, accdetail, acc_name, acc_address, acc_idproof, acc_passwords
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
            accs = data.get("accs", [])
            accdetail = {int(k): v for k, v in data.get(
                "accdetail", {}).items()}
            acc_name = {int(k): v for k, v in data.get("acc_name", {}).items()}
            acc_address = {int(k): v for k, v in data.get(
                "acc_address", {}).items()}
            acc_idproof = {int(k): tuple(v)
                           for k, v in data.get("acc_idproof", {}).items()}
            acc_passwords = {int(k): v for k, v in data.get(
                "acc_passwords", {}).items()}


def save_db():
    data = {
        "accs": accs,
        "accdetail": accdetail,
        "acc_name": acc_name,
        "acc_address": acc_address,
        "acc_idproof": acc_idproof,
        "acc_passwords": acc_passwords
    }
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
