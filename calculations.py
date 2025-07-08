import math

def calculate_respect(
    target_level: int,
    fair_fight: float = 1.0,
    war: float = 1.0,
    kill: float = 1.0,
    overseas: float = 1.0,
    group: float = 1.0,
    retaliation: float = 1.0,
    hit_number: int = 1,
    milestone_bonus: bool = False
) -> float:
    """
    Returns respect for a given hit.
    If milestone_bonus is True, returns flat respect = hit_number.
    Else, calculates normally.
    """
    if milestone_bonus:
        return float(hit_number)  # flat bonus, ignores everything else

    # base respect
    base = round((target_level / 200) + 1, 2)

    # chain scale
    chain_mult = 0.25 * math.log10(hit_number) + 0.75 if hit_number >= 10 else 1.0

    return round(base * fair_fight * war * kill * overseas * group * retaliation * chain_mult, 2)


scenarios = [
    # Regular hit, level 100, no multipliers
    calculate_respect(100, hit_number=1),
    # Fair fight only
    calculate_respect(100, fair_fight=3.0, hit_number=1),
    # Level up (regular hit)
    calculate_respect(100, hit_number=1),  # vs level 50
    calculate_respect(50, hit_number=1),
    # Chain scaling at hit 1000
    calculate_respect(100, fair_fight=3.0, hit_number=1000),
    # Milestone bonus: 100th hit
    calculate_respect(100, hit_number=100, milestone_bonus=True),
]

print(scenarios)
