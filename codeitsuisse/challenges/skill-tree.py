def evaluate(inputVal):
    skills = inputVal['skills']
    boss = inputVal['boss']

    level = 0
    skills_copy = skills[:]
    newSkills = []
    zeroOffense = []

    def operate(s):
        if s["require"] == None:
            newSkills.append(s)
            if s["offense"] == 0:
                zeroOffense.append(s)
            return False
        elif s["require"] in map(lambda s: s['name'], newSkills):
            newSkills.append(s)
            return False
        return True

    while len(skills_copy) > 0:
        skills_copy = [s for s in skills_copy if operate(s)]

    dp_table = {}

    def getMinPointSet(index, target):
        if (index, target) in dp_table:
            return dp_table[(index, target)]

        if target == 0:
            dp_table[(index, target)] = [[[], 0]]
            return dp_table[(index, target)]

        if index < 0 or target < 0:
            dp_table[(index, target)] = -1
            return dp_table[(index, target)]

        include = getMinPointSet(index-1, target - newSkills[index]["offense"])
        exclude = getMinPointSet(index-1, target)
        res = []
        if include != -1:
            canInclude = False
            for poss in include:
                if newSkills[index]["require"] == None or newSkills[index]["require"] in poss[0]:
                    canInclude = True
                    poss[0].append(newSkills[index]["name"])
                    poss[1] += newSkills[index]["points"]

            if canInclude:
                res = res + include
        if exclude != -1:
            res = res + exclude

        if len(res) != 0:
            dp_table[(index, target)] = res
            return dp_table[(index, target)]
        else:
            dp_table[(index, target)] = -1
            return dp_table[(index, target)]




    target = boss["offense"]
    while True:
        res = getMinPointSet(len(newSkills) - 1, target)
        print(res)
        if res != -1:
            return min(res, key=lambda r: r[1])[0]
        target += 1

tests = [
    {
          "boss":
            {
                      "name": "joker",
                      "offense": 11
                    }
          ,
          "skills": [
                  {
                            "name": "Grapple Gun",
                            "offense": 5,
                            "points": 1,
                            "require": None
                          },
                  {
                            "name": "Hacking Device",
                            "offense": 6,
                            "points": 2,
                            "require": "Grapple Gun"
                          },
                  {
                            "name": "Remote",
                            "offense": 7,
                            "points": 3,
                            "require": "Hacking Device"
                          },
                  {
                            "name": "Bomb",
                            "offense": 20,
                            "points": 5,
                            "require": "Remote"
                          },
                  {
                            "name": "Inverted takedown",
                            "offense": 5,
                            "points": 1,
                            "require": None
                          },
                  {
                            "name": "Shockwave attack",
                            "offense": 8,
                            "points": 3,
                            "require": "Inverted takedown"
                          }
                ]
    }
]
