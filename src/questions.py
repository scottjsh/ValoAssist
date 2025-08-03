# -*- coding: utf-8 -*-
from InquirerPy.base.control import Choice
from src.constants import DEFAULT_CONFIG, WEAPONS

TABLE_OPTS = {
    "skin": "Skin",
    "rr": "Ranked Rating",
    "earned_rr": "RR gained or lost (and AFK Penalties)",
    "leaderboard": "Leaderboard Position",
    "peakrank": "Peak Rank",
    "previousrank": "Previous Act Rank",
    "headshot_percent": "Headshot Percentage",
    "winrate": "WinRate",
    "kd": "K/D Ratio <!> Last Game Only <!>",
    "level": "Account Level"
}

FLAGS_OPTS = {
    "last_played": "Last Played Stats",
    "auto_hide_leaderboard": "Auto Hide Leaderboard Column",
    "pre_cls": "Pre-Clear Screen",
    "game_chat": "Print Game Chat",
    "peak_rank_act": "Peak Rank Act",
    "discord_rpc": "Discord Rich Presence",
    "aggregate_rank_rr": "Display Rank and Ranked Rating in the same column",
    "server_id": "Show Server ID"
}


def weapon_question(config): return {
    "type": "fuzzy",
    "name": "weapon",
    "message": "Please select a weapon to show skin for:",
    "default": config.get("weapon", "Vandal"),
    "choices": WEAPONS,
}


def table_question(config): return {
    "type": "checkbox",
    "name": "table",
    "message": "Please select table columns to display:",
    "choices": [
            Choice(k, name=v, enabled=config.get(
                "table", DEFAULT_CONFIG["table"]).get(k, DEFAULT_CONFIG["table"][k]))
            for k, v in TABLE_OPTS.items()
    ],
    "filter": lambda table: {k: k in table for k in TABLE_OPTS.keys()},
    "long_instruction": "Press 'space' to toggle selection and 'enter' to submit"
}


def port_question(config): return {
    "type": "number",
    "name": "port",
    "message": "Please enter port for server to run:",
    "default": config.get("port", 1100),
    "min_allowed": 0,
    "max_allowed": 65535,
    "filter": lambda ans: int(ans)
}


def flags_question(config): return {
    "type": "checkbox",
    "name": "flags",
    "message": "Please select optional features:",
    "choices": [
            Choice(k, name=v, enabled=config.get(
                "flags", DEFAULT_CONFIG["flags"]).get(k, DEFAULT_CONFIG["flags"][k]))
            for k, v in FLAGS_OPTS.items()
    ],
    "filter": lambda flags: {k: k in flags for k in FLAGS_OPTS.keys()},
    "long_instruction": "Press 'space' to toggle selection and 'enter' to submit"
}


def chat_limit_question(config): return {
    "type": "number",
    "name": "chat_limit",
    "message": "Please enter the length of the chat messages history:",
    "default": config.get("chat_limit", 5),
    "min_allowed": 0,
    "max_allowed": 100,
    "filter": lambda ans: int(ans)
}


def basic_questions(config): return [
    weapon_question(config=config),
    table_question(config=config),
    chat_limit_question(config=config)
]


def advance_questions(config): return [
    port_question(config=config),
] + basic_questions(config=config)
