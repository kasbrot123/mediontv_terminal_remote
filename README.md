# Medion TV Terminal Remote

This is a simple bash script for controlling a Medion TV which is capable of receiving netcat commands via port `4660`.

Usage of the script:

```
medion power # turns on TV
medion 1 # press button 1
```

There is also an interactive mode where the tv can be controled with the keyboard by pressing keys. 

```
medion # turns on TV
<KEYPRESS M>
mute
```


## List of commands

- `0`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `menue`
- `mute`
- `up`
- `left`
- `ok`
- `right`
- `down`
- `volup`
- `voldown`
- `vol <number>` (set volume level to number)
- `power`
- `return`
- `info`
- `exit`
- `source`
- `epg`
- `pup` (page up)
- `pdown` (page down)
- `program` (returns the current program info)
- `volume` (returns the current volume level)
- `activechannellist` (active channel list)
- `green`
- `yellow`
- `red`
- `blue`
- `play`
- `stop`
- `pause`
- `<NO FLAG>` (interactive mode)


## Interactive Mode Commands

*See script for detailed information..*



