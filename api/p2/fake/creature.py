from model.creature import Creature

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country='CN',area="Himalaya",
             description="Hirsute Himalya"
             ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch"
    ),
]
def get_all() -> list[Creature]:
    return _creatures

def get_on(name:str) -> Creature|None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

#the following are nonfunctional for now, so they just act like
#they work, without modifyng the actual fake _creature list

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(name: str):
    return None