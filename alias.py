
from commands import *

ALIASES = {
    "about": about.main,
    "analyze": analyze.main,
    "an": analyze.main,
    "await": debugawait.main,
    "badge": badge.main,
    "bio": bio.main,
    "board": board.main,
    "bd": board.main,
    "bug": bug.main,
    "buy": buy.main,
    "coinflip": coinflip.main,
    "cf": coinflip.main,
    "debug": debug.main,
    "db": debug.main,
    "disband": disband.main,
    "donate": donate.main,
    "draw": draw.main,
    "exit": exit.main,
    "fen": fen.main,
    "game": game.main,
    "games": games.main,
    "hasbeat": hasbeat.main,
    "help": help.main,
    "invite": invite.main,
    "inv": invite.main,
    "joke": joke.main,
    "kick": kick.main,
    "leaderboard": leaderboard.main,
    "lb": leaderboard.main,
    "leave": leave.main,
    "listserver": listserver.main,
    "move": move.main,
    "go": move.main,
    "m": move.main,
    "g": move.main,
    "newgame": newgame.main,
    "ng": newgame.main,
    "pay": pay.main,
    "pgn": pgn.main,
    "ping": ping.main,
    "prefix": prefix.main,
    "profile": profile.main,
    "pf": profile.main,
    "randserver": randserver.main,
    "recruit": recruit.main,
    "renameteam": renameteam.main,
    "report": report.main,
    "resign": resign.main,
    "restart": restart.main,
    "server": server.main,
    "setstatus": setstatus.main,
    "shop": shop.main,
    "store": shop.main,
    "suggestion": suggestion.main,
    "suggest": suggestion.main,
    "team": team.main,
    "tm": team.main,
    "teambio": teambio.main,
    "unlistserver": unlistserver.main,
    "vote": vote.main,
    "accept": None,
    "join": None,
    "decline": None,
    "mosthype": mosthype.main,
}
