"""a11y_probe.py — 静态扫 HTML/CSS 的设计与无障碍异味（标准库，只读不改盘）。
用法: python a11y_probe.py <文件或目录>
输出: 每条命中 = 严重度 | 规则 | 位置 | 片段（每规则最多 3 条）。判定仍需人工实测复核。"""
import os, re, sys

RULES = [
    ("P0", "outline-none-no-replacement", r"outline\s*:\s*(none|0)\b"),
    ("P0", "img-missing-alt", r"<img\b(?![^>]*\balt=)[^>]*>"),
    ("P0", "positive-tabindex", r"tabindex\s*=\s*[\"'][1-9]"),
    ("P1", "div-onclick-no-role", r"<(div|span|p)\b[^>]*\bon(click|keydown)="),
    ("P1", "placeholder-as-label", r"<input\b[^>]*placeholder=(?![^>]*(id=|aria-label))"),
    ("P1", "fixed-px-width", r"width\s*:\s*[3-9]\d\dpx"),
    ("P1", "autoplay-carousel", r"(autoplay|setInterval)[^;\n]{0,40}(carousel|slide)"),
    ("P2", "aria-hidden-focusable", r"aria-hidden=[\"']true[\"'][^>]*tabindex=[\"']0"),
    ("P2", "layout-thrash-anim", r"transition[^;\n]*(height|width|top|left|margin)"),
    ("P2", "important-spam", r"!important"),
    ("P3", "magic-spacing", r"(margin|padding|gap)\s*:\s*\d*[13579]px"),
]


def files(p):
    return [p] if os.path.isfile(p) else [
        os.path.join(d, f) for d, _, fs in os.walk(p) for f in fs
        if f.endswith((".html", ".htm", ".css", ".jsx", ".tsx", ".vue"))]


def scan(paths):
    hits = []
    for f in paths:
        t = open(f, encoding="utf-8", errors="replace").read()
        if "<html" in t.lower() and "viewport" not in t.lower():
            hits.append(("P1", "missing-viewport-meta", f + ":1", "<head>"))
        for sev, rule, pat in RULES:
            for m in list(re.finditer(pat, t, re.I | re.M))[:3]:
                ln = t[:m.start()].count("\n") + 1
                hits.append((sev, rule, f"{f}:{ln}", m.group(0)[:60].replace("\n", " ")))
    return sorted(hits)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    rs = {}
    for sev, rule, loc, snip in scan(files(sys.argv[1])):
        rs[sev] = rs.get(sev, 0) + 1
        print(f"{sev} | {rule} | {loc} | {snip}")
    print("[汇总] " + " ".join(f"{k}={rs.get(k, 0)}" for k in ("P0", "P1", "P2", "P3")))
