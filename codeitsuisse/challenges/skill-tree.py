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
        elif s["require"] in [a['name'] for a in newSkills]:
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
            for poss in include:
                if newSkills[index]["require"] == None or newSkills[index]["require"] in poss[0]:
                    ll = poss[0][:]
                    ll.append(newSkills[index]["name"])
                    score = poss[1] + newSkills[index]["points"]
                    res.append([ll, score])

        if exclude != -1:
            res = res + exclude

        #def near(s, mini):
        #    if s[1] > (mini * 1.3) and s[1] > (mini + 10):
        #        return False
        #    return True

        #res = [s for s in res if near(s, min(res, key=lambda x: x[1])[1])]
        if len(res) != 0:
            dp_table[(index, target)] = res
            return dp_table[(index, target)]
        else:
            dp_table[(index, target)] = -1
            return dp_table[(index, target)]




    poss = []
    target = boss["offense"]
    for t in range(target, target*2):
        res = getMinPointSet(len(newSkills) - 1, t)
        if res != -1:
            poss += res
    return min(poss, key=lambda r: r[1])[0]

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
    },
    {'boss': {'offense': 210}, 'skills': [{'name': 'skill-22', 'offense': 13, 'points': 14, 'require': 'skill-21'}, {'name': 'skill-50', 'offense': 14, 'points': 12, 'require': 'skill-49'}, {'name': 'skill-51', 'offense': 18, 'points': 13, 'require': 'skill-50'}, {'name': 'skill-49', 'offense': 10, 'points': 11, 'require': 'skill-48'}, {'name': 'skill-38', 'offense': 112, 'points': 24, 'require': 'skill-37'}, {'name': 'skill-52', 'offense': 22, 'points': 14, 'require': 'skill-51'}, {'name': 'skill-34', 'offense': 78, 'points': 23, 'require': 'skill-33'}, {'name': 'skill-36', 'offense': 94, 'points': 24, 'require': 'skill-35'}, {'name': 'skill-19', 'offense': 6, 'points': 8, 'require': 'skill-18'}, {'name': 'skill-27', 'offense': 33, 'points': 19, 'require': 'skill-26'}, {'name': 'skill-56', 'offense': 46, 'points': 17, 'require': 'skill-55'}, {'name': 'skill-26', 'offense': 28, 'points': 18, 'require': 'skill-25'}, {'name': 'skill-2', 'offense': 6, 'points': 8, 'require': 'skill-1'}, {'name': 'skill-44', 'offense': 175, 'points': 26, 'require': 'skill-43'}, {'name': 'skill-24', 'offense': 20, 'points': 16, 'require': 'skill-23'}, {'name': 'skill-6', 'offense': 17, 'points': 15, 'require': 'skill-5'}, {'name': 'skill-16', 'offense': 48, 'points': 24, 'require': 'skill-15'}, {'name': 'skill-29', 'offense': 44, 'points': 20, 'require': 'skill-28'}, {'name': 'skill-42', 'offense': 153, 'points': 26, 'require': 'skill-41'}, {'name': 'skill-4', 'offense': 11, 'points': 12, 'require': 'skill-3'}, {'name': 'skill-18', 'offense': 4, 'points': 5, 'require': None}, {'name': 'skill-32', 'offense': 63, 'points': 22, 'require': 'skill-31'}, {'name': 'skill-15', 'offense': 45, 'points': 23, 'require': 'skill-14'}, {'name': 'skill-48', 'offense': 8, 'points': 10, 'require': 'skill-47'}, {'name': 'skill-23', 'offense': 16, 'points': 15, 'require': 'skill-22'}, {'name': 'skill-8', 'offense': 23, 'points': 18, 'require': 'skill-7'}, {'name': 'skill-7', 'offense': 20, 'points': 17, 'require': 'skill-6'}, {'name': 'skill-5', 'offense': 14, 'points': 14, 'require': 'skill-4'}, {'name': 'skill-10', 'offense': 29, 'points': 20, 'require': 'skill-9'}, {'name': 'skill-45', 'offense': 2, 'points': 3, 'require': None}, {'name': 'skill-3', 'offense': 8, 'points': 10, 'require': 'skill-2'}, {'name': 'skill-28', 'offense': 38, 'points': 19, 'require': 'skill-27'}, {'name': 'skill-35', 'offense': 86, 'points': 23, 'require': 'skill-34'}, {'name': 'skill-9', 'offense': 26, 'points': 19, 'require': 'skill-8'}, {'name': 'skill-20', 'offense': 8, 'points': 10, 'require': 'skill-19'}, {'name': 'skill-17', 'offense': 51, 'points': 24, 'require': 'skill-16'}, {'name': 'skill-54', 'offense': 33, 'points': 16, 'require': 'skill-53'}, {'name': 'skill-37', 'offense': 103, 'points': 24, 'require': 'skill-36'}, {'name': 'skill-41', 'offense': 142, 'points': 25, 'require': 'skill-40'}, {'name': 'skill-47', 'offense': 5, 'points': 8, 'require': 'skill-46'}, {'name': 'skill-14', 'offense': 41, 'points': 22, 'require': 'skill-13'}, {'name': 'skill-21', 'offense': 10, 'points': 12, 'require': 'skill-20'}, {'name': 'skill-1', 'offense': 3, 'points': 4, 'require': None}, {'name': 'skill-40', 'offense': 132, 'points': 25, 'require': 'skill-39'}, {'name': 'skill-33', 'offense': 70, 'points': 22, 'require': 'skill-32'}, {'name': 'skill-53', 'offense': 28, 'points': 15, 'require': 'skill-52'}, {'name': 'skill-31', 'offense': 56, 'points': 21, 'require': 'skill-30'}, {'name': 'skill-30', 'offense': 50, 'points': 21, 'require': 'skill-29'}, {'name': 'skill-55', 'offense': 39, 'points': 16, 'require': 'skill-54'}, {'name': 'skill-46', 'offense': 3, 'points': 6, 'require': 'skill-45'}, {'name': 'skill-12', 'offense': 35, 'points': 21, 'require': 'skill-11'}, {'name': 'skill-39', 'offense': 122, 'points': 25, 'require': 'skill-38'}, {'name': 'skill-25', 'offense': 24, 'points': 17, 'require': 'skill-24'}, {'name': 'skill-57', 'offense': 54, 'points': 17, 'require': 'skill-56'}, {'name': 'skill-43', 'offense': 164, 'points': 26, 'require': 'skill-42'}, {'name': 'skill-13', 'offense': 38, 'points': 22, 'require': 'skill-12'}, {'name': 'skill-11', 'offense': 32, 'points': 20, 'require': 'skill-10'}]},
    {"boss": {"offense": 145}, "skills": [{"name": "skill-93", "offense": 315, "points": 24, "require": "skill-92"}, {"name": "skill-55", "offense": 175, "points": 26, "require": "skill-54"}, {"name": "skill-73", "offense": 54, "points": 17, "require": "skill-72"}, {"name": "skill-47", "offense": 94, "points": 24, "require": "skill-46"}, {"name": "skill-58", "offense": 212, "points": 27, "require": "skill-57"}, {"name": "skill-17", "offense": 51, "points": 24, "require": "skill-16"}, {"name": "skill-43", "offense": 63, "points": 22, "require": "skill-42"}, {"name": "skill-59", "offense": 225, "points": 27, "require": "skill-58"}, {"name": "skill-49", "offense": 112, "points": 24, "require": "skill-48"}, {"name": "skill-52", "offense": 142, "points": 25, "require": "skill-51"}, {"name": "skill-14", "offense": 41, "points": 22, "require": "skill-13"}, {"name": "skill-94", "offense": 334, "points": 24, "require": "skill-93"}, {"name": "skill-2", "offense": 6, "points": 8, "require": "skill-1"}, {"name": "skill-77", "offense": 88, "points": 19, "require": "skill-76"}, {"name": "skill-99", "offense": 436, "points": 25, "require": "skill-98"}, {"name": "skill-79", "offense": 109, "points": 20, "require": "skill-78"}, {"name": "skill-44", "offense": 70, "points": 22, "require": "skill-43"}, {"name": "skill-80", "offense": 120, "points": 20, "require": "skill-79"}, {"name": "skill-96", "offense": 373, "points": 25, "require": "skill-95"}, {"name": "skill-81", "offense": 132, "points": 21, "require": "skill-80"}, {"name": "skill-26", "offense": 84, "points": 28, "require": "skill-25"}, {"name": "skill-33", "offense": 13, "points": 14, "require": "skill-32"}, {"name": "skill-25", "offense": 80, "points": 27, "require": "skill-24"}, {"name": "skill-78", "offense": 98, "points": 20, "require": "skill-77"}, {"name": "skill-89", "offense": 245, "points": 23, "require": "skill-88"}, {"name": "skill-11", "offense": 32, "points": 20, "require": "skill-10"}, {"name": "skill-22", "offense": 69, "points": 26, "require": "skill-21"}, {"name": "skill-39", "offense": 38, "points": 19, "require": "skill-38"}, {"name": "skill-6", "offense": 17, "points": 15, "require": "skill-5"}, {"name": "skill-56", "offense": 187, "points": 27, "require": "skill-55"}, {"name": "skill-37", "offense": 28, "points": 18, "require": "skill-36"}, {"name": "skill-61", "offense": 2, "points": 3, "require": None}, {"name": "skill-28", "offense": 92, "points": 28, "require": "skill-27"}, {"name": "skill-102", "offense": 504, "points": 26, "require": "skill-101"}, {"name": "skill-87", "offense": 214, "points": 23, "require": "skill-86"}, {"name": "skill-85", "offense": 184, "points": 22, "require": "skill-84"}, {"name": "skill-92", "offense": 297, "points": 24, "require": "skill-91"}, {"name": "skill-45", "offense": 78, "points": 23, "require": "skill-44"}, {"name": "skill-23", "offense": 73, "points": 27, "require": "skill-22"}, {"name": "skill-16", "offense": 48, "points": 24, "require": "skill-15"}, {"name": "skill-75", "offense": 70, "points": 18, "require": "skill-74"}, {"name": "skill-42", "offense": 56, "points": 21, "require": "skill-41"}, {"name": "skill-83", "offense": 157, "points": 21, "require": "skill-82"}, {"name": "skill-13", "offense": 38, "points": 22, "require": "skill-12"}, {"name": "skill-86", "offense": 199, "points": 22, "require": "skill-85"}, {"name": "skill-64", "offense": 8, "points": 10, "require": "skill-63"}, {"name": "skill-97", "offense": 394, "points": 25, "require": "skill-96"}, {"name": "skill-32", "offense": 10, "points": 12, "require": "skill-31"}, {"name": "skill-15", "offense": 45, "points": 23, "require": "skill-14"}, {"name": "skill-74", "offense": 61, "points": 18, "require": "skill-73"}, {"name": "skill-12", "offense": 35, "points": 21, "require": "skill-11"}, {"name": "skill-18", "offense": 55, "points": 25, "require": "skill-17"}, {"name": "skill-1", "offense": 3, "points": 4, "require": None}, {"name": "skill-30", "offense": 6, "points": 8, "require": "skill-29"}, {"name": "skill-91", "offense": 279, "points": 24, "require":"skill-90"}, {"name": "skill-3", "offense": 8, "points": 10, "require": "skill-2"}, {"name": "skill-84", "offense": 170, "points": 22, "require": "skill-83"}, {"name": "skill-68", "offense": 22, "points": 14, "require": "skill-67"}, {"name": "skill-7", "offense": 20, "points": 17, "require": "skill-6"}, {"name": "skill-51", "offense": 132, "points": 25, "require": "skill-50"}, {"name": "skill-19", "offense": 58, "points": 25, "require": "skill-18"}, {"name": "skill-98", "offense": 415, "points": 25, "require": "skill-97"}, {"name": "skill-20", "offense": 62, "points": 25, "require": "skill-19"}, {"name": "skill-67", "offense": 18, "points": 13, "require": "skill-66"}, {"name": "skill-100", "offense": 459, "points": 25, "require": "skill-99"}, {"name": "skill-65", "offense": 10, "points": 11, "require": "skill-64"}, {"name": "skill-40", "offense": 44, "points": 20, "require": "skill-39"}, {"name": "skill-50", "offense": 122, "points": 25, "require": "skill-49"}, {"name": "skill-71", "offense": 39, "points": 16, "require": "skill-70"}, {"name": "skill-24", "offense": 76, "points": 27, "require": "skill-23"}, {"name": "skill-53", "offense": 153, "points": 26, "require": "skill-52"}, {"name": "skill-63", "offense": 5, "points": 8, "require": "skill-62"}, {"name": "skill-38", "offense": 33, "points": 19, "require": "skill-37"}, {"name": "skill-82", "offense": 144, "points": 21, "require": "skill-81"}, {"name": "skill-90", "offense": 262, "points": 23, "require": "skill-89"}, {"name": "skill-48", "offense": 103, "points": 24, "require": "skill-47"}, {"name": "skill-9", "offense": 26, "points": 19, "require": "skill-8"}, {"name": "skill-69", "offense": 28, "points": 15, "require": "skill-68"}, {"name": "skill-54", "offense": 164, "points": 26, "require": "skill-53"}, {"name": "skill-4", "offense": 11, "points": 12, "require": "skill-3"}, {"name": "skill-31", "offense": 8, "points": 10, "require": "skill-30"}, {"name": "skill-103", "offense": 528, "points": 26, "require": "skill-102"}, {"name": "skill-36", "offense": 24, "points": 17, "require": "skill-35"}, {"name": "skill-41", "offense": 50, "points": 21, "require": "skill-40"}, {"name": "skill-29", "offense": 4, "points": 5, "require": None}, {"name": "skill-34", "offense": 16, "points": 15, "require": "skill-33"}, {"name": "skill-46", "offense": 86, "points": 23, "require": "skill-45"}, {"name": "skill-60", "offense": 239, "points": 28, "require": "skill-59"}, {"name": "skill-95", "offense": 353, "points": 24, "require": "skill-94"}, {"name": "skill-27", "offense": 88, "points": 28, "require": "skill-26"}, {"name": "skill-35", "offense": 20, "points": 16, "require": "skill-34"}, {"name": "skill-57", "offense": 199, "points": 27, "require": "skill-56"}, {"name": "skill-21", "offense": 65, "points": 26, "require": "skill-20"}, {"name": "skill-70", "offense": 33, "points": 16, "require": "skill-69"}, {"name": "skill-5", "offense": 14, "points": 14, "require": "skill-4"}, {"name": "skill-8", "offense": 23, "points": 18, "require": "skill-7"}, {"name": "skill-62", "offense": 3, "points": 6, "require": "skill-61"}, {"name": "skill-88", "offense": 229, "points": 23, "require": "skill-87"}, {"name": "skill-101", "offense": 481, "points": 26, "require": "skill-100"}, {"name": "skill-66", "offense": 14, "points": 12, "require": "skill-65"}, {"name": "skill-72", "offense": 46, "points": 17, "require": "skill-71"}, {"name": "skill-76", "offense": 79, "points": 19, "require": "skill-75"}, {"name": "skill-10", "offense": 29, "points": 20, "require": "skill-9"}]}
]
