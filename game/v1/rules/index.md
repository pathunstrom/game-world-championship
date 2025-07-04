# The Rules

A game is a battle between two characters.
Each player brings a character and a deck to play.
The object of the game is to remove every card from your opponent's deck.

## Setup

1. Place your character in the center of your play space and the deck to one side.
2. Draw initial hand and decide if you would like to mulligan.
3. A mulligan is performed by selecting any number of cards in your hand
   and putting them on the bottom of your deck then drawing that many cards.
4. Choose the active player. Active player plays first on a round and switches every round.

You're ready to play.

## Concepts

### Dealing Damage

When a player is dealt damage, that player is considered the Blocking Player.
The player that caused the damage is considered the Attacking Player.

Follow the following steps:

1. Flip the top card of their deck into their discard pile.
2. The Attacking Player may play reactions "When an opponent reveals a card for damage."
3. That Blocking Player may play reactions "When you reveal a card for damage."
4. Reduce damage by the combination of the base Defense value + your character defense value + any bonus defense.
5. If the defense icons exactly match the remaining damage, put the card in your hand. (Perfect Defense)
6. If the defense card has a defense trigger, resolve it now.
7. Discard the card as damage.
8. If you have damage remaining, return to 1.

You are done once there is no more damage to take.

### Paying Energy

To pay an energy cost, put cards from the top of your energy pile onto the bottom of your deck.
If you do not have enough energy cards to pay the cost, you may not pay the cost.

### Characters

A character represents the player. Each character has:

* An effect: either a Reaction, Attack, Action, or Ongoing.
* A power rating: This is the amount of energy you gain during the Ready Step.
* A Character Damage Bonus: An amount of damage that is added to all attacks as a Character Bonus
* A Character Defense Bonus: An amount of defense added to each life card.  (Feels powerful, might need to be "per 
  attack")

Character abilities may only be used once per round.

### Definitions

* Action: Takes a turn during the combat step.
* Attack: A card that can be played as an action. Deals damage, may have a one time effect.
* Defense: An effect that activates before a card is discarded as damage.
* Drill: A card played during the training phase. Provides an Ongoing, Reaction, or Attack that can be used on 
  future turns.
* Ongoing: An effect that lasts. Will tell you when it ends.
* Reaction: Responds to a specific event. Has one time use effect.
* Tactic: A card that can be played as an action. Has a one time effect and is discarded.

## Round Structure

A round is broken into 3 steps:

1. Ready
2. Combat
3. Training
4. End of Round

### Ready Step

Right now, the only thing to do here is power up and draw.
We'll formalize how much energy later.
Also character levels are a future concern,
as well as "at the start of turn" effects.

1. Draw two cards.
2. Power up by putting 3 cards + 1 card per drill from the top of your deck into your energy pile
3. Perform "At start of turn" abilities

### Combat Step

In the combat step you will set yourself up and attack your opponent.
Starting with the active player, take turns performing one action.
When both players pass in succession, the combat step ends.

The possible actions to perform:

1. Attack Card - Play an attack card from your hand and resolve it.
2. Tactic Card - Play a tactic card from your hand and resolve it.
3. Drill Attack - Activate an action drill in play.
4. Drill Action - Activate an attack drill in play.
5. Character Action - Play an action printed on your character card.
6. Character Attack - Play an attack printed on your character card.
7. Pass - Pass your turn.

#### Perform an attack

No matter what kind of attack it is, you follow these steps:

1. Pay its costs. (Energy from your energy pool, cards from your hand, life cards from the top of your deck.)
2. You may activate a reaction. (When you)
3. Your opponent may activate a reaction. (When your opponent)
4. If the card has an effect, do what it says.
5. Deal damage equal to the base damage of the attack + your character attack bonus + any additional bonus damage.

* Reactions phrases: "activate an attack", "activate an action"
* If this is a Character Attack: "activate a character attack", "activate a character action"
* If this is a Drill Attack: "activate a drill attack", "activate a drill action"
* If this is an Attack card: "plays a card"

#### Perform an action

You may perform either a drill action or a player action. Follow these steps:

1. Pay its costs. (Energy from your energy pool, cards from your hand, life cards from the top of your deck.)
2. You may activate a reaction. (When you)
3. Your opponent may activate a reaction. (When your opponent)
4. Perform its immediate effect.
5. If it has an ongoing effect it continues to affect play until its end trigger.

Reaction phrases:

* "activate an action"
* If this is a Character Action: "activate a character action"
* If this is a Drill Action: "activate a drill action"

#### Play a Tactic

You may play a tactic from your hand. Follow these steps:

1. Pay its costs. (Energy from your energy pool, cards from your hand, life cards from the top of your deck.)
2. You activate a reaction. (When you, When a player)
3. Your opponent may activate a reaction (When your opponent, when a player)
4. Perform its immediate effect.
5. If it has an ongoing effect it continues to affect play until its end trigger.

Reaction phrases:

* "activate an action"
* "activate a tactic"
* "plays a card"

#### Pass

You do nothing, your opponent takes their turn.
If your opponent attacks you, you do not need to pass on your next turn.
If both players pass in succession, combat is over.

Design note: We should definitely not create reactions to "when your opponent passes".

### Training Step

Starting with the active player, each player may play 1 Drill card from their hand.

#### Playing a drill

1. Pay its cost from your energy pool.
2. Put it into play behind your character. 

Types of drills:

Ongoing: Effects that last as long as they're in play.
Reaction: Discard the drill from play when you're told to get its affect.
Action: Pay the associated costs to activate the effect of the drill.
Attack: Pay the associated costs to perform an attack.

### End Step

1. Discard down to hand size.
2. End of round effects
3. The active player passes to the other player.
