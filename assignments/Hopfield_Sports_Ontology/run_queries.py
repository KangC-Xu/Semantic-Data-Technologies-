from pathlib import Path
import json

from rdflib import Graph


base = Path(__file__).resolve().parent
queries = sorted((base / "queries").glob("*.rq"))
if len(queries) != 25:
    raise ValueError(f"Expected 25 query files, found {len(queries)}")

graph = Graph().parse(base / "Hopfield_Sports_Ontology.owl")
output = base / "results"
output.mkdir(exist_ok=True)
counts = {}
for query in queries:
    result = graph.query(query.read_text(encoding="utf-8"))
    counts[query.stem] = len(result)
    (output / f"{query.stem}.csv").write_bytes(result.serialize(format="csv"))
    print(f"{query.stem}: {counts[query.stem]} rows")

(output / "row_counts.json").write_text(
    json.dumps(counts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"Results saved to {output}")
