import numpy as np

def evaluate(data):
    input = np.array(data["input"][0:3])
    output = np.array(data["output"][0:3])
    question = np.array(data["question"])
    x = np.linalg.solve(input, output)
    result = np.matmul(x, question)
    return {"answer": result}

    # print(result)
    # print(np.shape(input), np.shape(output))
    # print(input, output, x)


tests = [
{
  "input": [
    [1, 2, 3],
    [2, 3, 4],
    [2, 1, 4],
    [5, 3, 2],
    [2, 1, 2]
  ],
  "output": [
    6,
    9,
    7,
    10,
    5
   ],
  "question": [3, 4, 5]
}
]
