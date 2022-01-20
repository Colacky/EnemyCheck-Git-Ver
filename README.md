# EnemyCheck Github Version
 A script allowing the user to check other players' versatility in World of Warcraft.

## How to use it

To run the program:
1. Head to venv/Scripts and activate the virtual environment.
2. Go back to the main directory and use "pip install -r requirements.txt" to install required libraries
3. Head over to [Battle.Net Deveveloper Portal]https://develop.battle.net/ and sign up for API Access
4. Once you receive your Client ID and Client Secret, pass them into auth.py
5. Run enemycheckGUI.py
6. Insert enemy credentials pulled directly from World of Warcraft (name-realm format) into input fields on the left and then press "Find the weakest link". Their versatility values will be put in the fields on the right. The player with the lowest versatility is the weakest link and should be targeted first.

## How to pull enemy names in World of Warcraft

Typing enemy names by hand is annoying and time-consuming. There are work arounds for this.
You can use a macro in-game to put enemy target name into chat:
/script print(GetUnitName("target", true))
Use that macro on all enemies, and then copy them from in-game chat into the Weakest Link input fields.

### Possible future for the program

I have currently quit World of Warcraft, however I might still develop a web-app version of this program - if WoW doesn't die by that time, that is :).
