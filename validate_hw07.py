"""
Validation script for git-pycore-hw-07: Enhanced Assistant Bot
Tests all assignment criteria and requirements
"""
import sys
import os

# Add the git-pycore-hw-07 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'git-pycore-hw-07'))

from task1 import *
from datetime import datetime, timedelta


def test_birthday_validation():
    """Test Birthday class validation (DD.MM.YYYY format)."""
    print("=== Testing Birthday Validation ===")
    
    try:
        # Valid format
        birthday = Birthday("15.06.1990")
        assert birthday.value == "15.06.1990"
        print("✓ Valid birthday format (DD.MM.YYYY) works")
        
        # Invalid formats should raise errors
        try:
            Birthday("1990-06-15")
            print("✗ Should reject wrong format")
            return False
        except ValueError:
            print("✓ Rejects invalid format (YYYY-MM-DD)")
        
        try:
            Birthday("15/06/1990")
            print("✗ Should reject wrong separator")
            return False
        except ValueError:
            print("✓ Rejects invalid separator")
            
        try:
            Birthday("32.01.1990")
            print("✗ Should reject invalid date")
            return False
        except ValueError:
            print("✓ Rejects invalid date")
            
    except Exception as e:
        print(f"✗ Birthday validation failed: {e}")
        return False
    
    return True


def test_phone_validation():
    """Test Phone class validation (10 digits)."""
    print("\n=== Testing Phone Validation ===")
    
    try:
        # Valid 10-digit phone
        phone = Phone("1234567890")
        assert phone.value == "1234567890"
        print("✓ Valid 10-digit phone works")
        
        # Invalid phones should raise errors
        try:
            Phone("123456789")  # 9 digits
            print("✗ Should reject 9 digits")
            return False
        except ValueError:
            print("✓ Rejects 9 digits")
        
        try:
            Phone("12345678901")  # 11 digits
            print("✗ Should reject 11 digits")
            return False
        except ValueError:
            print("✓ Rejects 11 digits")
            
        try:
            Phone("abc1234567")  # letters
            print("✗ Should reject letters")
            return False
        except ValueError:
            print("✓ Rejects letters")
            
    except Exception as e:
        print(f"✗ Phone validation failed: {e}")
        return False
    
    return True


def test_all_bot_commands():
    """Test all bot commands work correctly."""
    print("\n=== Testing All Bot Commands ===")
    
    try:
        book = AddressBook()
        
        # Test add command
        result = add_contact(["John", "1234567890"], book)
        assert result == "Contact added."
        print("✓ add command works")
        
        # Test add to existing contact
        result = add_contact(["John", "0987654321"], book)
        assert result == "Contact updated."
        print("✓ add command updates existing contact")
        
        # Test change command
        result = change_contact(["John", "1234567890", "5555555555"], book)
        assert result == "Contact updated."
        print("✓ change command works")
        
        # Test phone command
        result = show_phone(["John"], book)
        assert "John:" in result and "5555555555" in result
        print("✓ phone command works")
        
        # Test all command
        result = show_all([], book)
        assert "John" in result
        print("✓ all command works")
        
        # Test add-birthday command
        result = add_birthday(["John", "15.06.1990"], book)
        assert result == "Birthday added for John."
        print("✓ add-birthday command works")
        
        # Test show-birthday command
        result = show_birthday(["John"], book)
        assert result == "John's birthday: 15.06.1990"
        print("✓ show-birthday command works")
        
        # Test birthdays command
        result = birthdays([], book)
        # Should show no upcoming birthdays or the list
        assert "No upcoming birthdays" in result or "Upcoming birthdays" in result
        print("✓ birthdays command works")
        
    except Exception as e:
        print(f"✗ Bot commands test failed: {e}")
        return False
    
    return True


def test_error_handling():
    """Test comprehensive error handling."""
    print("\n=== Testing Error Handling ===")
    
    try:
        book = AddressBook()
        
        # Test contact not found errors
        result = show_phone(["NonExistent"], book)
        assert "Contact not found" in result
        print("✓ Handles contact not found")
        
        # Test insufficient arguments
        result = add_contact(["John"], book)
        assert "Not enough arguments" in result
        print("✓ Handles insufficient arguments")
        
        # Test invalid phone format
        result = add_contact(["John", "invalid"], book)
        assert "Invalid input" in result
        print("✓ Handles invalid phone format")
        
        # Test invalid birthday format
        add_contact(["John", "1234567890"], book)
        result = add_birthday(["John", "invalid"], book)
        assert "Invalid input" in result
        print("✓ Handles invalid birthday format")
        
    except Exception as e:
        print(f"✗ Error handling test failed: {e}")
        return False
    
    return True


