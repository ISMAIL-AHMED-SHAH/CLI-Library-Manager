import json

# Load library from file (if exists)
try:
    with open("library.txt", "r") as file:
        library = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    library = []  # Empty library if file doesn't exist


def save_library():
    """Save the library to a file."""
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)
    print("\n📁 Library saved successfully!\n")


def add_book():
    """Add a new book to the library."""
    title = input("📖 Enter book title: ").strip()
    author = input("✍️ Enter author: ").strip()
    year = input("📅 Enter publication year: ").strip()
    genre = input("📚 Enter genre: ").strip()
    read_status = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status,
    }
    library.append(book)
    print(f"\n✅ '{title}' by {author} added successfully!\n")
    save_library()


def remove_book():
    """Remove a book from the library."""
    title = input("❌ Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"\n✅ '{title}' removed successfully!\n")
            save_library()
            return
    print(f"\n⚠️ Book '{title}' not found.\n")


def search_books():
    """Search for a book by title or author."""
    print("\n🔍 Search by:\n1️⃣ Title\n2️⃣ Author")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        search_title = input("\n📖 Enter book title: ").strip().lower()
        results = [book for book in library if search_title in book["title"].lower()]
    elif choice == "2":
        search_author = input("\n✍️ Enter author name: ").strip().lower()
        results = [book for book in library if search_author in book["author"].lower()]
    else:
        print("\n⚠️ Invalid choice. Please try again.\n")
        return

    if results:
        print("\n📚 Matching Books:")
        for i, book in enumerate(results, 1):
            read_status = "✅ Read" if book["read"] else "❌ Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("\n⚠️ No matching books found.\n")


def display_books():
    """Display all books in the library."""
    if not library:
        print("\n📚 Your library is empty!\n")
        return

    print("\n📖 Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "✅ Read" if book["read"] else "❌ Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print()


def display_statistics():
    """Display statistics about the library."""
    total_books = len(library)
    if total_books == 0:
        print("\n📊 No books in the library yet.\n")
        return

    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books read: {read_books} ({read_percentage:.1f}%)\n")


def main():
    """Main function to run the library manager."""
    while True:
        print("\n📚 Welcome to Personal Library Manager! 📚")
        print("1️⃣ Add a book")
        print("2️⃣ Remove a book")
        print("3️⃣ Search for a book")
        print("4️⃣ Display all books")
        print("5️⃣ Display statistics")
        print("6️⃣ Exit")

        choice = input("\n🎯 Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("\n👋 Goodbye! Your library has been saved.")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
