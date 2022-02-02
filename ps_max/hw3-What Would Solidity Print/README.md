
# HW3 - What Would Solidity Print?

Written by Jenny Cong, Edited by Minxing Chen and Simon Guo.



### `CoinFlip` Solidity Smart Contract Code

![CoinFlip](./coinflip.png)



### Set Up

Assume there is a `print()` function in Solidity that takes in any variable and prints a human-readable representation of the variable without quotes regardless of public/private access.

Assume gas is zero. Currently, Tim has 10 ether. Matt has 10 ether. Minxing has 10 ether.



### What Would Solidity Print?

Consider the following questions happening in a single environment, meaning, question 2 happened after the action of question 1 has taken place.

**Question 1**

Tim’s address is `0xd95e068a69045ece32eecad394d86a9ac7b832ca`.

Tim hashed `abi.encodePacked(true, “12345678")` with keccak256 and got `“c844hfksjc9didvnrrmf4hdusjznryfu”` (Don’t worry if you don’t understand this part.)

Tim called `constructor(“c844hfksjc9didvnrrmf4hdusjznryfu”)` with a value of 1 ether.

You called `print(player1)`.

What would Solidity print?

ANSWER: Solidity would print 0xd95e068a69045ece32eecad394d86a9ac7b832ca (Tim's Address)


**Question 2**

Minxing’s address is `0x4d6dd6a6471123dd54f45088c991a5aac0c9ef01`.

Minxing called `takeBet(true)` with a value of 2 ether.

You called `print(player2)`.

What would Solidity print?

ANSWER: Solidity will print 0 as it would throw an error at the assertion (line 30)
and takeBet function will stop at that moment before assigning Minxing's
address to player2 variable.


**Question 3**

Matt’s address is `0xbbab9d85b4eca79ec9f0e4595681f3a025b5e3f6`.

Matt called `takeBet(false)` with a value of 1 ether.

You called `print(player2)`.

What would Solidity print?

ANSWER: Solidity will print '0xbbab9d85b4eca79ec9f0e4595681f3a025b5e3f6' (Matt's Address)


**Question 4**

Tim called `reveal(true, “12345678”)`.

What is Matt's ether balance now?

Matt's ether balance is 9 eth now since he lost a bet because he guessed false
while


**Question 5**

What is Tim's ether balance now?

Tim's balance is 11 eth now since Matt haven't correctly guessed Tim's initial
choice and therefore lost the bet. 

**NOTE**: The assertion and initializing commitment in the first place can be
thought of as a password that player1 sets so that only he can activate the
reveal function. Otherwise player2 can activate it with the same choice value
and win the bet without risk. And also this protects player1's choice from
being seen on the blockchain since he stores his choice encrypted initially
as player1Commitment. If the player1 tries to change his choice after seeing
player2's choice he wouldn't be able to do that due to assertion on line 42.

Also note that claimTimeout() can be called by anyone including player2 in case
the player1 sees choice of player2 (since ethereum is public blockchain and
all variables are publicly visible on it) and decides not to activate reveal
function. Therefore, after a set timeout player2 can claimTimeout() and get
all funds deposited in the contract returned to his address. Also note that
player1 can't overwrite player2's bet due to assertion player2 == 0 in takeBet.
In other words, after player2 enters the bet, contract only works between two of
them. However, new contracts can be created by calling the constructor function.


### Check Off

Submit the quiz on [Google form](https://docs.google.com/forms/d/e/1FAIpQLScFLnEo71COZ8mTXL5ZCMTAuzZDHNbTRWivbGE4lnkFkCdAoA/closedform).
