from lib.models.category import Category

print("Starting tests...")

# Step 1: Create the table
print("Creating categories table...")
Category.create_table()
print("Table created successfully!")

# Step 2: Add a category
print("Adding a category...")
cat1 = Category(name="Science")
cat1.save()
print(f"Category saved with ID: {cat1.id}")

print("Fetching all categories...")
all_categories = Category.all()
for category in all_categories:
    print(f"ID: {category.id}, Name: {category.name}")

cat2 = Category(name="History")
cat2.save()
print(f"Category saved with ID: {cat2.id}")


