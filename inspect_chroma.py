from src.vector_store import collection

results = collection.get()

print("Total Docs:")
print(len(results["documents"]))

for i in range(10):

    print("\n")
    print("=" * 80)

    print("ID:")
    print(results["ids"][i])

    print("\nDocument Length:")

    if results["documents"][i]:
        print(len(results["documents"][i]))
    else:
        print("EMPTY")

    print("\nPreview:")

    print(results["documents"][i][:200] if results["documents"][i] else "EMPTY")