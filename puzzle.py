from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),         # A is either Knight or Knave
    Implication(AKnight, And(AKnight, AKnave)),             # If A is knight then the statement should be True
    Implication(AKnave, Not(And(AKnight, AKnave)))          # If A is knave then the statement should be False
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),         # A is either Knight or Knave
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),         # B is either Knight or Knave
    Implication(AKnight, And(AKnave, BKnave)),             # If A is knight then the statement should be True
    Implication(AKnave, Not(And(AKnave, BKnave)))          # If A is knave then the statement should be False
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),         # A is either Knight or Knave
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),         # B is either Knight or Knave
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnave, Biconditional(AKnight, BKnight)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),         # A is either Knight or Knave
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),         # B is either Knight or Knave
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),         # C is either Knight or Knave
    Implication(AKnight, And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))),
    Implication(AKnave, Not(And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))))),
    Implication(BKnight, 
    And(Implication(AKnight, AKnave), Implication(AKnave, AKnave))
    ),
    Implication(BKnave, 
    Not(And(Implication(AKnight, AKnave), Implication(AKnave, AKnave)))
    ),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
