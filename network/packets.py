"""
Contains all network packets.
"""
from enum import Enum
import msgpack


class Packet:
    def encode(self):
        """Encode the message using msgpack."""
        return msgpack.packb(self.__dict__, use_bin_type=True)


class ServerInfoRequest(Packet):
    class ServerInfoRequestType(Enum):
        PING = 0
        BASIC = 1
        FULL = 2

    id = 'ServerInfoRequest'

    def __init__(self, request_type: ServerInfoRequestType):
        self.type = request_type


class ServerInfoResponse(Packet):
    id = 'ServerInfoResponse'
    # TODO
    pass


class JoinRequest(Packet):
    id = 'JoinRequest'

    def __init__(self, player_name: str, auth_response: bytes = None):
        self.player_name = player_name
        self.auth_response = auth_response


class JoinResponse(Packet):
    class JoinResult(Enum):
        SUCCESS = 0
        SERVER_FULL = 1
        BAD_PASSWORD = 2

    id = 'JoinResponse'

    def __init__(self, result: JoinResult, msg: str):
        self.result = result
        self.msg = msg


class RoomListRequest(Packet):
    id = 'RoomListRequest'


class JoinRoomRequest(Packet):
    id = 'JoinRoomRequest'

    def __init__(self, player_name: str, auth_response: bytes = None):
        self.player_name = player_name
        self.auth_response = auth_response


class JoinRoomResponse(Packet):
    class JoinRoomResult(Enum):
        SUCCESS = 0
        ROOM_FULL = 1
        BAD_PASSWORD = 2

    id = 'JoinRoomResponse'

    def __init__(self, result: JoinRoomResult):
        self.result = result


class Chat(Packet):
    id = 'Chat'

    def __init__(self, player_id: int, emote: str, msg: str, timescale: float = 1, flip: bool = False):
        self.player_id = player_id
        self.emote = emote
        self.msg = msg
        self.timescale = timescale
        self.flip = flip


class ChatOOC(Packet):
    id = 'Chat_OOC'

    def __init__(self, player_id: int, msg: str):
        self.player_id = player_id
        self.msg = msg


class Join(Packet):
    id = 'Join'

    def __init__(self, player_id: int, player_name: str, char_id: str):
        self.player_id = player_id
        self.player_name = player_name
        self.char_id = char_id


class Leave(Packet):
    id = 'Leave'

    def __init__(self, player_id: int):
        self.player_id = player_id


class Disconnect(Packet):
    class DisconnectCause(Enum):
        UNSPECIFIED = 0
        DISCONNECT_BY_USER = 1
        KICKED = 2
        BANNED = 3

    id = 'Disconnect'

    def __init__(self, cause: DisconnectCause, player_id: int):
        self.cause = cause
        self.player_id = player_id


class SetBackground(Packet):
    class Transition:
        class TransitionType(Enum):
            NONE = 0
            FADE_TO_BLACK = 1
            CROSSFADE = 2
            FADE_TO_WHITE = 3

        def __init__(self, transition_type: TransitionType, time: float):
            self.type = transition_type
            self.time = time

    id = 'SetBackground'

    def __init__(self, name: str, transition: Transition = None):
        self.name = name
        self.transition = transition


class SoundPlay(Packet):
    id = 'SoundPlay'

    def __init__(self, name: str, channel: int, loop: bool = False):
        self.name = name
        self.channel = channel
        self.loop = loop


class SoundStop(Packet):
    id = 'SoundStop'

    def __init__(self, channel: int):
        self.channel = channel


class SoundVolume(Packet):
    id = 'SoundVolume'

    def __init__(self, channel: int, smooth: bool = False):
        self.channel = channel
        self.smooth = smooth