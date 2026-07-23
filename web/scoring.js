// OJTS 2.1 确定性计分 —— scripts/score.py 的 JavaScript 等价实现。
// 任何修改必须与 Python 版保持一致（tests/test_web_parity.py 逐分对照）。
// 同时支持浏览器（window.OJTS_SCORING）与 Node（module.exports）两种加载方式。
(function (global) {
  "use strict";

  var LETTERS = "EISNTFJP";
  var AXES = [["E", "I"], ["S", "N"], ["T", "F"], ["J", "P"]];

  // 与 Python round(x, 4) 一致的四舍六入五成双
  function round4(x) {
    var v = x * 10000;
    var floor = Math.floor(v);
    var diff = v - floor;
    var n;
    if (diff > 0.5) n = floor + 1;
    else if (diff < 0.5) n = floor;
    else n = floor % 2 === 0 ? floor : floor + 1;
    return n / 10000;
  }

  function scoreAnswers(items, answers) {
    if (!Array.isArray(answers) || answers.length !== 48) {
      throw new Error("需要 48 个答案");
    }
    var scores = {};
    for (var i = 0; i < LETTERS.length; i++) scores[LETTERS[i]] = 0;
    for (var j = 0; j < items.length; j++) {
      var item = items[j];
      var answer = answers[j];
      if (!Number.isInteger(answer) || answer < 1 || answer > 5) {
        throw new Error(item.id + " 的答案必须是 1 到 5 的整数");
      }
      if (item.kind === "likert") {
        for (var k = 0; k < item.keys.length; k++) scores[item.keys[k]] += answer - 1;
      } else if (item.kind === "bipolar") {
        scores[item.left_key] += 5 - answer;
        scores[item.right_key] += answer - 1;
      } else {
        throw new Error("未知题型：" + item.kind);
      }
    }
    return scores;
  }

  function summarizeScores(scores) {
    var rawLetters = [];
    var axes = [];
    var boundaryAxes = [];
    for (var i = 0; i < AXES.length; i++) {
      var left = AXES[i][0], right = AXES[i][1];
      var leftScore = scores[left], rightScore = scores[right];
      var total = leftScore + rightScore;
      var chosen;
      if (leftScore === rightScore) {
        chosen = "X";
        boundaryAxes.push(left + "/" + right);
      } else {
        chosen = leftScore > rightScore ? left : right;
      }
      rawLetters.push(chosen);
      axes.push({
        axis: left + "/" + right,
        left: leftScore,
        right: rightScore,
        left_ratio: round4(leftScore / total),
        right_ratio: round4(rightScore / total),
        difference: Math.abs(leftScore - rightScore),
        chosen: chosen,
      });
    }
    var rawType = rawLetters.join("");
    var candidates = [""];
    for (var p = 0; p < AXES.length; p++) {
      var next = [];
      for (var q = 0; q < candidates.length; q++) {
        if (rawLetters[p] === "X") {
          next.push(candidates[q] + AXES[p][0]);
          next.push(candidates[q] + AXES[p][1]);
        } else {
          next.push(candidates[q] + rawLetters[p]);
        }
      }
      candidates = next;
    }
    var nonBoundary = axes.filter(function (a) { return a.chosen !== "X"; });
    var secondCandidates = [];
    if (boundaryAxes.length === 0 && nonBoundary.length > 0) {
      var weakest = Math.min.apply(null, nonBoundary.map(function (a) { return a.difference; }));
      for (var m = 0; m < nonBoundary.length; m++) {
        var axis = nonBoundary[m];
        if (axis.difference === weakest) {
          var parts = axis.axis.split("/");
          var flip = axis.chosen === parts[0] ? parts[1] : parts[0];
          var pos = ["E/I", "S/N", "T/F", "J/P"].indexOf(axis.axis);
          var flipped = rawType.slice(0, pos) + flip + rawType.slice(pos + 1);
          if (secondCandidates.indexOf(flipped) === -1) secondCandidates.push(flipped);
        }
      }
      secondCandidates.sort();
    }
    return {
      scores: scores,
      axes: axes,
      raw_type: rawType,
      boundary_axes: boundaryAxes,
      candidates: candidates,
      second_candidates: secondCandidates,
    };
  }

  var api = { scoreAnswers: scoreAnswers, summarizeScores: summarizeScores };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  global.OJTS_SCORING = api;
})(typeof window !== "undefined" ? window : globalThis);
