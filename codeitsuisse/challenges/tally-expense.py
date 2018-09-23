import operator
def evaluate(data):
    persons = data.get("persons")
    expenses = data.get("expenses")
    nPerson = len(persons)
    pIndex = {}

    for i, p in enumerate(persons):
        pIndex[p] = i

    paid = [0 for _ in range(nPerson)]
    expenseOwe = []
    totalOwe = 0
    for e in expenses:
        split = nPerson
        if 'exclude' in e:
            split -= len(e['exclude'])
        o = e['amount'] / split
        expenseOwe.append(o)
        totalOwe += o
        paid[pIndex[e['paidBy']]] += e['amount']

    owe = [totalOwe for _ in range(nPerson)]

    for o, e in zip(expenseOwe,expenses):
        if 'exclude' in e:
            excludeIndex = [pIndex[x] for x in e['exclude']]
            for i in excludeIndex:
                owe[i] -= o

    minOIndex, minOwe = min(enumerate(owe), key=operator.itemgetter(1))
    minPIndex, minPaid = min(enumerate(paid), key=operator.itemgetter(1))
    maxPIndex, maxPaid = max(enumerate(paid), key=operator.itemgetter(1))

    minIsPaid = False
    minVal = minPaid
    if minOwe < minPaid:
        minIsPaid = False
        minVal = minOwe

    owe = [x - minVal for x in owe]
    paid = [x - minVal for x in paid]

    ans = []
    for i in range(nPerson):
        if i != maxPIndex:
            if owe[i] != 0:
                ans.append({"from": persons[i],
                            "to": persons[maxPIndex],
                            "amount": round(owe[i], 2)
                            })
            if paid[i] != 0:
                ans.append({"from": persons[maxPIndex],
                            "to": persons[i],
                            "amount": round(paid[i], 2)
                            })

    return {"transactions": ans}



tests = [
    {
            "name": "Jan Expense Report",
            "persons": ["Alice", "Bob", "Claire", "David"],
            "expenses": [
                        {
                                        "category": "Breakfast",
                                        "amount": 60,
                                        "paidBy": "Bob",
                                        "exclude": ["Claire","David"]
                                    },
                        {
                                        "category": "Phone Bill",
                                        "amount": 100,
                                        "paidBy": "Claire"
                                    },
                        {
                                        "category": "Groceries",
                                        "amount": 80,
                                        "paidBy": "David"
                                    },
                        {
                                        "category": "Petrol",
                                        "amount": 40,
                                        "paidBy": "David"
                                    }
                    ]
    },
    {"name": "testcase-28", "persons": ["M", "E", "P", "T", "R", "H", "Z", "A", "O"], "expenses": [{"category": "Electricity", "amount": 51, "paidBy": "T", "exclude": ["O", "R", "T", "H", "P", "A", "M"]}, {"category": "Groceries", "amount": 310.89, "paidBy": "M", "exclude": ["M", "H", "R", "P"]}, {"category": "Petrol", "amount": 0.046, "paidBy": "H", "exclude": ["Z", "R", "H", "A", "O", "E"]}, {"category": "Food", "amount": 189953.478, "paidBy": "Z", "exclude": ["Z", "E", "P", "R", "H"]}, {"category": "Food", "amount": 0.45, "paidBy": "Z", "exclude": ["O", "M", "R"]}, {"category": "Travel", "amount": 0.249, "paidBy": "H", "exclude": ["Z", "A", "P", "R"]}, {"category": "Water", "amount": 83, "paidBy": "H", "exclude": ["A", "E"]}, {"category": "Internet", "amount": 3328.1, "paidBy": "H", "exclude": ["O", "T", "A", "E", "P", "R"]}, {"category": "Food", "amount": 2.785, "paidBy": "A", "exclude": ["H", "A", "E", "O", "M", "R", "Z"]}, {"category": "Water", "amount": 286, "paidBy": "T", "exclude": ["T", "R", "P"]}, {"category": "Internet", "amount": 7028.182, "paidBy": "H", "exclude": ["M", "H", "E", "A", "O"]}, {"category": "Rent", "amount": 0.8, "paidBy": "M", "exclude": ["A", "T", "O", "H", "R", "P"]}, {"category": "Rent", "amount": 257584.625, "paidBy": "O", "exclude": ["R", "T", "Z", "O", "P", "M"]}, {"category": "Food", "amount": 350.48, "paidBy": "O", "exclude": ["R", "T", "O", "P", "Z", "H"]}]}

]
