import math
import random
import json

class Ingredient:
    """
    This class represents an ingredient in the simulator
    """
    def __init__(self):
        self.name = None
        self.quality = 0
        self.sweet = 0
        self.salt = 0
        self.blendability = 0
        self.temperature = 0
        self.liquidity = 0
        self.size = 0
        self.rot = 0
        self.holiness = 0
        self.eaten = 0
        self.luck = 0
        self.arcana = None
        self.atomicnumber = 0
        self.element = None
        self.sentience = 0

        with open("data/food/foods.json") as f:
            json_data = json.load(f)
            name = random.choice(list(json_data.keys()))
            data = json_data[name]
            self.name = name
            for stat, value in data.items():
                if stat in ["atomicnumber", "sentience", "element", "arcana"]:
                    setattr(self, stat, value)
                else:
                    setattr(self, stat, random.randint(value["min"], value["max"]))

    def __str__(self):
        return f"{self.name} \nQuality: {self.quality} \nSweet: {self.sweet} \nSalt: {self.salt} \nBlendability: {self.blendability} \nTemp: {self.temperature} \nLiquidity: {self.liquidity} \nSize: {self.size} \nRot: {self.rot} \nHoliness: {self.holiness} \nEaten: {self.eaten} \nLuck: {self.luck} \nArcana: {self.arcana} \nAN: {self.atomicnumber} \nElement: {self.element} \nSentience: {self.sentience} \n"

class Appliance:
    def __init__(self, name, statEffects:{}):
        """
        Creates an Appliance object
        :param name: Name of appliance
        :param statEffects: Dictionary of stats effects
        """
        self.name = name
        self.statEffects = statEffects

    def applianceUsed(self, ingredient: Ingredient):
        """
        Uses the appliance on the provided ingredient object
        :param ingredient: Ingredient object
        :return: Modified Ingredient object
        """
        for stat, change in self.statEffects.items():
            print(f"{self.name} used to increase {stat} by {change}")
            setattr(ingredient, stat, min(max(getattr(ingredient, stat) + change["add"], -50), 50))
            setattr(ingredient, stat, min(max(getattr(ingredient, stat) * change["mult"],-50), 50))
            print(f"{stat} increased to {getattr(ingredient, stat)}")
        return ingredient

class Dish:
    def __init__(self):
        """Creates a dish object with empty stats"""
        self.name = None
        self.mainIngredient = None
        self.quality = 0
        self.integrity = 0
        self.artistry = 0
        self.enchantment = 0
        self.ingredients = []

    def __str__(self):
        return f"{self.name} \n {self.quality} Quality {''.join(['★' for x in range(round(self.quality/(50*len(self.ingredientList))))])}{'⯪' if round(self.quality%(50*len(self.ingredientList))) > 25 else ''} \n {self.integrity} Integrity {''.join(['★' for x in range(round(self.integrity/(50*len(self.ingredientList))))])}{'⯪' if round(self.integrity%(50*len(self.ingredientList))) > 25 else ''}\n {self.artistry} Artistry {''.join(['★' for x in range(round(self.artistry/(50*len(self.ingredientList))))])}{'⯪' if round(self.artistry%(50*len(self.ingredientList))) > 25 else ''}\n {self.enchantment} Enchantment {''.join(['★' for x in range(round(self.enchantment/(50*len(self.ingredientList))))])}{'⯪' if round(self.enchantment%(50*len(self.ingredientList))) > 25 else ''}\n \n \n"

    def determineMainIngredient(self, ingredientList: list[Ingredient]):
        """
        Sets the ingredient list and chooses a main ingredient (currently random)
        :param ingredientList: List of Ingredient objects
        :return: none
        """
        self.ingredientList = ingredientList
        self.mainIngredient = random.choice(ingredientList)

    def determineName(self):
        """
        Chooses a name for dish
        :return: none
        """
        dishes = [
                "soup",
                "salad",
                "stew",
                "curry",
                "sandwich",
                "pasta",
                "pie",
                "stir fry",
                "casserole",
                "risotto",
                "tacos",
                "burger",
                "omelette",
                "wrap",
                "pizza",
                "lasagna",
                "noodles",
                "bake",
                "dip",
                "skewers",
                "gratin",
                "sauce",
                "toast",
                "rolls",
                "chili",
                "quiche",
                "patties",
                "gnocchi",
                "dumplings",
                "kabobs"
        ]
        self.name = f"{self.mainIngredient.name} {random.choice(dishes)}"

    def addIngredient(self, ingredient: Ingredient):
        """
        Adds an ingredient to the dish stats
        """
        self.quality += round(ingredient.quality + ingredient.sweet + ingredient.salt + abs(ingredient.temperature) - ingredient.rot + ingredient.luck*0.1 - ingredient.eaten)
        self.integrity += round(ingredient.luck*0.1 + ingredient.size - ingredient.blendability - ingredient.liquidity - ingredient.eaten - ingredient.rot - ingredient.atomicnumber)
        self.artistry += round(ingredient.sweet + ingredient.size - ingredient.rot + ingredient.holiness + ingredient.luck*0.1)
        self.enchantment += round(ingredient.luck*0.1 + ingredient.salt + ingredient.rot + ingredient.sentience + ingredient.holiness)

