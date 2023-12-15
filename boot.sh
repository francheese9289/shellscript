#! /bin/bash

echo "Would you like to play a game of Rocks, Paper, Scissors with me?"

read answer

if [ $answer == "yes" ]
then
    python3 rocks_paper_scissors.py
else
    echo "That's too bad, maybe next time."
fi