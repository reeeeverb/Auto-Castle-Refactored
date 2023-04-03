# Auto-Castle

## Chessboard TODO:
- Stalemate
- Timers
- Logs with PGN files

## Engine notes:

#### Evaulation
- Evalutation has 2 main methods 
  - hand-crafted
  - neural networks
    - only one really in use these days
    - start with this one 

#### Hand Crafted Evalution 
- **Negamax** is minimax but each side is capable of being scored

#### NN Evaluation 
- the hard part is ofc evalution, after that is just finding the largest value as fast as possible
  - prob using a MC algo bc its cool
- do a little *self play reinforcement learning*
  - I have no idea how to implement that although I suspect it will involve python


## What We Learned from Previous Implementation
- seperate the GUI from the backend
  - no shit
- do a more fn approach rather than OO
- complete generailty of methods
- all operations should be preformed on arrays and then passed to GUI
