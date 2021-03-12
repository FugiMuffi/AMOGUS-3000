# A.M.O.G.U.S 3000

**A**mongUs **M**ute **O**mnipotent **G**amer **U**ltra **S**entinel 3000
allows you to mute everyone in a Discord voice channel using a hotkey, e.g. when your friends can't shut up while playing.

### Prerequisites

* Python 3.6 or higher

### Installation

```
$ pip3 install -r requirements.txt
```

### Usage

Set your bot token, channel id and keybind in discordbot<span></span>.py
```
$ python3 discordbot.py
```
Now you can press your keybind to mute/unmute everyone in the channel. Users will only be muted in that channel. (Known issue: if someone disconnects while muted, its not possible to unmute them until they connect to a voice channel again.)
