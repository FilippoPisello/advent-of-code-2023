from advent_of_code.day5.filippo.solution import (
    Map,
    _convert_seeds_to_seed_ranges,
    main_part_one,
    main_part_two,
    map_number,
    parse_maps,
)


def test_if_maps_do_not_contain_number_then_return_number():
    map1 = Map(destination_start=10, source_start=0, length=2)
    assert map_number(10, [map1, map1]) == 10


def test_if_maps_contain_number_then_return_destination():
    map1 = Map(destination_start=50, source_start=98, length=2)
    assert map_number(98, [map1]) == 50
    assert map_number(99, [map1]) == 51


def test_mapped_number_is_returned_as_soon_as_matched():
    maps = [
        Map(destination_start=49, source_start=53, length=8),
        Map(destination_start=0, source_start=11, length=42),
        Map(destination_start=42, source_start=0, length=7),
        Map(destination_start=57, source_start=7, length=4),
    ]
    assert map_number(53, maps) == 49


def test_map_is_parsed_from_line():
    map1 = Map.from_line("50 98 2")
    assert map1.destination_start == 50
    assert map1.source_start == 98
    assert map1.length == 2


def test_maps_belonging_to_different_sections_are_divided_into_groups():
    maps = [
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
    ]
    parsed_maps = parse_maps(maps)
    assert len(parsed_maps) == 2
    assert len(parsed_maps[0]) == 2
    assert len(parsed_maps[1]) == 3


def test_example_part_one():
    problem_input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]
    assert main_part_one(problem_input) == 35


def test_seeds_are_converted_to_seed_range():
    seeds = [79, 14, 55, 13]
    expected = set(range(79, 79 + 14)) | set(range(55, 55 + 13))
    assert {x for x in _convert_seeds_to_seed_ranges(seeds)} == expected


def test_overlapping_seeds_are_converted_to_seed_range():
    seeds = [10, 2, 10, 2]
    assert sorted([x for x in _convert_seeds_to_seed_ranges(seeds)]) == [10, 11]


def test_example_part_two():
    problem_input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]
    assert main_part_two(problem_input) == 46
