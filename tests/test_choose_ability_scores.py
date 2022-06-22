
import pytest

from game.choose_ability_scores import *

def test_create_entity():
    name = "Bob"
    ent = Entity(name)
    assert ent.name == name
    assert ent.ability_scores[Ability.str] == 0
