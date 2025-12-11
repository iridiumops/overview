# YAML files

Instead of having one large unwieldy YAML file, Iridium Overview is split into individual parts, allowing to easily generate alternative versions with different sets of filters or tab settings variations.

During the build process, filter files get updated with data from SDE in form of comment labels, however all YAML comments are stripped from final YAML file.

## Filter Naming
Filters are grouped into categories based on intended use-case via common first character (symbol).

Brackets and Dscan filter names are prepended with a character (`/` and `?`) selected for its low ASCII numeric value in order to allow their selection via shortcuts in the Dscan window, which sorts filters lexically in ascending order.

Part in parenthesis denotes changes compared to base filter. Character `+` indicates that something was added while `-` indicates removal. Alternatively it describes what state is displayed on the filter.

States:
   - All - any standings, any special state
   - Red - negative standing i.e. -5 and -10
   - Neutral - neutral standing or no standings
   - Friendly - positive standings i.e. +5 and +10, fleet
   - War targets - valid target due to Concord sanctioned war
   - Hisec criminals - valid target due to suspect or criminal timer or low security status

## Filter list and description

### / Brackets: Combat
Standard bracket filter, controls what is visible in space.

### / Brackets: Combat (+drones)
Variation with drones and fighters. In many situations such as large scale fights, drones are irrelevant and their rendering can significantly hinder performance. However in smaller engagements drones can play a crucial role and thus their visibility in space is needed.

### / Brackets: Combat (-wrecks)
Variation without wrecks. While wrecks are typically useful to display in PVE situations and can be used as tactical warp-in points in PVP engagements, in larger quantities they can be seen as distracting clutter. Users of the CTRL+Drag&Select feature might prefer this bracket filter to avoid targeting wrecks when using it.

### ? DSCAN: Ships
Strictly defensive Dscan filter intended to warn you about ships and ships only.

### ? DSCAN: Basic
Standard multipurpose dscan filter, intended both for defense (displaying potentially dangerous objects like ships, combat probes and warp disruption bubbles) and offence (enabling to quickly locate targets).

### ? DSCAN: Extra

Dscan filter with expanded list of displayed objects. Intended for reconnaissance in wormholes, hunting specific targets (such as Combat Recons which themselves are immune to Dscan but secondary evidence such as wreck accumulation can be observed), etc.

### ⌘ All: All
Displays all objects and all states. Intended for situations that require finding obscure mission objectives or navigating while cloaked.

### ✪ System: System
Standard navigation filter. Displays warpable objects beyond current grid.

### ✪ System: System (-citadels)
Variation without citadels. Due to extreme Upwell structure spam in some areas such as The Citadel region around the system of Jita or near Goonswarm staging in Delve.

### ✪ System: System (+belts)
Variation with permanent asteroid belts.

### ✪ System: Mining
Only asteroids and permanent asteroid belts.

### ✪ System: Beacons
Only warpable beacons.

### ➔ Warp: Warp out!
Designed as a list of relatively safe warp destinations usable in emergency, for example after encountering a gatecamp, being chased by tackle or to save your pod after your ship is destroyed. This filter is also handy for hunting miners, PI haulers and anyone else loitering at such locations. 

### ➔ Warp: Travel
Intended to allow quick navigation on congested grids in nullsec staging systems or hisec trade hubs.

Note: This is deprecated legacy filter; multiple overview window support alleviates the need for this.

### ➔ Warp: Travel (-citadels)
Variation without citadels. Due to extreme Upwell structure spam in some areas such as The Citadel region around the system of Jita or near Goonswarm staging in Delve.

Note: This is deprecated legacy filter; multiple overview window support alleviates the need for this. Furthermore, Upwell structure spam is significantly less of a problem than it used to be.

### ❒ Loot: Loot and salvage
Containers, wrecks and common openable or destructible mission objects.

### ✜ Drones: Drones and Fighters (all)
Drones and fighters belonging to player ships or player structures.

### ✜ Drones: Drones and Fighters (red+neutral)
Drones and fighters. Only those that belong to entities with neutral or negative standing.

### ✜ Drones: Fighters (red+neutral)
Fighters that belong to entities with neutral or negative standing. 

### ❖ Ships: NPCs (+turrets)
All NPC ships and other NPC entities including turrets.

### ❖ Ships: Friendly
Ships of players with positive standing, including a corporation and alliance members.

### ❖ Ships: Fleet
Player ships that are part of your fleet regardless of standings. Useful mainly for logistics pilots who prefer it to watchlist or NPSI fleets as well.

### ❖ Ships: Enemy All (red)
Ships belonging to players with negative standings.

### ❖ Ships: Enemy All (red -capsules)
Ships belonging to players with negative standings. Excludes capsules since they do not pose a threat themselves and often aren't interesting targets.

### ❖ Ships: Enemy All (red+neutral)
Ships belonging to players with negative or neutral standings.

### ❖ Ships: Enemy All (red+neutral -capsules)
Ships belonging to players with negative or neutral standings. Excludes capsules since they do not pose a threat themselves and often aren't interesting targets.

### ❖ Ships: Enemy All (war targets)

Ships belonging to players that your corporation is at war with. They can be freely attacked in hisec.

### ❖ Ships: Enemy All (hisec criminals)
All player ships that can be attacked in hisec without Concord interference.

### ❖ Ships: Enemy Logi (red+neutral)
Logistic ships belonging to players with negative or neutral standings.

### ❖ Ships: Enemy Utility (red+neutral)
Force multiplier utility ships (booshers, links and interdictors) belonging to players with negative or neutral standings.

### ❖ Ships: Enemy Capitals (red+neutral)
Capital ships belonging to players with negative or neutral standings.

### ✱ Main: PVX
This filter combines previously used `Main: PVE` and `Main: PVP` into single universal filter, suitable for most situations and activities.

### ✱ Main: PVX (+extra)
Includes additional objects of interest (mainly for PVE) such as depots, containers, mission objectives, some destructible structures, tractor units and some beacons.

### ✱ Main: PVX (+friendly +extra)
Includes ships of players with positive standing, corporation and alliance members.

### ✱ Main: PVX (-npc)
Excludes NPC ships.

### ✱ Main: PVX (+mining)
Includes clouds and asteroids.

### ✕ Main: System & PVX (+extra)
Combines `✪ System: System` and `✱ Main: PVX (+extra)` into single filter for single-overview-window users.

### ✕ Main: System & PVX (-npc)
Combines `✪ System: System` and `✱ Main: PVX (-npc)` into single filter for single-overview-window users.
