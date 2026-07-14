from src.retriever import retrieve

query = "PTO accrual days"

results = retrieve(query)

print("\nRESULT KEYS:")
print(results.keys())

print("\nNUMBER OF RESULTS:")
print(len(results["documents"][0]))

for i in range(len(results["documents"][0])):

    print("\n" + "=" * 100)

    print(f"RESULT #{i+1}")

    print("=" * 100)

    # Source
    source = results["metadatas"][0][i].get(
        "source",
        "Unknown Source"
    )

    category = results["metadatas"][0][i].get(
        "category",
        "Unknown Category"
    )

    print(f"Source: {source}")
    print(f"Category: {category}")

    # Distance / Score
    if "distances" in results:
        print(
            f"Distance: {results['distances'][0][i]}"
        )

    print("-" * 100)

    # Document text
    document = results["documents"][0][i]

    if document:
        print(document[:1000])
    else:
        print("⚠️ EMPTY DOCUMENT RETURNED")

    print("\n")