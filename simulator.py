import math
import random

class Ingredient:
    def __init__(self):
        names = [
            "salt",
            "sugar",
            "butter",
            "milk",
            "eggs",
            "baking powder",
            "flour",
            "vanilla extract",
            "olive oil",
            "garlic",
            "onion",
            "tomato",
            "black pepper",
            "chicken breast",
            "beef",
            "carrot",
            "potato",
            "rice",
            "pasta",
            "cheddar cheese",
            "mozzarella",
            "spinach",
            "broccoli",
            "mushrooms",
            "lemon juice",
            "soy sauce",
            "honey",
            "cinnamon",
            "ginger",
            "cumin"
        ]
        self.name = random.choice(names)
        self.quality = 1

class Player:
    def __init__(self):
        firstnames = [
                    "James",
                    "Olivia",
                    "Liam",
                    "Emma",
                    "Noah",
                    "Ava",
                    "Elijah",
                    "Sophia",
                    "William",
                    "Isabella",
                    "Benjamin",
                    "Mia",
                    "Lucas",
                    "Charlotte",
                    "Henry",
                    "Amelia",
                    "Alexander",
                    "Harper",
                    "Daniel",
                    "Evelyn",
                    "Mateo",
                    "Abigail",
                    "Sebastian",
                    "Ella",
                    "Jack",
                    "Chloe",
                    "Aiden",
                    "Layla",
                    "Muhammad",
                    "Zoe"
        ]
        lastnames = [
                    "Smith",
                    "Johnson",
                    "Williams",
                    "Brown",
                    "Jones",
                    "Garcia",
                    "Miller",
                    "Davis",
                    "Rodriguez",
                    "Martinez",
                    "Hernandez",
                    "Lopez",
                    "Gonzalez",
                    "Wilson",
                    "Anderson",
                    "Thomas",
                    "Taylor",
                    "Moore",
                    "Jackson",
                    "Martin",
                    "Lee",
                    "Perez",
                    "Thompson",
                    "White",
                    "Harris",
                    "Sanchez",
                    "Clark",
                    "Ramirez",
                    "Lewis",
                    "Robinson"
        ]
        self.name = f"{random.choice(firstnames)} {random.choice(lastnames)}"
        self.teamName = None
        self.inventory = []
        # Chef Stats
        self.pro = 1 #Proficiency
        self.gus = 1 #Gusto
        self.div = 1 #Divinity
        self.dis = 1 #Dissapointability
        self.foc = 1 #Focus
        self.str = 1 #Strength
        self.cow = 1 #Cowardice
        self.spd = random.randint(1,5) #Speed
        self.thi = 1 #Thickness
        self.blo = 1 #Bloodlust
        self.sco = 1 #Scouting

        self.position = 1

    def setTeamName(self, teamName):
        self.teamName = teamName

    def addToInventory(self, ingredient: Ingredient):
        self.inventory.append(ingredient)

class Appliance:
    def __init__(self, name):
        self.name = name

class Arena:
    def __init__(self, name):
        self.name = name
        # Arena Stats
        self.appliances = []

class Team:
    def __init__(self, name, arena: Arena):
        self.name = name
        self.chefs = []
        self.runners = []
        self.arena = arena

    def addChef(self, chef: Player):
        self.chefs.append(chef)

    def removeChef(self, chef: Player):
        try:
            self.chefs.remove(chef)
        except:
            print("No such chef")

    def addRunner(self, runner: Player):
        self.runners.append(runner)

    def removeRunner(self, runner: Player):
        try:
            self.runners.remove(runner)
        except ValueError:
            print("No such runner")

class PlayingTeam(Team):
    def __init__(self, name, arena: Arena):
        super().__init__(name, arena)
        self.ingredients = []
        self.currentChef = 0
        self.dishes = []




class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.quality = 0

class Judge:
    def __init__(self, name):
        self.name = name

class Match:
    def __init__(self, home: Team, away: Team):
        self.home = home
        self.away = away
        self.phase = "Preparation"
        self.pile = []
        self.piledist = 200

    def preparation(self):
        self.phase = "Running"

    def running(self):
        # Generate Ingredients for Pile
        for x in range(0, random.randint(10, 20)):
            self.pile.append(Ingredient())

        # Generate Runner speed order
        pile_runners = {
        } # distance each runner is from pile, 0 = at pile, anything above = not
        for runner in self.home.runners:
            pile_runners[runner] = self.piledist
        for runner in self.away.runners:
            pile_runners[runner] = self.piledist
        # returning to base is instant
        running_tick = 0

        # Loop for ticking
        cowards = []
        while True:
            running_tick += 1
            #remove leavers from pile_runners list
            for runner in cowards:
                pile_runners.pop(runner)
            cowards = []
            print(list(pile_runners.items()))
            #if pile_runners empty, stop while loop
            if len(pile_runners) == 0:
                break

            for runner, distance in pile_runners.items():
                # is runner here
                if distance > 0:
                    distance -= random.randint(0, 10+runner.spd)
                    pile_runners[runner] = distance
                    print(f"{runner.name} is now {distance} away")
                # if not make runner get closer based on speed
                else:
                    # if runner is here (0 distance)
                    # if there is an opposing team runner present - set actions including attack
                    attack_possible = False
                    for other_runner, distance in pile_runners.items():
                        if distance <= 0 and other_runner.teamName != runner.teamName:
                            attack_possible = True
                            break
                    # if there isn't - set actions excluding attack
                    # if there are no ingredients left - consolidate running and gathering into just running
                    gathering_possible = True
                    if len(self.pile) <= 0:
                        gathering_possible = False
                    # get action percentages based on this
                    actions_to_add = ["run"]
                    if gathering_possible:
                        actions_to_add.append("gather")
                    if attack_possible:
                        actions_to_add.append("attack")
                    chances = round((1 / len(actions_to_add))*100)
                    action_chances = {}
                    for action in actions_to_add:
                        action_chances[action] = chances
                    selected_action = random.choices(population=list(action_chances.keys()), weights=list(action_chances.values()), k=1)[0]
                    print(f"Runner {runner.name} has chosen action {selected_action}\n")
                    if selected_action == "gather":
                        chosen_ingredient = random.choice(self.pile)
                        print(f"Chosen ingredient {chosen_ingredient.name}\n")
                        runner.inventory.append(chosen_ingredient)
                        self.pile.remove(chosen_ingredient)
                    elif selected_action == "attack":
                        pass
                    else:
                        cowards.append(runner)



    def cooking(self):
        pass

    def judging(self):
        pass

    def step(self):
        if self.phase == "Preparation":
            self.preparation()
        elif self.phase == "Running":
            self.running()
        elif self.phase == "Cooking":
            self.cooking()
        elif self.phase == "Judging":
            self.judging()

def main():
    team1 = Team("The british bakeoff", Arena("Gaming"))
    team2 = Team("The american grilloff", Arena("Not Gaming"))

    for x in range(4):
        player = Player()
        player.setTeamName(team1.name)
        team1.addChef(player)

    for x in range(7):
        player = Player()
        player.setTeamName(team1.name)
        team1.addRunner(player)

    for x in range(4):
        player = Player()
        player.setTeamName(team2.name)
        team1.addChef(player)

    for x in range(7):
        player = Player()
        player.setTeamName(team2.name)
        team1.addRunner(player)

    match = Match(team1, team2)

    match.step()
    match.step()

if __name__ == "__main__":
    main()