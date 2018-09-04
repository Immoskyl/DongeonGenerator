I was getting bored lately so for no reason I decided to write a little pseudo-random generation script based on a tabletop oriented method provided in "Mener des parties de jeu de rôle" (French tabletop collection of texts that can be found here: https://fr.ulule.com/jeu-de-role/ , http://www.legrog.org/jeux/documentation-etudes/sortir-de-l-auberge/mener-des-parties-de-jeu-de-role-fr ).

Basically the dongeonGenerator script is a tool really easy to use. Its goal is to help the DMs to create dongeons, designing a given number of rooms by randomly picking in an attribute list (which can always be extanded.
It allows to build inhabited rooms (or not) with different features (natural hazards, special events, etc) in a text format. Of course the script does not do all the work, bit that's the point: its goal is only to inspire the DM to go further than the classic golden-hammerish dongeon crawling.
Here's an exemple of a generated room:

Salle n°3:
Est occupée par 1 combattant hostile spécial et 3 alliés potentiels et est habituellement utilisée pour les Ressources (cultures, réserve, matériel, constructions...).
Elle renferme un objet aux propriétés spéciales.

Creating dongeons using this script may be useful for:
-Creating or enlarge a dongeon on the fly while playing so that the DM can focus on something else than pure creation. This avoids series of dull rooms opened and slayered by PCs.
-Suggest original possibilities of room/entier dongeons that one would not have think of immediately. The unprecedente often becomes interesting for both the PCs and the DM by pushing both sides beyond their confort zone.


It works quite well, sometimes the room combinations are bad so one shall just drop that room or modify that one, but overall it suggests interesting dongeon layouts to custom at will.
Talking about customisation, there are alreay some input variables (number of special rooms, etc) and some basic features (textfile saving, etc) and can of course be overwritten according to your needs/universe/goal.

So yeah that's it folks, just run it with python (2.7+) in a prompt, or take a look at the code to modify some variables.
