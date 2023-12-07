# More Company!

This mod is a lobby player count expansion mod. It increases the max player count.

The mod is specifically designed for 8 players. Not every UI modification will properly accomodate for above 8 players.

# Release Trailer
[![IMAGE ALT TEXT](http://img.youtube.com/vi/yHxU4YrA8Ag/0.jpg)](http://www.youtube.com/watch?v=yHxU4YrA8Ag "More Company Launch Trailer")

# Why this mod? Isn't there another mod that does the same thing?
Yes, although there is another mod that does a very similar thing, it has a few stability issues regarding the functionality of the game. In the development of MoreCompany, I had stability and polish in mind, I wanted to make a relatively frictionless experience regarding expanded player counts.

In my testing of an 8 player lobby, I experienced no issues nor did anyone else in the lobby. Alot of game conditions were tested, but there may be conditions which were not tested that may be broken or cause a softlock. If you experience issues like these, please let me know at the Discord server linked at the bottom of this page.

This mod is not affiliated with BiggerLobby/LethalPlayers nor does it use any code from that mod! Any similarities are purely coincidental.

# ``Installation``
```
- Install BepinEx.
- Place BepInEx/plugins/MoreCompany.dll in your BepInEx/plugins folder.
- Make sure everyone joining you has this mod installed.
```

# Features
- Cosmetics

# Minor Features
- The scavenge results screen has been modified to fit 8 players and will show their missing/deceased/alive states accordingly.
- The spectating screen properly fits greater than 4 players if they die. (They will not go offscreen)
- The quickmenu player volume section accounts for greater than 4 players, with a scrollable UI.

# Cosmetics Demonstration
![](https://cdn.discordapp.com/attachments/1121903172189962272/1177369023822970950/ezgif.com-video-to-gif.gif?ex=65724159&is=655fcc59&hm=92ccdc457dbba7b97f2e84169b3826064a7d1be6544846abe05f7531180bab47&)

# Changelog
## 1.6.0
- Fixed rare Coilhead targetting issue on extra players.
- Added 2 new cosmetics.
- Fixed jiggly cosmetics on players.
- Added new chest cosmetic anchor point.

## 1.5.1
- Fixed ship stall issue if the playercount was set to 8 or below.

## 1.5.0
- Added 7 new cosmetics.
- Removed 1 cosmetic.
- Added option to disable cosmetics displaying on other players.
- Fixed minor performance hit when in a lobby with a large player count while the player slots are not taken up.
- Upped max player cap to 50. (Default value is 32)
- Reverted LC_API serverlist display. Base MoreCompany players will only see other MoreCompany lobbies if they do not have LC_API installed.
- Added player count selector to hosting box.
- Fixed widescreen players not being able to see the cosmetic button on the main menu.

## 1.4.2
- Fixed death screen rendering above the results screen.

## 1.4.1
- Fixed voice slider range going too quiet too quickly.

## 1.4.0
- Added cosmetic system to MoreCompany. Currently features 12 cosmetics at the time of writing.
- Expanded UI on quickmenu to be scrollable. All players have individual volume sliders. Including kick buttons.

## 1.3.0
- Patched furniture getting desynced between clients if objects were moved prior to joining.
- Fixed suit on rack sometimes appearing far from the ship for clients other than the host.

## 1.2.1
- Caught minor mistake in LC_API compatibility. Patched in this version.

## 1.2.0
- Fixed cross compatibility with LC_API users and non LC_API users not being able to join one anothers lobbies.
- Patched out warn that occured every frame.

## 1.1.1
- The mod now targets BepInEx instead of MelonLoader.

## 1.1.0
- Increased player cap to 32 users.
- Modified version text in bottom left corner to display (MC) next to it on the menu.
- Prevented MoreCompany servers from showing up on public lobby displays. Only other MoreCompany users can see MoreCompany public lobbies.

# Upcoming (Potentially)
- More cosmetics.

# [Discord Server](https://discord.gg/cKa6sPBFZ9)

## ```Contributors```
- Krystilize

## ```Cosmetic Contributors```
- Unun
- Taxi.man981
- DrakeFruit
- thisisquitter
- jelly
- SoulWithMae
- Runnerdude127
