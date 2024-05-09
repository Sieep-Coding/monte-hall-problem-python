## What is the Monty Hall Problem?
The Monty Hall problem is a famous probability puzzle named after the host of the television game show "Let's Make a Deal." 

### It goes like this:
Suppose you're on a game show and you're given the choice of three doors: 
- Behind one door is a car, and behind the other two doors are goats. 
- You pick a door, say Door 1, and the host, who knows what's behind the doors, opens another door, say Door 3, which has a goat. 
- He then asks you, "Do you want to switch your choice from Door 1 to Door 2?"

The question is: Should you switch doors or stick with your original choice?

### The Solution
Surprisingly, switching doors gives you a higher probability of winning the car. The probability of winning the car by switching is 2/3, while the probability of winning by sticking with your original choice is 1/3.

![](https://github.com/Sieep-Coding/monte-hall-problem-python/blob/main/images/bar.png)

#### Here's why:

- Initially, there are three doors, and the car is equally likely to be behind any one of them (1/3 probability for each door).

- When you initially pick a door, say Door 1, there's a 1/3 chance that you've picked the door with the car, and a 2/3 chance that the car is behind one of the other two doors.

- The host then opens one of the remaining two doors, say Door 3, which reveals a goat. 

- This doesn't change the probability of the car being behind your initial choice (Door 1) or the remaining unopened door (Door 2).

- Since there's a 2/3 chance that the car is behind the remaining unopened door (Door 2), switching doors gives you a 2/3 probability of winning the car.

![](https://github.com/Sieep-Coding/monte-hall-problem-python/blob/main/images/pie.png)
