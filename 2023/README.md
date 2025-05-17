# 2023 PACE NSC Streaming Util
This is a utility designed to help run the livestream of gameplay for the 2023 PACE NSC, as well as future streams of Quizbowl tournaments.
It is meant to be used alongside the OBS Studio software, with the use of a few additional plugins.

## Dependencies
This project utilizes HTML-GL, HTML, and TypeScript. It is currently in version 0.0.1, and I plan to extend its functionality
for future uses.

## Installation
First, install [OBS Studio]. Then, clone this project to an easily-accessible location. After that, you're good to go!

## Use
To use this project effectively, first import the scene collection into obs. One
can do this by navigating to "Scene Collection > Import" and linking the .json file under ./obs/PACENSC.json. From here, you'll have to composite in the camera
and microphone feeds into their corresponding scenes. You'll also need to start 
a browser capture on MODAQ or Google Sheets (the latter for Finals) to keep 
track of the score.

Overlaying the lower thirds layout allows for the audience to see the team and 
player names. One can alternatively use the dockable lower-thirds plugin authored 
by [author name here].

[WIP 06/11/2023: linking player names to html via .js script and team colors to
gradients]

## Features
A few key parts of the software:

* Shaders that incorporate team / school colors
* Indicators for buzzes and point values on tossups and bonuses
* Showing which team controls a given bonus or bounceback
* Custom shaders for waiting screens between games and for added flair during gameplay
* Integration with MODAQ to show dynamic score updates

## Feedback
Suggestions are welcome and highly appreciated! Please send them to S. A. Shenoy (sshenoy [at] pace-nsc [dot] org).

Best of luck to all teams at this year's NSC~