from advent_of_code.day11.filippo.solution import (
    Galaxy,
    _parse_galaxies,
    _sum_shortest_distances,
    expand_universe,
    _calculate_expanded_input,
)


def test_distance_between_two_galaxies_is_sum_of_the_dist_between_their_coordinates():
    galaxy_1 = Galaxy(1, 1)
    galaxy_2 = Galaxy(2, 2)
    assert galaxy_1.distance(galaxy_2) == 2


def test_distance_with_example():
    galaxies = [
        Galaxy(4, 0),
        Galaxy(9, 1),
        Galaxy(0, 2),
        Galaxy(8, 5),
        Galaxy(1, 6),
        Galaxy(12, 7),
        Galaxy(9, 10),
        Galaxy(0, 11),
        Galaxy(5, 11),
    ]
    assert _sum_shortest_distances(galaxies) == 374


def test_parse_galaxies_with_example():
    expanded_input = [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#.......",
    ]
    assert _parse_galaxies(expanded_input) == [
        Galaxy(4, 0),
        Galaxy(9, 1),
        Galaxy(0, 2),
        Galaxy(8, 5),
        Galaxy(1, 6),
        Galaxy(12, 7),
        Galaxy(9, 10),
        Galaxy(0, 11),
        Galaxy(5, 11),
    ]


def test_no_galaxy_in_row():
    test_universe = ["........."]
    new_unviverse = expand_universe(test_universe)

    assert new_unviverse == [".........", "........."]


def test_universe_expansion():
    test_universe = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]

    expanded_input = _calculate_expanded_input(test_universe)
    assert expanded_input == [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#.......",
    ]
