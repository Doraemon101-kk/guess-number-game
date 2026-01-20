# 🎯 Number Guessing Game (Pro)

A terminal-based number guessing game with configurable range, input validation, and multi-round statistics.

## ✨ Features

- **Custom range**: Play with default (1–50) or set your own via command line  
- **Robust input handling**: Non-integers? Out-of-range? No problem — it asks again!  
- **Multi-round mode**: Play as many rounds as you like  
- **Game summary**: See your average guesses per round when you quit  
- **Clean code**: Modular design with separated logic and utilities  

## ▶️ How to Play

```bash
# Use default range (1 to 50)
python game.py

# Set custom range
python game.py 10 100
```

During the game:
- Enter an integer when prompted  
- Get feedback: *“Too small”*, *“Too big”*, or *“Bingo!”*  
- After each round, choose to play again or quit  
- On exit, see your performance summary  

## 💡 Example

```text
Please give a number between 1 and 50:
25
Too small
...
Bingo!
You played 4 times to guess it.
Play again? (Yes/No): No
You played 2 rounds, with an average of 3.5 guesses per round.
```

## 🛠 Built With

- Python 3.x  
- Standard library only (`sys`, `random`) — no external dependencies!

---

> Made for learning, fun, and clean coding practice.  
> Ready to run — no installation needed!

---
