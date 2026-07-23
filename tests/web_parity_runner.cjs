// 供 tests/test_web_parity.py 调用：从 stdin 之外接收向量文件路径，输出 JSON 结果。
const fs = require("fs");
const path = require("path");

const scoring = require(path.join(__dirname, "..", "web", "scoring.js"));
const bank = JSON.parse(
  fs.readFileSync(path.join(__dirname, "..", "references", "questions.json"), "utf8")
);
const vectors = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out = vectors.map((v) => scoring.summarizeScores(scoring.scoreAnswers(bank.items, v)));
process.stdout.write(JSON.stringify(out));
