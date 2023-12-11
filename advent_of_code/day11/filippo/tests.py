from advent_of_code.day11.filippo.solution import Galaxy, _sum_shortest_distances


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
