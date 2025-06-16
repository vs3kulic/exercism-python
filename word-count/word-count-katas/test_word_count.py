"""Test suite for word count kata."""
import sys
sys.path.append('..')  # Add parent directory to path

from word_count import count_words, _normalise_text

# Global tracking variables
TOTAL_TESTS = 0
PASSED_TESTS = 0
FAILED_TESTS = []
ALPHANUMERIC_CHARS = set('abcdefghijklmnopqrstuvwxyz0123456789 ')

def run_test(test_name, input_text, expected):
    """Helper function to run a single test and track results."""
    global TOTAL_TESTS, PASSED_TESTS, FAILED_TESTS
    
    TOTAL_TESTS += 1
    result = count_words(input_text)
    
    # ✨ Beautiful visual separator
    print(f"\n{'─' * 50}")
    print(f"🧪 Test #{TOTAL_TESTS}: {test_name}")
    print(f"{'─' * 50}")
    
    print(f"📝 Testing: {repr(input_text)}")
    words = _normalise_text(input_text)
    print(f"🔍 Extracted: {words}")
    
    if result != expected:
        print(f"🎯 Expected: {expected}")
        print(f"➡️ Got:      {result}")
        print(f"❌ {test_name} failed!")
        FAILED_TESTS.append(test_name)
        return False
    else:
        print(f"✅ {test_name} passed!")
        PASSED_TESTS += 1
        return True

def test_count_one_word():
    """Test single word counting."""
    run_test("Single word test", "word", {"word": 1})

def test_count_one_of_each_word():
    """Test multiple unique words."""
    run_test("Multiple unique words test", "one of each", {"one": 1, "of": 1, "each": 1})

def test_multiple_occurrences_of_a_word():
    """Test word repetition counting."""
    run_test("Word repetition test", "one fish two fish red fish blue fish",
             {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1})

def test_handles_cramped_lists():
    """Test comma separation."""
    run_test("Cramped list test", "one,two,three", {"one": 1, "two": 1, "three": 1})

def test_handles_expanded_lists():
    """Test newline separation."""
    run_test("Expanded list test", "one,\ntwo,\nthree", {"one": 1, "two": 1, "three": 1})

def test_ignore_punctuation():
    """Test punctuation handling."""
    input_text = "car: carpet as java: javascript!!&@$%^&"
    expected = {"car": 1, "carpet": 1, "as": 1, "java": 1, "javascript": 1}
    
    success = run_test("Punctuation test", input_text, expected)
    
    # Additional debugging for punctuation test
    if not success:
        unknown_chars = set(input_text) - ALPHANUMERIC_CHARS
        print(f"🚨 Unhandled characters: {unknown_chars}")

def test_include_numbers():
    """Test that numbers are treated as words."""
    run_test("Numbers test", "testing, 1, 2 testing", {"testing": 2, "1": 1, "2": 1})

def test_normalize_case():
    """Test case insensitivity."""
    run_test("Case normalization test", "go Go GO Stop stop", {"go": 3, "stop": 2})

def test_with_apostrophes():
    """Test complex apostrophe handling."""
    run_test("Apostrophes test", "'First: don't laugh. Then: don't cry. You're getting it.'",
             {"first": 1, "don't": 2, "laugh": 1, "then": 1, "cry": 1, "you're": 1, "getting": 1, "it": 1})

def test_with_quotations():
    """Test quotation vs apostrophe handling."""
    run_test("Quotations test", "Joe can't tell between 'large' and large.",
             {"joe": 1, "can't": 1, "tell": 1, "between": 1, "large": 2, "and": 1})

def test_quotation_for_word_with_apostrophe():
    """Test quoted contractions."""
    run_test("Quoted contractions test", "can, can't, 'can't'", {"can": 1, "can't": 2})

def test_multiple_spaces_not_detected_as_a_word():
    """Test multiple whitespace handling."""
    run_test("Multiple spaces test", " multiple   whitespaces", {"multiple": 1, "whitespaces": 1})

def test_non_alphanumeric():
    """Test underscore handling."""
    run_test("Non-alphanumeric test", "hey,my_spacebar_is_broken", 
             {"hey": 1, "my": 1, "spacebar": 1, "is": 1, "broken": 1})

def test_substrings_from_the_beginning():
    """Test substring recognition."""
    run_test("Substrings test", "Joe can't tell between app, apple and a.",
             {"joe": 1, "can't": 1, "tell": 1, "between": 1, "app": 1, "apple": 1, "and": 1, "a": 1})

def test_alternating_word_separators_not_detected_as_a_word():
    """Test complex separator patterns."""
    run_test("Alternating separators test", ",\n,one,\n ,two \n 'three'", 
             {"one": 1, "two": 1, "three": 1})

def test_tabs():
    """Test tab character handling."""
    run_test("Tabs test", "rah rah ah ah ah\troma roma ma\tga ga oh la la\twant your bad romance",
             {"rah": 2, "ah": 3, "roma": 2, "ma": 1, "ga": 2, "oh": 1, "la": 2, "want": 1, "your": 1, "bad": 1, "romance": 1})

def test_multiple_apostrophes_ignored():
    """Test multiple surrounding apostrophes."""
    run_test("Multiple apostrophes test", "''hey''", {"hey": 1})

def print_test_summary():
    """Print comprehensive test summary."""
    global TOTAL_TESTS, PASSED_TESTS, FAILED_TESTS
    
    failed_count = len(FAILED_TESTS)
    success_rate = (PASSED_TESTS / TOTAL_TESTS * 100) if TOTAL_TESTS > 0 else 0
    
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    # Overall Stats
    print(f"📈 Tests Performed:  {TOTAL_TESTS}")
    print(f"✅ Tests Passed:     {PASSED_TESTS}")
    print(f"❌ Tests Failed:     {failed_count}")
    print(f"📊 Success Rate:     {success_rate:.1f}%")
    print("-" * 60)


if __name__ == "__main__":
    print("=" * 50)
    print("🧪 WORD COUNT TEST SUITE")
    print("=" * 50)
    
    # Run all tests in order - clean and simple
    test_count_one_word()
    test_count_one_of_each_word()
    test_multiple_occurrences_of_a_word()
    test_handles_cramped_lists()
    test_handles_expanded_lists()
    test_ignore_punctuation()
    test_include_numbers()
    test_normalize_case()
    test_with_apostrophes()
    test_with_quotations()
    test_quotation_for_word_with_apostrophe()
    test_multiple_spaces_not_detected_as_a_word()
    test_non_alphanumeric()
    test_substrings_from_the_beginning()
    test_alternating_word_separators_not_detected_as_a_word()
    test_tabs()
    test_multiple_apostrophes_ignored()
    
    # Print comprehensive summary
    print_test_summary()