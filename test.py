
# test.py
import pytest
from main import (
    read_data,
    get_female_names_capitalized,
    get_male_phone_info,
    get_occupations_starting_with_vowels,
    get_total_entries,
    get_all_countries,
    get_unique_occupations,
    get_first_entry_first_name,
    get_average_first_name_length,
    contains_peter,
    get_reversed_first_names
)

sample_data = [
    ["alice", "smith", "a", "Female", "Engineer", "+1-111-1111111", "USA"],
    ["bob", "jones", "b", "Male", "Artist", "+1-222-2222222", "UK"],
    ["irene", "white", "c", "Female", "Illustrator", "+1-333-3333333", "Canada"],
    ["john", "black", "d", "Male", "Technician", "+1-444-4444444", "Germany"],
    ["peter", "stone", "e", "Male", "Analyst", "+1-555-5555555", "France"]
]




def test_get_female_names_capitalized():
    assert get_female_names_capitalized(sample_data) == ['Alice', 'Irene']

def test_get_male_phone_info():
    assert get_male_phone_info(sample_data) == {
        'Bob': '+1-222-2222222',
        'John': '+1-444-4444444',
        'Peter': '+1-555-5555555'
    }

def test_get_occupations_starting_with_vowels():
    result = get_occupations_starting_with_vowels(sample_data)
    assert 'Artist' in result
    assert 'Illustrator' in result
    assert 'Engineer' in result
    assert 'Analyst' in result
    assert 'Technician' not in result

def test_get_total_entries():
    assert get_total_entries(sample_data) == 5

def test_get_all_countries():
    assert sorted(get_all_countries(sample_data)) == sorted(['USA', 'UK', 'Canada', 'Germany', 'France'])

def test_get_unique_occupations():
    assert get_unique_occupations(sample_data) == {'Engineer', 'Artist', 'Illustrator', 'Technician', 'Analyst'}

def test_get_first_entry_first_name():
    assert get_first_entry_first_name(sample_data) == 'alice'

def test_get_average_first_name_length():
    assert abs(get_average_first_name_length(sample_data) - 4.8) < 0.1

def test_contains_peter():
    assert contains_peter(sample_data) == True

def test_get_reversed_first_names():
    assert get_reversed_first_names(sample_data) == ['peter', 'john', 'irene', 'bob', 'alice']
