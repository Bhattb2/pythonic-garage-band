# Pythonic Garage Band
PR: https://github.com/Bhattb2/pythonic-garage-band/pull/3
## Exercise
Practice classes by making instances of bands and musicians

### Description
- Use Python classes to model a Band made up of different kinds of musicians.

- Start with Guitarist,Bassist, and Drummer.

- Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

## User Acceptance Tests
---
### Band Tests
- A Band instance should have a name attribute which is a string.
- A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
- A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
- A Band instance should have appropriate str and repr methods.
- A Band should have a class method to_list which returns a list of previously created Band instances
### Musician Subclass Tests
- Each kind of Musician instance should have appropriate str and repr methods.
- Each kind of Musician instance should have a get_instrument method that returns string.
- Each kind of Musician instance should have a play_solo method that returns string.
### Stretch
- A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance.

    - The Band instance should have its members be set to musicians based on info from the input.
    - The formatted data should be in a file
    - The exact formatting is up to you.


## Dependencies
---
- editorconfig
- gitattributes
- gitignore
