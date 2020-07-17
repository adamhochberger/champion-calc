'''
TODO: Create structure diagram of champions->abilities->components and determine where objects are needed vs calculations

TODO: Change existing structure for champion to reflect this pattern
champion will be an object with the following attributes:
(string) name
(string) title
(image) portrait
(list/images) cosmetics
(boolean) shapeshifter/form-switching
(dictionary of int arrays) attributes
(list of ability objects) abilities
(list of item objects) items equipped
(list of rune objects) runes [could function like items] equipped

functions:

TODO: Implement calculation to find what an attribute is at a given level
double value_at_rank(int rank){};

TODO: Calculate mitigation based on given damage type
double get_mitigation(int damage_type){};

TODO: Implement damage mitigation formula with defenses + health
double calculate_damage(double raw_damage, champion target){};

TODO: Affect current health value by a given damage value (post-mitigation)
double take_damage(double damage){};

TODO: Change values based on incoming modifiers
double reduce_defense(int defense_type, string reduction_type, double value)


attributes are:
a type (can be a large dictionary with known stats) and a growth 
    calculating growth * level + base storing a [2] array will be better than a size [18] array of precomputed values (will verify during testing)
i.e. armor has base armor + armor growth + armor from items/other factors

TODO: Determine how characters current armor should be stored, this will allow for better usage of percentage reductions/additions etc

TODO: Change existing structure for ability to reflect this pattern
abilities will be an object with the following attributes:
(string) name
(string) description
(image) icon
(int) number (which ability for character)
(string) ability type (buff, damage, stim)
(string/int) damage type (magic, physical, true)
(int) on target cooldown
(array of double) base value, scaling values (can be stored as a [2] array)
    different damage types that can depend on different factors - can use flags to determine how it is calculated during execution
(array of double) current rank, max rank
(array of double) cooldown, scaling value
(array of double) cost, scaling value
(array of double) range, scaling range

functions:

TODO: Implement calculation to find what an ability's values are at a given level
(dictionary) value_at_rank(int rank){};

'''