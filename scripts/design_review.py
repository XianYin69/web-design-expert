"""design_review.py — 把评审发现（JSON 数组）按优先级约束排序、归并并渲染报告。
用法: python design_review.py findings.json [--max 12] [--out report.md]
输入项字段: severity(P0-P3), dimension, symptom, evidence, basis, action, spec, accept, cost
输出: 排序后的 Markdown 清单；P2/P3 超量时折叠为「品质批次」一条。"""
import json, sys, collections

ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def fold(items, mx):
    keep = [i for i in items if i["severity"] in ("P0", "P1")]
    rest = [i for i in items if i["severity"] not in ("P0", "P1")]
    if len(items) > mx and rest:
        g = collections.Counter(i["dimension"] for i in rest)
        keep.append({"severity": "P2", "dimension": "品质批次",
                     "symptom": "；".join(f"{k}×{v}" for k, v in g.items()),
                     "evidence": "合并展示", "basis": "优先级约束",
                     "action": "按令牌阶梯与状态矩阵统一整改", "spec": "见 knowledge/设计令牌与暗色模式",
                     "accept": "非阶梯值与硬编码色值为 0", "cost": "M"})
        return keep
    return items


def render(items):
    L = ["| 级 | 维度 | 现象与证据 | 依据 | 动作与规格 | 验收 | 成本 |", "|---|---|---|---|---|---|---|"]
    for i in items:
        L.append(f"| {i.get('severity','?')} | {i.get('dimension','')} | {i.get('symptom','')} "
                 f"（{i.get('evidence','')}） | {i.get('basis','')} | {i.get('action','')} "
                 f"{i.get('spec','')} | {i.get('accept','')} | {i.get('cost','')} |")
    c = collections.Counter(i.get("severity", "?") for i in items)
    verdict = "不通过" if c.get("P0") else ("部分通过" if c.get("P1") else "通过")
    L.append(f"\n[统计] " + " ".join(f"{k}={v}" for k, v in sorted(c.items(), key=lambda x: ORDER.get(x[0], 9))))
    L.append(f"[判定] 存在未清 P0/P1 前不得放行 → 当前：{verdict}")
    return "\n".join(L)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 12
    data = json.load(open(a[0], encoding="utf-8"))
    data.sort(key=lambda i: ORDER.get(i.get("severity", "P3"), 9))
    out = render(fold(data, mx))
    if "--out" in sys.argv:
        open(sys.argv[sys.argv.index("--out") + 1], "w", encoding="utf-8").write(out + "\n")
    print(out)
