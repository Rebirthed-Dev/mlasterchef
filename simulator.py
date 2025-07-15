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
        self.quality = 1 # q+ i+
        self.sweet = 1 # q+ a+
        self.salt = 1 # q+ e-
        self.blendability = 1 # i-
        self.temperature = 1 # q*
        self.liquidity = 1 # i-
        self.size = 1 # i+ a+
        self.sentience = 0 # e+
        self.rot = 0 # q- i- a- e+
        self.arcana = 1 # unique
        self.holiness = 1 # e+ a+
        self.eaten = 0 # i-
        self.element = 0 # e+
        self.atomicnumber = 1 # i-
        self.luck = 1 # e+ a+ i+
        self.filesize = 1 # a+

class Appliance:
    def __init__(self, name, statEffects:{}):
        self.name = name
        self.statEffects = statEffects

    def applianceUsed(self, ingredient: Ingredient):
        for stat, change in self.statEffects.items():
            print(f"{self.name} used to increase {stat} by {change}")
            setattr(ingredient, stat, getattr(ingredient, stat) + change[0])
            setattr(ingredient, stat, getattr(ingredient, stat) * change[1])
            print(f"{stat} increased to {getattr(ingredient, stat)}")
        return ingredient

class Dish:
    def __init__(self):
        self.name = None
        self.mainIngredient = None
        self.quality = 0
        self.integrity = 0
        self.artistry = 0
        self.enchantment = 0

    def __str__(self):
        return f"{self.name} \n {self.quality} \n {self.integrity} \n {self.artistry} \n {self.enchantment} \n \n \n"

    def determineMainIngredient(self, ingredientList: list[Ingredient]):
        self.mainIngredient = random.choice(ingredientList)

    def determineName(self):
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
        self.quality += ingredient.quality + ingredient.sweet + ingredient.salt + abs(ingredient.temperature) - ingredient.rot
        self.integrity += ingredient.luck + ingredient.size - ingredient.blendability - ingredient.liquidity - ingredient.eaten - ingredient.rot - ingredient.atomicnumber
        self.artistry += ingredient.sweet + ingredient.size - ingredient.rot + ingredient.holiness + ingredient.luck + ingredient.filesize
        self.enchantment += ingredient.arcana + ingredient.luck + ingredient.element + ingredient.salt + ingredient.rot + ingredient.sentience + ingredient.holiness

class Kitchen:
    def __init__(self, name):
        self.name = name
        # Temporary Appliance Hardcode
        self.appliances = [Appliance("Microwave", {"temperature": (2, 5)}), Appliance("Fridge", {"temperature": (-5, -1.2)}), Appliance("Blender", {"filesize": (-10, 0), "liquidity": (10, 2)}), Appliance("Cutting Board", {"size": (-10, 0)})]
        self.ingredients = []

    def addIngredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def clearIngredient(self):
        self.ingredients = []

    def createDish(self):
        dish = Dish()
        for ingredient in self.ingredients:
            dish.addIngredient(ingredient)

        dish.determineMainIngredient(self.ingredients)
        dish.determineName()
        return dish

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

    def setHome(self, homeaway):
        self.isHome = homeaway

    def setTeamName(self, teamName):
        self.teamName = teamName

    def addToInventory(self, ingredient: Ingredient):
        self.inventory.append(ingredient)

    def chooseAppliance(self, kitchen: Kitchen):
        appliance = random.choice(kitchen.appliances)
        ingredientNum = random.randint(0, len(kitchen.ingredients)-1)
        kitchen.ingredients[ingredientNum] = appliance.applianceUsed(kitchen.ingredients[ingredientNum])

class Arena:
    def __init__(self, name):
        self.name = name
        # Arena Stats

class Team:
    def __init__(self, name, arena: Arena):
        self.name = name
        self.chefs = []
        self.runners = []
        self.arena = arena
        self.kitchen = Kitchen("Yo mama")
        self.activeChef = None

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

    def rotateChef(self):
        if self.activeChef is None:
            self.activeChef = self.chefs[0]
        else:
            self.chefs.append(self.chefs.pop(0))
            self.activeChef = self.chefs[0]

class PlayingTeam(Team):
    def __init__(self, name, arena: Arena):
        super().__init__(name, arena)
        self.ingredients = []
        self.currentChef = 0
        self.dishes = []

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
        self.homedishes = []
        self.awaydishes = []

        for player in home.runners + home.chefs:
            player.isHome = True
        for player in away.runners + away.chefs:
            player.isHome = False

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
                if runner.isHome:
                    for ingredient in runner.inventory:
                        self.home.kitchen.ingredients.append(ingredient)
                else:
                    for ingredient in runner.inventory:
                        self.away.kitchen.ingredients.append(ingredient)
                runner.inventory = []
                pile_runners.pop(runner)
            cowards = []
            print(list(pile_runners.items()))
            #if pile_runners empty, stop while loop
            if len(pile_runners) == 0:
                self.phase = "Cooking"
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
        actionsLeft = 20
        while actionsLeft > 0:
            actionsLeft -= 1
            self.home.activeChef.chooseAppliance(self.home.kitchen)
            self.away.activeChef.chooseAppliance(self.away.kitchen)
        self.homedishes.append(self.home.kitchen.createDish())
        self.awaydishes.append(self.away.kitchen.createDish())
        if len(self.homedishes) == 3:
            for dish in self.homedishes:
                print(dish)
            for dish in self.awaydishes:
                print(dish)
            self.phase = "Judging"
        else:
            self.phase = "Preparation"

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
        team2.addChef(player)

    for x in range(7):
        player = Player()
        player.setTeamName(team2.name)
        team2.addRunner(player)

    team1.rotateChef()
    team2.rotateChef()

    match = Match(team1, team2)

    while match.phase != "Judging":
        match.step()




if __name__ == "__main__":
    main()