import random
import time


class Game:
    # Score constants
    SCORE_REWARDS = {
        "MISSION_ACCEPT": 10,
        "KILL_ENEMY": 20,
        "FIND_TREASURE": 30,
        "COMPLETE_LEVEL": 50,
        "WIN_GAME": 100
    }

    SCORE_PENALTIES = {
        "DEATH": -50,
        "MISSION_FAIL": -30,
        "WRONG_CHOICE": -10
    }

    def __init__(self):
        # Game Levels
        self.levels = {
            "death_island": {
                "name": "Death Island",
                "method": self.play_death_island,
                "completed": False
            },
            "ghost_ship": {
                "name": "Ghost Ship",
                "method": self.play_ghost_ship,
                "completed": False
            },
            "bermuda_triangle": {
                "name": "Bermuda Triangle",
                "method": self.play_bermuda_triangle,
                "completed": False
            },
            "land_of_pirates": {
                "name": "Land of Pirates",
                "method": self.play_land_of_pirates,
                "completed": False
            }
        }

        # Game rewards
        self.rewards = [
            "To be the king of Egypt",
            "To be the king of the world",
            "To be the Minister",
            "Win the world map",
            "Win the treasure chest",
            "Win the sword of power"
        ]

        self.character_name = self.get_player_name()
        print(
            f"Welcome {self.character_name} to the game!"
        )
        self.reset_game()

    def reset_game(self):
        self.player_health = 100
        self.score = 0
        self.high_score = 0
        for level in self.levels.values():
            level["completed"] = False

    def get_valid_input(self, prompt, options=("1", "2")):
        while True:
            try:
                choice = input(prompt).strip()
                if choice in options:
                    return choice
                print(
                    "Invalid input. Please choose from: "
                    f"{', '.join(options)}"
                )
            except (EOFError, KeyboardInterrupt):
                print("\nInput interrupted. Please try again.")
            except Exception as e:
                print(f"Error reading input: {e}")

    def get_player_name(self):
        while True:
            try:
                name = input("Enter your name: ").strip()
                if name and name.isprintable() and len(name) <= 20:
                    return name
                print(
                    "Please enter a valid name (max 20 characters)"
                )
            except (EOFError, KeyboardInterrupt):
                print("\nInput interrupted. Please try again.")
            except Exception as e:
                print(f"Error reading name: {e}")

    def update_score(self, points, reason=""):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
        msg = (
            f"\n{'Gained' if points > 0 else 'Lost'} "
            f"{abs(points)} points"
        )
        if reason:
            msg += (
                f" for {reason.replace('_', ' ').lower()}"
            )
        print(msg + "!")

    def show_status(self):
        print(
            f"\nPlayer Name: {self.character_name}"
        )
        print(
            f"Player Health: {self.player_health}"
        )
        print(
            f"Current Score: {self.score}"
        )
        print(
            f"High Score: {self.high_score}"
        )

    def get_current_level(self):
        level_order = [
            "death_island",
            "ghost_ship",
            "bermuda_triangle",
            "land_of_pirates"
        ]
        for level_name in level_order:
            if not self.levels[level_name]["completed"]:
                return level_name, self.levels[level_name]
        return None, None
        
    # Death island level
    def play_death_island(self):
        print("\n=== DEATH ISLAND LEVEL ===")

        time.sleep(1)
        print("\nYou lived in the Alexandria Governorate. "
              "You loved to travel and discover new places. "
              "Then the King of Egypt summoned you")
        print(" and told you that he wanted you to bring him \n"
              "1)The treasure chest,\n2)The sword of power,\n"
              "3)The world map.\n")
        time.sleep(1)
        while True:
            action = self.get_valid_input(
                "1) Do you accept the king\"s mission?" 
                " 2) Do you refuse? (1/2): "
            )
            time.sleep(1)
            if action == "1":
                print("\nThe King of Egypt was very happy"
                      " and gave you a ship"
                      " and arms to go on your mission.")
                self.update_score(
                    self.SCORE_REWARDS
                    ["MISSION_ACCEPT"],
                    "accepting the king\"s mission"
                )
                time.sleep(1)
                print("\nYou are now on a ship with your team and you have"
                      " to choose a direction to go.")
                direction = self.get_valid_input(
                    "1) North 2) South\nChoose a direction (1/2): "
                )
                time.sleep(1)
                if direction == "1":
                    print("\nYou entered a huge storm and the ship broke!")
                    self.player_health -= 100
                    time.sleep(1)
                    print("You are dead.")
                    self.update_score(
                        self.SCORE_PENALTIES["DEATH"],
                        "dying in the storm"
                    )
                    self.show_status()
                    time.sleep(1)
                    play_again = self.get_valid_input(
                        "\nDo you want to play again? (1)yes / 2)no): "
                    )
                    if play_again == "1":
                        self.player_health = 100
                        self.score = 0
                        return self.play_death_island()
                    elif play_again == "2":
                        print("Thank you for playing!")
                        return
                elif direction == "2":
                    print(
                        "\nYou see Death Island containing the treasure chest,"
                        " guarded by Cannibals and a Giant Snake."
                    )
                    time.sleep(1)
                    enter_island = self.get_valid_input(
                        "Enter the island? (1)yes / 2)no): "
                    )
                    time.sleep(1)
                    if enter_island == "1":
                        print("\nYou entered the island"
                              " and must fight the Giant Snake"
                              " who save the island!")
                        fight_or_run = self.get_valid_input(
                            "1) Fight 2) Run\nChoose an option (1/2): "
                        )
                        time.sleep(1)
                        if fight_or_run == "1":
                            weapon = self.get_valid_input(
                                "\nWhich weapon to fight the Giant Snake?"
                                "\n1) Sword 2) Gun\nChoose (1/2): "
                            )
                            time.sleep(1)
                            if weapon == "1":
                                print("\nThe sword had no effect!"
                                      " The Giant Snake killed you.")
                                time.sleep(1)
                                self.player_health -= 100
                                self.update_score(
                                    self.SCORE_PENALTIES
                                    ["DEATH"],
                                    "dying to the Giant Snake"
                                )
                                print("You are dead.")
                                self.show_status()
                                time.sleep(1)
                                play_again = self.get_valid_input(
                                    "Play again? (1)yes / 2)no): "
                                )
                                if play_again == "1":
                                    self.player_health = 100
                                    self.score = 0
                                    return self.play_death_island()
                                elif play_again == "2":
                                    print("Thanks for playing!")
                                    return
                            elif weapon == "2":
                                print("\nYou killed the Giant Snake!"
                                      " Now search for the treasure cave.")
                                self.update_score(
                                    self.SCORE_REWARDS["KILL_ENEMY"],
                                    "defeating the enemy"
                                )
                                time.sleep(1)
                                print("\nWhen you were searching"
                                      " about the treasure"
                                      " one from the Cannibals"
                                      " spot you and alert others!")
                                fight_or_run = self.get_valid_input(
                                    "1) Fight 2) Run\nChoose (1/2): "
                                )
                                time.sleep(1)
                                if fight_or_run == "1":
                                    weapon = self.get_valid_input(
                                        "\nChoose weapon:\n1) "
                                        "Sword 2) Gun\nChoose (1/2): "
                                    )
                                    time.sleep(1)
                                    if weapon == "1":
                                        print("\nSwords couldn't"
                                              " defeat all Cannibals!"
                                              " They killed you.")
                                        self.player_health -= 100
                                        self.update_score(
                                            self.SCORE_PENALTIES["DEATH"],
                                            "dying to Cannibals"
                                        )
                                        time.sleep(1)
                                        print("You are dead.")
                                        self.show_status()
                                        time.sleep(1)
                                        play_again = self.get_valid_input(
                                            "Play again? (1)yes / 2)no): "
                                        )
                                        if play_again == "1":
                                            self.player_health = 100
                                            self.score = 0
                                            return self.play_death_island()
                                        elif play_again == "2":
                                            print("Thanks for playing!")
                                            return
                                    elif weapon == "2":
                                        print("\nYou killed many Cannibals! "
                                              "Survivors tell you "
                                              "the treasure's location.")
                                        self.update_score(
                                            self.SCORE_REWARDS["KILL_ENEMY"],
                                            "defeating Cannibals"
                                        )
                                        time.sleep(1)
                                        print("They say the treasure is"
                                              " in a volcanic mountain.")
                                        time.sleep(1)
                                        climb_or_not = self.get_valid_input(
                                            "\n1) Climb mountain "
                                            "2) Don\"t climb\nChoose (1/2): "
                                        )
                                        time.sleep(1)
                                        if climb_or_not == "1":
                                            print("\nYou found "
                                                  "the treasure chest! "
                                                  "The volcano erupts!")
                                            time.sleep(1)
                                            run_or_throw = self.get_valid_input(
                                                "1) Run 2) Throw treasure"
                                                "\nChoose (1/2): "
                                            )
                                            time.sleep(1)
                                            if run_or_throw == "1":
                                                print("\nYou escaped "
                                                      "with the treasure!")
                                                time.sleep(1)
                                                print("You are a hero "
                                                      "you win "
                                                      "Death island level!")
                                                self.update_score(
                                                    self.SCORE_REWARDS
                                                    ["COMPLETE_LEVEL"],
                                                    "completing Death Island"
                                                )
                                                self.show_status()
                                                self.levels["death_island"]["completed"] = True
                                                return
                                            elif run_or_throw == "2":
                                                print("\nYou threw "
                                                      "the treasure into lava!"
                                                      " You died.")
                                                self.player_health -= 100
                                                self.update_score(
                                                    self.SCORE_PENALTIES
                                                    ["DEATH"],
                                                    "dying in the volcano"
                                                )
                                                time.sleep(1)
                                                print("You are dead.")
                                                self.show_status()
                                                time.sleep(1)
                                                play_again = self.get_valid_input(
                                                    "Play again? "
                                                    "(1)yes / 2)no): "
                                                )
                                                if play_again == "1":
                                                    self.player_health = 100
                                                    self.score = 0
                                                    return self.play_death_island()
                                                elif play_again == "2":
                                                    print("Thanks "
                                                          "for playing!")
                                                    return
                                        elif climb_or_not == "2":
                                            print("\nYou didn't climb."
                                                  " The King executed you!")
                                            self.player_health -= 100
                                            self.update_score(
                                                self.SCORE_PENALTIES
                                                ["MISSION_FAIL"],
                                                "failing the mission"
                                            )
                                            time.sleep(1)
                                            print("You are dead.")
                                            self.show_status()
                                            time.sleep(1)
                                            play_again = self.get_valid_input(
                                                "Play again? (1)yes / 2)no): "
                                            )
                                            if play_again == "1":
                                                self.player_health = 100
                                                self.score = 0
                                                return self.play_death_island()
                                            elif play_again == "2":
                                                print("Thanks for playing!")
                                                return
                                elif fight_or_run == "2":
                                    print("\nYou ran away!"
                                          " Cannibals hunted you down.")
                                    self.player_health -= 100
                                    self.update_score(
                                        self.SCORE_PENALTIES
                                        ["DEATH"],
                                        "dying while running away"
                                    )
                                    time.sleep(1)
                                    print("You are dead.")
                                    self.show_status()
                                    time.sleep(1)
                                    play_again = self.get_valid_input(
                                        "Play again? (1)yes / 2)no): "
                                    )
                                    if play_again == "1":
                                        self.player_health = 100
                                        self.score = 0
                                        return self.play_death_island()
                                    elif play_again == "2":
                                        print("Thanks for playing!")
                                        return
                        elif fight_or_run == "2":
                            print("\nYou ran away!"
                                  " The Giant snake killed you")
                            self.player_health -= 100
                            self.update_score(
                                self.SCORE_PENALTIES
                                ["DEATH"],
                                "dying while running away"
                            )
                            time.sleep(1)
                            print("You are dead.")
                            self.show_status()
                            time.sleep(1)
                            play_again = self.get_valid_input(
                                "Play again? (1)yes / 2)no): "
                            )
                            if play_again == "1":
                                self.player_health = 100
                                self.score = 0
                                return self.play_death_island()
                            elif play_again == "2":
                                print("Thanks for playing!")
                                return

                    elif enter_island == "2":
                        print("\nYou avoided the island!"
                              " Mission failed and the King Killed you.")
                        self.player_health -= 100
                        self.update_score(
                            self.SCORE_PENALTIES["MISSION_FAIL"],
                            "failing the mission"
                        )
                        time.sleep(1)
                        print("You are dead.")
                        self.show_status()
                        time.sleep(1)
                        play_again = self.get_valid_input(
                            "Play again? (1)yes / 2)no): "
                        )
                        if play_again == "1":
                            self.player_health = 100
                            self.score = 0
                            return self.play_death_island()
                        elif play_again == "2":
                            print("Thanks for playing!")
                            return
            elif action == "2":
                print("\nYou refused the king mission!"
                      " He imprisoned you.")
                self.player_health -= 100
                self.update_score(
                    self.SCORE_PENALTIES["MISSION_FAIL"],
                    "refusing the mission"
                )
                time.sleep(1)
                print("You are dead.")
                self.show_status()
                time.sleep(1)
                play_again = self.get_valid_input(
                    "Play again? (1)yes / 2)no): "
                )
                if play_again == "1":
                    self.player_health = 100
                    self.score = 0
                    return self.play_death_island()
                elif play_again == "2":
                    print("Thanks for playing!")
                    return

    # Ghost ship level
    def play_ghost_ship(self):
        print("\n=== GHOST SHIP LEVEL ===")
        print("\nYou are on a ghost ship!"
              " You must find the Sword of Power.")
        time.sleep(1)
        while True:
            print("\nYou are now on a ship with your"
                  " team and you have to choose a direction to go.")
            direction = self.get_valid_input(
                "1) North 2) South\nChoose a direction (1/2): "
            )
            time.sleep(1)
            if direction == "1":
                print("\nYou entered a huge storm and the ship broke!")
                self.player_health -= 100
                self.update_score(self.SCORE_PENALTIES
                                  ["DEATH"],
                                  "dying in the storm")
                time.sleep(1)
                print("You are dead.")
                self.show_status()
                time.sleep(1)
                play_again = self.get_valid_input(
                    "\nDo you want to play again? (1)yes / 2)no): "
                )
                if play_again == "1":
                    self.player_health = 100
                    self.score = 0
                    return self.play_ghost_ship()
                else:
                    print("Thank you for playing!")
                    return
            elif direction == "2":
                print("\nYou see a ghost ship that in it the Sword of Power,"
                      " guarded by ghost pirates.")
                time.sleep(1)
                enter_ship = self.get_valid_input(
                    "Enter the ship? (1)yes / 2)no): "
                )
                time.sleep(1)
                if enter_ship == "1":
                    print("\nYou entered "
                          "the ship and must "
                          "fight the ghost pirates!")
                    time.sleep(1)
                    fight_or_run = self.get_valid_input(
                        "1) Fight 2) Run\nChoose an option (1/2): "
                    )
                    time.sleep(1)
                    if fight_or_run == "1":
                        weapon = self.get_valid_input(
                            "\nChoose weapon:\n1) Gun "\
                            "2) Laser device\nChoose (1/2): "
                        )
                        time.sleep(1)
                        if weapon == "1":
                            print("\nThe gun had no effect!"
                                  " The ghost pirates killed you.")
                            self.player_health -= 100
                            self.update_score(self.SCORE_PENALTIES
                                              ["DEATH"],
                                              "dying to ghost pirates")
                            time.sleep(1)
                            print("You are dead.")
                            self.show_status()
                            time.sleep(1)
                            play_again = self.get_valid_input(
                                "Play again? (1)yes / 2)no): "
                            )
                            if play_again == "1":
                                self.player_health = 100
                                self.score = 0
                                return self.play_ghost_ship()
                            else:
                                print("Thanks for playing!")
                                return
                        elif weapon == "2":
                            print("\nYou killed the ghost"\
                                  "pirates with the laser!"
                                  "Found the Sword of Power!")
                            self.update_score(self.SCORE_REWARDS
                                              ["KILL_ENEMY"],
                                              "defeating ghost pirates")
                            time.sleep(1)
                            print("But the ship is sinking!")
                            time.sleep(1)
                            run_or_throw = self.get_valid_input(
                                "1) Run with sword "\
                                "2) Throw sword\nChoose (1/2): "
                            )
                            if run_or_throw == "1":
                                print("\nYou escaped with the Sword of Power!")
                                time.sleep(1)
                                print("You completed the Ghost Ship level!")
                                self.update_score(self.SCORE_REWARDS
                                                  ["COMPLETE_LEVEL"],
                                                  "completing"\
                                                  "Ghost Ship level")
                                self.show_status()
                                self.levels["ghost_ship"]["completed"] = True
                                return
                            else:
                                print("\nYou threw the sword and got eaten"
                                      " by sharks while you"\
                                      "were searching about it!")
                                self.player_health -= 100
                                self.update_score(self.SCORE_PENALTIES
                                                  ["DEATH"],
                                                  "dying to sharks")
                                time.sleep(1)
                                print("You are dead.")
                                self.show_status()
                                time.sleep(1)
                                play_again = self.get_valid_input(
                                    "Play again? (1)yes / 2)no): "
                                )
                                if play_again == "1":
                                    self.player_health = 100
                                    self.score = 0
                                    return self.play_ghost_ship()
                                else:
                                    print("Thanks for playing!")
                                    return
                    else:
                        print("\nYou ran away!"
                              " Ghost pirates caught you!")
                        self.player_health -= 100
                        self.update_score(self.SCORE_PENALTIES
                                          ["DEATH"],
                                          "dying while running away")
                        time.sleep(1)
                        print("You are dead.")
                        self.show_status()
                        time.sleep(1)
                        play_again = self.get_valid_input(
                            "Play again? (1)yes / 2)no): "
                        )
                        if play_again == "1":
                            self.player_health = 100
                            self.score = 0
                            return self.play_ghost_ship()
                        else:
                            print("Thanks for playing!")
                            return
                else:
                    print("\nYou avoided the ship!"
                          " The King killed you for failing the mission.")
                    self.player_health -= 100
                    self.update_score(self.SCORE_PENALTIES
                                      ["MISSION_FAIL"],
                                      "failing the mission")
                    time.sleep(1)
                    print("You are dead.")
                    self.show_status()
                    time.sleep(1)
                    play_again = self.get_valid_input(
                        "Play again? (1)yes / 2)no): "
                    )
                    if play_again == "1":
                        self.player_health = 100
                        self.score = 0
                        return self.play_ghost_ship()
                    else:
                        print("Thanks for playing!")
                        return

    # Bermuda Triangle level
    def play_bermuda_triangle(self):
        print("\n=== BERMUDA TRIANGLE LEVEL ===")
        print("\nYou are in the Bermuda Triangle!"
              " You must find the World Map.")
        time.sleep(1)
        while True:
            print("\nYou are now on a ship with your"
                  " team and you have to choose a direction to go.")
            time.sleep(1)
            direction = self.get_valid_input(
                "1) North 2) South\nChoose a direction (1/2): "
            )
            time.sleep(1)
            if direction == "1":
                print("\nYou entered a huge storm and the ship broke!")
                self.player_health -= 100
                self.update_score(self.SCORE_PENALTIES
                                  ["DEATH"],
                                  "dying in the storm")
                time.sleep(1)
                print("You are dead.")
                self.show_status()
                time.sleep(1)
                play_again = self.get_valid_input(
                    "\nDo you want to play again? (1)yes / 2)no): "
                )
                if play_again == "1":
                    self.player_health = 100
                    self.score = 0
                    return self.play_bermuda_triangle()
                else:
                    print("Thank you for playing!")
                    return
            elif direction == "2":
                print("\nYou see the"\
                      "Bermuda Triangle that in it the world map,"
                      " known as the devil\"s triangle."\
                      "Many who enter it never return."
                      " It may be in it the Great Octopus.")
                time.sleep(1)
                enter_island = self.get_valid_input(
                    "Enter the island? 1) No / 2) Yes: "
                )
                if enter_island == "1":
                    time.sleep(1)
                    print("\nYou avoided the island!"
                          " Mission failed and the King killed you.")
                    self.player_health -= 100
                    self.update_score(self.SCORE_PENALTIES
                                      ["MISSION_FAIL"],
                                      "failing the mission")
                    time.sleep(1)
                    print("You are dead.")
                    self.show_status()
                    time.sleep(1)
                    play_again = self.get_valid_input(
                        "Play again? (1)yes / 2)no): "
                    )
                    if play_again == "1":
                        self.player_health = 100
                        self.score = 0
                        return self.play_bermuda_triangle()
                    else:
                        print("Thanks for playing!")
                        return
                elif enter_island == "2":
                    print(
                        "\nYou entered the Bermuda Triangle. "
                        "The weather turns violent with storms."
                    )
                    time.sleep(1)
                    print("The ship is shaking!"\
                          "You must throw things overboard to save it.")
                    time.sleep(1)
                    throw = self.get_valid_input(
                        "1) Throw the treasure chest"\
                        "2) Throw your arms\nChoose (1/2): "
                    )
                    time.sleep(1)
                    if throw == "1":
                        print("\nYou threw the treasure chest."\
                              "The ship stabilizes,"\
                              "but you failed the mission!")
                        self.player_health -= 100
                        self.update_score(self.SCORE_PENALTIES
                                          ["MISSION_FAIL"],
                                          "failing the mission")
                        time.sleep(1)
                        print("The King executes you for losing the treasure!")
                        self.show_status()
                        time.sleep(1)
                        play_again = self.get_valid_input(
                            "Play again? (1)yes / 2)no): "
                        )
                        if play_again == "1":
                            self.player_health = 100
                            self.score = 0
                            return self.play_bermuda_triangle()
                        else:
                            print("Thanks for playing!")
                            return
                    elif throw == "2":
                        print("\nYou threw your arms."
                              "The ship is safe, but now you\"re defenseless!")
                        time.sleep(1)
                        print("The storm subsides,"
                              "revealing the island."
                              "You approach and encounter the Great Octopus!")
                        time.sleep(1)
                        fight_or_run = self.get_valid_input(
                            "1) Fight 2) Run\nChoose (1/2): "
                        )
                        time.sleep(1)
                        if fight_or_run == "1":
                            weapon = self.get_valid_input(
                                "\nChoose a weapon:"\
                                "1) Gun "\
                                "2) Sword of Power\nChoose (1/2): "
                            )
                            time.sleep(1)
                            if weapon == "1":
                                print("\nThe gun is ineffective!"\
                                      "The Octopus kills you.")
                                time.sleep(1)
                                self.player_health -= 100
                                self.update_score(self.SCORE_PENALTIES
                                                  ["DEATH"],
                                                  "dying to the Great Octopus")
                                print("You are dead.")
                                self.show_status()
                                time.sleep(1)
                                play_again = self.get_valid_input(
                                    "Play again? (1)yes / 2)no): "
                                )
                                if play_again == "1":
                                    self.player_health = 100
                                    self.score = 0
                                    return self.play_bermuda_triangle()
                                else:
                                    print("Thanks for playing!")
                                    return
                            elif weapon == "2":
                                print("\nThe Sword of Power glows!"\
                                      "How will you activate it?")
                                time.sleep(1)
                                how = self.get_valid_input(
                                    "1) Press red button "\
                                    "2) Press blue button\nChoose (1/2): "
                                )
                                time.sleep(1)
                                if how == "1":
                                    print("\nThe sword emits a beam,"\
                                          "killing the Octopus!"\
                                          "You find the World Map in a cave.")
                                    self.update_score(self.SCORE_REWARDS
                                                      ["KILL_ENEMY"],
                                                      "defeating"\
                                                      "the Great Octopus")
                                    time.sleep(1)
                                    print("As you"\
                                          "leave,"\
                                          "rocks collapse!"\
                                          "Choose your escape path.")
                                    time.sleep(1)
                                    way = self.get_valid_input(
                                        "1) Left 2) Right\nChoose (1/2): "
                                    )
                                    if way == "1":
                                        print("\nRocks crush you! You die.")
                                        self.player_health -= 100
                                        self.update_score(self.SCORE_PENALTIES
                                                          ["DEATH"],
                                                          "dying in the cave")
                                        self.show_status()
                                        time.sleep(1)
                                        play_again = self.get_valid_input(
                                            "Play again? (1)yes / 2)no): "
                                        )
                                        if play_again == "1":
                                            self.player_health = 100
                                            self.score = 0
                                            return self.play_bermuda_triangle()
                                        else:
                                            print("Thanks for playing!")
                                            return
                                    elif way == "2":
                                        print("\nYou escape safely"\
                                              "with the World Map!")
                                        self.update_score(self.SCORE_REWARDS
                                                          ["COMPLETE_LEVEL"],
                                                          "completing Bermuda"\
                                                          "Triangle level")
                                        time.sleep(1)
                                        print("You completed"\
                                              "the Bermuda Triangle level!")
                                        self.show_status()
                                        self.levels["bermuda_triangle"]["completed"] = True
                                        return
                                elif how == "2":
                                    print("\nThe sword"\
                                          "backfires,"\
                                          "killing you!")
                                    self.player_health -= 100
                                    self.update_score(self.SCORE_PENALTIES
                                                      ["DEATH"],
                                                      "dying to the"\
                                                      "sword backfire")
                                    time.sleep(1)
                                    print("You are dead.")
                                    self.show_status()
                                    time.sleep(1)
                                    play_again = self.get_valid_input(
                                        "Play again? (1)yes / 2)no): "
                                    )
                                    if play_again == "1":
                                        self.player_health = 100
                                        self.score = 0
                                        return self.play_bermuda_triangle()
                                    else:
                                        print("Thanks for playing!")
                                        return
                        elif fight_or_run == "2":
                            print("\nYou try to run, "\
                                  "but the Octopus drags you under!")
                            self.player_health -= 100
                            self.update_score(self.SCORE_PENALTIES
                                              ["DEATH"],
                                              "dying while running away")
                            time.sleep(1)
                            print("You are dead.")
                            self.show_status()
                            time.sleep(1)
                            play_again = self.get_valid_input(
                                "Play again? (1)yes / 2)no): "
                            )
                            if play_again == "1":
                                self.player_health = 100
                                self.score = 0
                                return self.play_bermuda_triangle()
                            else:
                                print("Thanks for playing!")
                                return

    # Land of Pirates level
    def play_land_of_pirates(self):
        print("\n=== LAND OF PIRATES LEVEL ===")
        print("\nYou are in the Land of Pirates! Find the Treasure Chest Key.")
        time.sleep(1)
        while True:
            print("\nChoose a direction to sail:")
            time.sleep(1)
            direction = self.get_valid_input(
                "1) North 2) South\nChoose (1/2): "
            )
            time.sleep(1)
            if direction == "1":
                print("\nA storm destroys your ship! You die.")
                time.sleep(1)
                self.player_health -= 100
                self.update_score(self.SCORE_PENALTIES
                                  ["DEATH"],
                                  "dying in the storm")
                self.show_status()
                time.sleep(1)
                play_again = self.get_valid_input(
                    "Play again? (1)yes / 2)no): "
                )
                if play_again == "1":
                    self.player_health = 100
                    self.score = 0
                    return self.play_land_of_pirates()
                else:
                    print("Thanks for playing!")
                    return
            elif direction == "2":
                print("\nYou spot the Pirate King\"s island."\
                      "That the key was with"\
                      "the king of the pirates and the pirates save him.")
                time.sleep(1)
                enter = self.get_valid_input(
                    "1) Avoid island 2) Land and fight\nChoose (1/2): "
                )
                time.sleep(1)
                if enter == "1":
                    print("\nThe mission failed and the king killed you!")
                    self.player_health -= 100
                    self.update_score(self.SCORE_PENALTIES
                                      ["MISSION_FAIL"],
                                      "failing the mission")
                    time.sleep(1)
                    print("You are dead.")
                    self.show_status()
                    time.sleep(1)
                    play_again = self.get_valid_input(
                        "Play again? (1)yes / 2)no): "
                    )
                    if play_again == "1":
                        self.player_health = 100
                        self.score = 0
                        return self.play_land_of_pirates()
                    else:
                        print("Thanks for playing!")
                        return
                elif enter == "2":
                    print("\nYou confront the Pirate King and his crew!")
                    time.sleep(1)
                    fight = self.get_valid_input(
                        "1) Fight 2) Run\nChoose (1/2): "
                    )
                    time.sleep(1)
                    if fight == "2":
                        print("\nThey catch you and killed you!")
                        self.player_health -= 100
                        self.update_score(self.SCORE_PENALTIES
                                          ["DEATH"],
                                          "dying while running away")
                        self.show_status()
                        time.sleep(1)
                        play_again = self.get_valid_input(
                            "Play again? (1)yes / 2)no): "
                        )
                        if play_again == "1":
                            self.player_health = 100
                            self.score = 0
                            return self.play_land_of_pirates()
                        else:
                            print("Thanks for playing!")
                            return
                    elif fight == "1":
                        weapon = self.get_valid_input(
                            "\nChoose weapon:"\
                            "1) Gun "\
                            "2) Sword of Power\nChoose (1/2): "
                        )
                        time.sleep(1)
                        if weapon == "1":
                            print("\nYou shoot some pirates,"\
                                  "but the King kills you!")
                            self.player_health -= 100
                            self.update_score(self.SCORE_PENALTIES
                                              ["DEATH"]
                                              , "dying to the Pirate King")
                            time.sleep(1)
                            print("You are dead.")
                            self.show_status()
                            time.sleep(1)
                            play_again = self.get_valid_input(
                                "Play again? (1)yes / 2)no): "
                            )
                            if play_again == "1":
                                self.player_health = 100
                                self.score = 0
                                return self.play_land_of_pirates()
                            else:
                                print("Thanks for playing!")
                                return
                        elif weapon == "2":
                            print("\nThe Sword of Power"\
                                  "activates! Choose a button:")
                            time.sleep(1)
                            btn = self.get_valid_input(
                                "1) Green 2) Blue\nChoose (1/2): "
                            )
                            time.sleep(1)
                            if btn == "1":
                                print("\nWrong button! The sword explodes.")
                                time.sleep(1)
                                self.player_health -= 100
                                self.update_score(self.SCORE_PENALTIES
                                                  ["DEATH"],
                                                  "dying to the"\
                                                  "sword explosion")
                                time.sleep(1)
                                print("You are dead.")
                                self.show_status()
                                time.sleep(1)
                                play_again = self.get_valid_input(
                                    "Play again? (1)yes / 2)no): "
                                )
                                if play_again == "1":
                                    self.player_health = 100
                                    self.score = 0
                                    return self.play_land_of_pirates()
                                else:
                                    print("Thanks for playing!")
                                    return
                            elif btn == "2":
                                print("\nThe sword destroys"\
                                      "the pirates!"\
                                      "You take the key.")
                                self.update_score(self.SCORE_REWARDS
                                                  ["KILL_ENEMY"],
                                                  "defeating the Pirate King")
                                time.sleep(1)
                                print("You sudden that "
                                      "the treasure chest wants "
                                      "a code to open it")
                                time.sleep(1)
                                treasure_code = str(random.randint(1000, 9999))
                                print(
                                    f"Using the world map you "
                                    f"find the code {treasure_code} "
                                    "to open the treasure chest."
                                )
                                time.sleep(1)
                                code = input("Enter the code: ").strip()
                                time.sleep(1)
                                if code == treasure_code:
                                    print(f"\nThe chest opens")
                                    self.update_score(
                                        self.SCORE_REWARDS["COMPLETE_LEVEL"],
                                        "completing Land of Pirates level"
                                    )
                                    time.sleep(1)
                                    print("You win the Land of Pirates level!")
                                    time.sleep(1)
                                    self.levels["land_of_pirates"]["completed"] = True
                                    # Check if all levels are completed
                                    if all(level["completed"] 
                                           for level in self.levels.values()):
                                        print("\nCongratulations! "
                                              "You've completed all levels!")
                                        self.update_score(
                                            self.SCORE_REWARDS["WIN_GAME"], 
                                            "winning the game"
                                        )
                                        time.sleep(1)
                                        print("Final Status:")
                                        self.show_status()
                                        time.sleep(1)
                                        final_reward = random.choice(self.rewards)
                                        print(f"\nAs a reward for completing "
                                              f"all levels, you have won: "
                                              f"{final_reward}!")
                                        time.sleep(1)
                                        play_again = self.get_valid_input(
                                            "Do you want to play again? "
                                            "(1)yes / 2)no): "
                                        )
                                        if play_again == "1":
                                            self.player_health = 100
                                            self.score = 0
                                            return
                                        else:
                                            print("Thanks for playing!")
                                            return
                                else:
                                    print("\nIncorrect code! The chest explodes.")
                                    self.player_health -= 100
                                    self.update_score(self.SCORE_PENALTIES["DEATH"], "dying to the chest explosion")
                                    time.sleep(1)
                                    print("You are dead.")
                                    self.show_status()
                                    time.sleep(1)
                                    play_again = self.get_valid_input(
                                        "Play again? (1)yes / 2)no): "
                                    )
                                    if play_again == "1":
                                        self.player_health = 100
                                        self.score = 0
                                        return self.play_land_of_pirates()
                                    else:
                                        print("Thanks for playing!")
                                        return
                                        
                                        
    def play(self):
        WIN_SCORE = 200
        LOSE_SCORE = -100
        while True:
            level_name, level_data = self.get_current_level()
            if level_data is None:
                print("\nCongratulations! You've completed all levels!")
                self.show_status()
                final_reward = random.choice(self.rewards)
                print(f"\nAs a reward, you win: {final_reward}!")
                play_again = self.get_valid_input(
                    "\nPlay again? (1)yes / (2)no: "
                )
                if play_again == "1":
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    return
            print(f"\nStarting {level_data['name']} level...")
            level_data["method"]()
            
            if self.score <= LOSE_SCORE:
                print("\nGame Over! Your score is too low.")
                self.show_status()
                play_again = self.get_valid_input(
                    "\nTry again? (1)yes / (2)no: "
                )
                if play_again == "1":
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    return
            if self.score >= WIN_SCORE:
                print("\nCongratulations! You've achieved the winning score!")
                self.show_status()
                final_reward = random.choice(self.rewards)
                print(f"\nAs a reward, you win: {final_reward}!")
                play_again = self.get_valid_input(
                    "\nPlay again? (1)yes / (2)no: "
                )
                if play_again == "1":
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    return
                
if __name__ == "__main__":
    game = Game()
    game.play()