import json
import os
from typing import Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "members.json")


def _ensure_data_dir() -> None:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)


def _load_data() -> list[dict]:
    _ensure_data_dir()
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def _save_data(members: list[dict]) -> None:
    _ensure_data_dir()
    with open(DATA_FILE, "w") as f:
        json.dump(members, f, indent=2)


def get_all() -> list[dict]:
    return _load_data()


def get_by_id(member_id: str) -> Optional[dict]:
    members = _load_data()
    for m in members:
        if m["id"] == member_id:
            return m
    return None


def create(member: dict) -> dict:
    members = _load_data()
    members.append(member)
    _save_data(members)
    return member


def update(member_id: str, updates: dict) -> Optional[dict]:
    members = _load_data()
    for i, m in enumerate(members):
        if m["id"] == member_id:
            members[i].update(updates)
            _save_data(members)
            return members[i]
    return None


def delete(member_id: str) -> bool:
    members = _load_data()
    new_members = [m for m in members if m["id"] != member_id]
    if len(new_members) == len(members):
        return False
    _save_data(new_members)
    return True
