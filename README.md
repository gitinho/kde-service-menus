# kde-service-menus
My custom KDE service menus for audio analysis and organization

### Dependencies
* `python3`
* `ffmpeg`
* `lac`
* `sox`

Python modules:
* `mutagen`
* `discogs_client`
* `Levenshtein`

### Installation
The .desktop files go to `~/.local/share/kservices5/ServiceMenus/` for local user, or `/usr/share/kservices5/ServiceMenus/` for global

The scripts go to /usr/bin/, or somewhere else in the path environmental variable

Get a Discogs API personal token [here](https://www.discogs.com/settings/developers) and add it to the `autotaggenres` and `openindiscogs` scripts (The token included is outdated)