class Judge:
    def __init__(self):
        """
        Create a Judge object, with random preferences
        """
        first_names = [
            "Gordon",
            "Jamie",
            "Wolfgang",
            "Anthony",
            "Julia",
            "Nigella",
            "Thomas",
            "Alice",
            "Emeril",
            "Bobby",
            "Massimo",
            "Heston",
            "Ferran",
            "José",
            "Ina",
            "Rachael",
            "Marco",
            "Grant",
            "Curtis",
            "Christina"
        ]
        last_names = [
            "Ramsay",
            "Oliver",
            "Puck",
            "Bourdain",
            "Child",
            "Lawson",
            "Keller",
            "Waters",
            "Lagasse",
            "Flay",
            "Bottura",
            "Blumenthal",
            "Adrià",
            "Andrés",
            "Garten",
            "Ray",
            "White",
            "Achatz",
            "Stone",
            "Tosi"
        ]
        self.name = f"{random.choice(first_names)} {random.choice(last_names)}"
        # The code after this creates a list of 4 numbers summing to 100, such as [25, 15, 35, 25], with each number being a preference towards a dish stat in the order quality integrity artistry enchantment
        self.values = [random.randint(0, 100) for _ in range(4)]
        if sum(self.values) == 0:
            self.values = [0, 0, 0, 100]
        else:
            self.values = [round((v / sum(self.values)) * 100) for v in self.values]

class Kitchen:
    def __init__(self, name):
        """
        Initialise a kitchen object containing a name and a list of appliances.
        Kitchens also store ingredients during the match
        :param name: Name of Kitchen
        """
        self.name = name
        self.appliances = []

        with open("data/appliances/appliancelist.json") as f:
            for name, data in json.load(f)["appliances"].items():
                self.appliances.append(Appliance(name, data))

        self.ingredients = []

    def addIngredient(self, ingredient: Ingredient):
        """
        Add an ingredient to the kitchen.
        :param ingredient: Ingredient to add.
        :return: none
        """
        self.ingredients.append(ingredient)

    def clearIngredient(self):
        """
        Clear all ingredients from the kitchen.
        :return: none
        """
        self.ingredients = []

    def createDish(self):
        """
        Create a dish from all ingredients within the kitchen.
        :return: The created Dish object
        """
        dish = Dish()
        for ingredient in self.ingredients:
            dish.addIngredient(ingredient)

        dish.determineMainIngredient(self.ingredients)
        dish.determineName()
        return dish

