from advent_of_code.day5.filippo.solution import Map, combine_mappings


class TestMappingCombining:
    def test_second_mapping_contained_in_first_no_transformation(self):
        first = Map(start=4, end=8, delta=0)
        second = Map(start=5, end=7, delta=0)
        assert combine_mappings(first, second) == [
            Map(start=4, end=4, delta=0),
            Map(start=5, end=7, delta=0),
            Map(start=8, end=8, delta=0),
        ]

    def test_second_mapping_contained_in_first_with_transformation(self):
        first = Map(start=4, end=8, delta=10)
        second = Map(start=15, end=17, delta=0)
        assert combine_mappings(first, second) == [
            Map(start=4, end=4, delta=10),
            Map(start=15, end=17, delta=0),
            Map(start=8, end=8, delta=10),
        ]

    def test_second_mapping_no_intersection_with_first_no_transformation(self):
        first = Map(start=4, end=8, delta=0)
        second = Map(start=10, end=11, delta=0)
        assert combine_mappings(first, second) == [
            Map(start=4, end=8, delta=0),
            Map(start=10, end=11, delta=0),
        ]

    def test_second_mapping_no_intersection_with_transformation(self):
        first = Map(start=4, end=8, delta=1)
        second = Map(start=10, end=11, delta=0)
        assert combine_mappings(first, second) == [
            Map(start=4, end=8, delta=1),
            Map(start=10, end=11, delta=0),
        ]
