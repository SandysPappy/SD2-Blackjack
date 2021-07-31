class UnimplementedBetSpread(Exception):
    pass
class InvalidBettingUnit(ValueError):
    pass

def get_what_to_bet(betting_unit, bet_spread, min_bet_allowed, max_bet_allowed, true_count):
    if betting_unit < min_bet_allowed or betting_unit > max_bet_allowed:
        raise InvalidBettingUnit(f'Your unit of {betting_unit} is not withing the allowable range of {min_bet_allowed}-{max_bet_allowed}')

    list_of_spreads = ['1-8',]

    if bet_spread == '1-8':
        if true_count < 2:
            return betting_unit
        if true_count < 3:
            return 2*betting_unit
        if true_count < 4:
            return 3*betting_unit
        return 4*betting_unit

    raise UnimplementedBetSpread(f"Sorry, we've only implemented these bet spreads: {list_of_spreads}, you gave {bet_spread}")
