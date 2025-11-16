"""
Validation script for git-pycore-hw-06
Tests exact workflow from assignment example
"""
import sys
import os

# Add the git-pycore-hw-06 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'git-pycore-hw-06'))

from task1 import AddressBook, Record


def test_exact_assignment_example():
    """Test the exact code example from assignment."""
    print("=== Testing Exact Assignment Example ===")
    
    # Створення нової адресної книги
    book = AddressBook()
    print("✓ Created new AddressBook")

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    print("✓ Created John record with two phones")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print("✓ Added John to address book")

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    print("✓ Created and added Jane to address book")

    # Виведення всіх записів у книзі
    print("\nAll records in book:")
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(f"\n✓ Edited John's phone. Result: {john}")

    # Пошук конкретного телефону в записі John
    found_phone = john.find_phone("5555555555")
    print(f"✓ Found John's phone: {john.name}: {found_phone}")

    # Видалення запису Jane
    book.delete("Jane")
    print("✓ Deleted Jane from address book")
    
    print(f"\nFinal address book state:")
    for name, record in book.data.items():
        print(record)
    
    print("\n=== All assignment requirements validated successfully! ===")


def validate_criteria():
    """Validate against specific assignment criteria."""
    print("\n=== Validating Assignment Criteria ===")
    
    # Test AddressBook methods
    book = AddressBook()
    record = Record("TestUser")
    
    # Criterion 1: AddressBook methods
    try:
        book.add_record(record)  # add_record method
        assert book.find("TestUser") == record  # find method
        book.delete("TestUser")  # delete method
        assert book.find("TestUser") is None
        print("✓ AddressBook: add_record, find, delete methods work correctly")
    except Exception as e:
        print(f"✗ AddressBook methods failed: {e}")
        return False
    
    # Criterion 2: Record class
    record = Record("TestUser")
    try:
        # Check Name storage
        assert hasattr(record, 'name')
        assert record.name.value == "TestUser"
        print("✓ Record: Name object stored in separate attribute")
        
        # Check Phone list storage
        assert hasattr(record, 'phones')
        assert isinstance(record.phones, list)
        print("✓ Record: Phone list stored in separate attribute")
        
        # Test phone methods
        record.add_phone("1234567890")  # add_phone
        assert len(record.phones) == 1
        
        found = record.find_phone("1234567890")  # find_phone
        assert found == "1234567890"
        
        record.edit_phone("1234567890", "9876543210")  # edit_phone
        assert record.find_phone("9876543210") == "9876543210"
        assert record.find_phone("1234567890") is None
        
        record.remove_phone("9876543210")  # remove_phone
        assert len(record.phones) == 0
        
        print("✓ Record: add_phone, remove_phone, edit_phone, find_phone methods work correctly")
    except Exception as e:
        print(f"✗ Record methods failed: {e}")
        return False
    
    # Criterion 3: Phone validation
    from task1 import Phone
    try:
        # Valid 10-digit phone
        phone = Phone("1234567890")
        assert phone.value == "1234567890"
        
        # Invalid phones should raise ValueError
        try:
            Phone("123456789")  # 9 digits
            print("✗ Phone validation failed: should reject 9 digits")
            return False
        except ValueError:
            pass
            
        try:
            Phone("12345678901")  # 11 digits
            print("✗ Phone validation failed: should reject 11 digits")
            return False
        except ValueError:
            pass
            
        try:
            Phone("123abc7890")  # letters
            print("✗ Phone validation failed: should reject letters")
            return False
        except ValueError:
            pass
        
        print("✓ Phone: validation for 10 digits implemented correctly")
    except Exception as e:
        print(f"✗ Phone validation failed: {e}")
        return False
    
    print("\n=== All criteria validated successfully! ===")
    return True


if __name__ == "__main__":
    test_exact_assignment_example()
    validate_criteria()