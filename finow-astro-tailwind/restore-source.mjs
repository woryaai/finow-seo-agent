import { gunzipSync } from "node:zlib";
import { mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { dirname } from "node:path";

const dir = new URL("./source-payload/", import.meta.url);
const payload = readdirSync(dir)
  .filter((n) => n.endsWith(".txt"))
  .sort()
  .map((n) => readFileSync(new URL(n, dir), "utf8").trim())
  .join("");

const files = JSON.parse(
  gunzipSync(Buffer.from(payload, "base64")).toString("utf8")
);

for (const file of files) {
  mkdirSync(dirname(file.path), { recursive: true });
  writeFileSync(file.path, file.content, "utf8");
}

console.log(`Restored ${files.length} source text files.`);
