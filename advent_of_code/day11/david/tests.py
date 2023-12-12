from advent_of_code.day11.david.solution import (
    Galaxy,
    _calculate_expanded_input,
    _parse_galaxies,
    _sum_shortest_distances,
    main_part_one,
    main_part_two,
    _parse_empty_rows,
    _parse_empty_cols,
    _parse_extended_galaxies,
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


def test_part_one():
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

    value = main_part_one(test_universe)

    assert value == 374


def test_empty_rows_and_cols():
    galaxies = [
        Galaxy(1, 0),
        Galaxy(3, 2),
    ]

    empty_rows = _parse_empty_rows(galaxies)
    empty_cols = _parse_empty_cols(galaxies)
    assert empty_rows == [0, 2]
    assert empty_cols == [1]


def test_empty_rows_and_cols():
    galaxies = [
        Galaxy(1, 0),
        Galaxy(3, 2),
    ]

    empty_rows = [0, 2]
    empty_cols = [1]

    new_galaxies = _parse_extended_galaxies(galaxies, empty_rows, empty_cols)
    assert new_galaxies == [
        Galaxy(1000000, 0),
        Galaxy(2000001, 1000001),
    ]