class Player:
    def __init__(self):
        """
        Initialise a player object, currently contains stats and a name, as well as a team name and inventory list.
        """
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
        self.isHome = None
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

    def setHome(self, homeaway: bool):
        """
        Designate player as part of the Home Team for the match
        :param homeaway: True if home
        :return: none
        """
        self.isHome = homeaway

    def setTeamName(self, teamName):
        """
        Sets team name for player
        :param teamName: Team name
        :return: none
        """
        self.teamName = teamName

    def addToInventory(self, ingredient: Ingredient):
        """
        Adds ingredient to player inventory for running phase.
        :param ingredient: Ingredient object
        :return: none
        """
        self.inventory.append(ingredient)

    def chooseAppliance(self, kitchen: Kitchen):
        """
        Player will choose an appliance from the list of appliances in the kitchen provided.
        :param kitchen: Kitchen object
        :return: none
        """
        appliance = random.choice(kitchen.appliances)
        ingredientNum = random.randint(0, len(kitchen.ingredients)-1)
        kitchen.ingredients[ingredientNum] = appliance.applianceUsed(kitchen.ingredients[ingredientNum])

class Arena:
    def __init__(self, name):
        """
        Initialise a new arena, currently just contains a name
        :param name: Name of the arena.
        """
        self.name = name
        # Arena Stats

class Team:
    def __init__(self, name, arena: Arena):
        """
        Initialises a new Team object.
        Team objects contain by default:
         - Name
         - Empty Chef List
         - Empty Runner List
         - Arena
         - Default Kitchen
        :param name: Name of the Team
        :param arena: Arena object
        """
        self.name = name
        self.chefs = []
        self.runners = []
        self.arena = arena
        self.kitchen = Kitchen("Yo mama")
        self.activeChef = None

    def addChef(self, chef: Player):
        """
        Adds a chef to the team
        :param chef: Player object to add
        :return: none
        """
        self.chefs.append(chef)

    def removeChef(self, chef: Player):
        """
        Removes a chef from the team
        :param chef: Player object to be removed
        :return: none
        """
        try:
            self.chefs.remove(chef)
        except:
            print("No such chef")

    def addRunner(self, runner: Player):
        """
        Adds a runner to the team
        :param runner: Player object to be added
        :return: none
        """
        self.runners.append(runner)

    def removeRunner(self, runner: Player):
        """
        Removes a runner from the team
        :param runner: Player Object to be removed
        :return: none
        """
        try:
            self.runners.remove(runner)
        except ValueError:
            print("No such runner")

    def rotateChef(self):
        """
        Rotates the active chef from the teams chef roster, or designates one on teams with no active chef
        :return: none
        """
        if self.activeChef is None:
            self.activeChef = self.chefs[0]
        else:
            self.chefs.append(self.chefs.pop(0))
            self.activeChef = self.chefs[0]

