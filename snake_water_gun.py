import random

l = [[" ", "s", "w", "g"], ["s", "d", "w", "l"], ["w", "l", "d", "w"],
     ["g", "w", "l", "d"]]


def game():
  user_score = 0
  comp_score = 0
  draw = 0
  while True:
    user = input("s for snake, w for water and g for gun or q for quit:")
    if user == "q":
      print(
          f"user score={user_score} and computer score={comp_score} and draw={draw} and total played {user_score+comp_score+draw}"
      )
      break
    if user not in ["s", "w", "g"]:
      print("Invalid input")
      continue
    comp = random.choice(["s", "w", "g"])
    print(f"you choose {user} and computer choose {comp}")
    comp_index = ["", "s", "w", "g"]
    c_index = comp_index.index(f"{comp}")
    user_index = ["", "s", "w", "g"]
    u_index = user_index.index(f"{user}")
    result = l[c_index][u_index]
    if result == "w":
      user_score += 1
      print("you won")
    elif result == "l":
      comp_score += 1
      print("computer won")
    else:
      draw = draw + 1
      print("draw")


if __name__ == "__main__":
  game()
