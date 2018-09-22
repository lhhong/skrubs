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
                            "amount": owe[i]
                            })
            if paid[i] != 0:
                ans.append({"from": persons[maxPIndex],
                            "to": persons[i],
                            "amount": paid[i]
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
    }
]