class Match:
    """
    The Match object contains information about a match, including home and away teams, current state of an in progress match, ingredient pile information, and judges.
    """
    def __init__(self, home: Team, away: Team):
        """
        Initialise the match
        :param home: Team Object for Home
        :param away: Team Object for Away
        :return: none
        """
        self.home = home
        self.away = away
        self.phase = "Preparation"
        self.pile = [] # Stores Ingredients in the pile
        self.piledist = 40 # Default distance to pile
        self.homedishes = []
        self.awaydishes = []
        self.judgeCount = 3
        self.judges = [Judge() for x in range(self.judgeCount)] # Creates set of Judges

        for player in home.runners + home.chefs:
            player.isHome = True
        for player in away.runners + away.chefs:
            player.isHome = False

    def preparation(self):
        """
        Performs the preparation phase of the match, currently nothing.
        :return: none
        """
        self.phase = "Running"

    def running(self):
        """
        Performs the running phase of the match, starting runners off getting ingredients.
        :return: none
        """
        # Generate Ingredients for Pile
        for x in range(0, random.randint(10, 20)):
            self.pile.append(Ingredient())

        for x in self.pile: # prints all ingredients for debug purposes
            print(x)

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
                if runner.isHome:
                    for ingredient in runner.inventory:
                        self.home.kitchen.ingredients.append(ingredient)
                else:
                    for ingredient in runner.inventory:
                        self.away.kitchen.ingredients.append(ingredient)
                runner.inventory = []
                pile_runners.pop(runner)
            cowards = []
            #if pile_runners empty, stop while loop
            if len(pile_runners) == 0:
                self.phase = "Cooking"
                break

            for runner, distance in pile_runners.items():
                # is runner here
                if distance > 0:
                    distance -= random.randint(0, 10+runner.spd)
                    pile_runners[runner] = distance
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
                    if selected_action == "gather":
                        chosen_ingredient = random.choice(self.pile)
                        print(f"Chosen ingredient {chosen_ingredient.name}\n")
                        runner.inventory.append(chosen_ingredient)
                        self.pile.remove(chosen_ingredient)
                    elif selected_action == "attack": # attack code currently does nothing
                        pass
                    else:
                        cowards.append(runner)

    def cooking(self):
        """
        Performs the Cooking step, doing actions to ingredients stored in kitchens
        :return: none
        """
        actionsLeft = 20 # Denotes the number of actions available by default
        while actionsLeft > 0:
            actionsLeft -= 1
            # each chef chooses an appliance
            self.home.activeChef.chooseAppliance(self.home.kitchen)
            self.away.activeChef.chooseAppliance(self.away.kitchen)
        # once actions are performed dish is created and stored in Kitchen Object
        self.homedishes.append(self.home.kitchen.createDish())
        self.awaydishes.append(self.away.kitchen.createDish())
        # Kitchen ingredient piles are cleared
        self.home.kitchen.clearIngredient()
        self.away.kitchen.clearIngredient()
        # Active chef is rotated
        self.home.rotateChef()
        self.away.rotateChef()
        # If 3rd dish has been made advances to judging
        if len(self.homedishes) == 3:
            for dish in self.homedishes:
                print(dish)
            for dish in self.awaydishes:
                print(dish)
            self.phase = "Judging"
        else:
            self.phase = "Preparation"

    def judging(self):
        """
        Performs the Judging step, awarding points based on the Judges in the match object.
        :return: none
        """
        homepoints = 0
        awaypoints = 0
        for dish in self.homedishes:
            for judge in self.judges:
                points = 0
                points += round(judge.values[0]*0.01 * dish.quality)
                points += round(judge.values[1]*0.01 * dish.integrity)
                points += round(judge.values[2]*0.01 * dish.artistry)
                points += round(judge.values[3]*0.01 * dish.enchantment)
                print(f"Judge {judge.name} has awarded {dish.name} {points} points")
                homepoints += points
            print("--------------------------------------------------")
        for dish in self.awaydishes:
            for judge in self.judges:
                points = 0
                points += round(judge.values[0]*0.01 * dish.quality)
                points += round(judge.values[1]*0.01 * dish.integrity)
                points += round(judge.values[2]*0.01 * dish.artistry)
                points += round(judge.values[3]*0.01 * dish.enchantment)
                print(f"Judge {judge.name} has awarded {dish.name} {points} points")
                awaypoints += points
            print("--------------------------------------------------")
        if homepoints == awaypoints:
            print(f"Tie \nHome: {homepoints}\nAway: {awaypoints}")
        elif homepoints > awaypoints:
            print(f"Home Victory \nHome: {homepoints}\nAway: {awaypoints}")
        else:
            print(f"Away Victory \nHome: {homepoints}\nAway: {awaypoints}")
        self.phase = "Done"
        pass

    def step(self):
        """
        Pushes the simulation forward by one step
        :return: none
        """
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
        team2.addChef(player)

    for x in range(7):
        player = Player()
        player.setTeamName(team2.name)
        team2.addRunner(player)

    team1.rotateChef()
    team2.rotateChef()

    match = Match(team1, team2)

    while match.phase != "Done":
        match.step()

if __name__ == "__main__":
    main()