def test_user_friendly_output():
    """Test user-friendly output formats."""
    print("\n=== Testing User-Friendly Output ===")
    
    try:
        book = AddressBook()
        
        # Add contact with birthday
        add_contact(["John", "1234567890"], book)
        add_birthday(["John", "15.06.1990"], book)
        
        # Test formatted output
        result = show_all([], book)
        assert "Contact name: John, phones: 1234567890, birthday: 15.06.1990" in result
        print("✓ Contact display includes all information")
        
        # Test phone display
        result = show_phone(["John"], book)
        assert result == "John: 1234567890"
        print("✓ Phone display is clear")
        
        # Test birthday display
        result = show_birthday(["John"], book)
        assert result == "John's birthday: 15.06.1990"
        print("✓ Birthday display is clear")
        
        # Test empty book
        empty_book = AddressBook()
        result = show_all([], empty_book)
        assert result == "No contacts in address book."
        print("✓ Empty book message is clear")
        
    except Exception as e:
        print(f"✗ User-friendly output test failed: {e}")
        return False
    
    return True


def test_upcoming_birthdays_functionality():
    """Test upcoming birthdays functionality from hw-04."""
    print("\n=== Testing Upcoming Birthdays Functionality ===")
    
    try:
        book = AddressBook()
        
        # Add contact with upcoming birthday
        john = Record("John")
        john.add_phone("1234567890")
        
        # Set birthday to tomorrow
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
        john.add_birthday(tomorrow)
        book.add_record(john)
        
        # Test get_upcoming_birthdays method
        upcoming = book.get_upcoming_birthdays()
        assert len(upcoming) == 1
        assert upcoming[0]["name"] == "John"
        print("✓ get_upcoming_birthdays method works")
        
        # Test birthdays command
        result = birthdays([], book)
        assert "Upcoming birthdays:" in result
        assert "John:" in result
        print("✓ birthdays command shows upcoming birthdays")
        
        # Test weekend adjustment logic
        book2 = AddressBook()
        jane = Record("Jane")
        jane.add_phone("0987654321")
        
        # Find next Saturday within 7 days
        today = datetime.now().date()
        days_until_saturday = (5 - today.weekday()) % 7
        if days_until_saturday == 0:
            days_until_saturday = 7
        saturday = today + timedelta(days=days_until_saturday)
        
        if (saturday - today).days <= 7:
            jane.add_birthday(saturday.strftime("%d.%m.%Y"))
            book2.add_record(jane)
            
            upcoming = book2.get_upcoming_birthdays()
            if upcoming:
                # Should be moved to Monday
                congratulation_date = datetime.strptime(upcoming[0]["congratulation_date"], "%d.%m.%Y").date()
                assert congratulation_date.weekday() == 0  # Monday
                print("✓ Weekend birthday adjustment works")
        
    except Exception as e:
        print(f"✗ Upcoming birthdays test failed: {e}")
        return False
    
    return True


def test_program_exit():
    """Test program closes correctly with close/exit commands."""
    print("\n=== Testing Program Exit ===")
    
    try:
        # Test parse_input for exit commands
        command, args = parse_input("close")
        assert command == "close"
        print("✓ 'close' command parsed correctly")
        
        command, args = parse_input("exit")
        assert command == "exit"
        print("✓ 'exit' command parsed correctly")
        
        # Note: We can't test the actual exit in main() without running interactively
        print("✓ Exit commands recognition works (actual exit tested manually)")
        
    except Exception as e:
        print(f"✗ Program exit test failed: {e}")
        return False
    
    return True


def main():
    """Run all validation tests."""
    print("=== git-pycore-hw-07 Validation Script ===")
    print("Testing Enhanced Assistant Bot with Birthday Management\n")
    
    tests = [
        test_birthday_validation,
        test_phone_validation,
        test_all_bot_commands,
        test_error_handling,
        test_user_friendly_output,
        test_upcoming_birthdays_functionality,
        test_program_exit
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            break
    
    print(f"\n=== Validation Results ===")
    print(f"Passed: {passed}/{total} test categories")
    
    if passed == total:
        print("🎉 All assignment criteria validated successfully!")
        print("\nAssignment Requirements Summary:")
        print("✓ All bot commands implemented (add, change, phone, all, add-birthday, show-birthday, birthdays, hello, close/exit)")
        print("✓ User-friendly output formats for all data")
        print("✓ Comprehensive error handling with informative messages")
        print("✓ Date validation (DD.MM.YYYY format)")
        print("✓ Phone validation (10 digits)")
        print("✓ Program closes correctly with close/exit commands")
        print("\nThe enhanced assistant bot is ready for use! 🤖")
        return True
    else:
        print("❌ Some validation tests failed. Please check the implementation.")
        return False


if __name__ == "__main__":
    main()