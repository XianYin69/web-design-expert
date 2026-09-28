"""contrast_check.py — WCAG 2.2 相对亮度与对比度实算（标准库，无依赖）。
用法: python contrast_check.py <前景hex> <背景hex> [--large] [--icon]
输出: 比值 + AA/AAA 判定；半透明前景请先合成实际底色再传入。"""
import sys


def rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError("hex 需 3 或 6 位: " + h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    def f(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(v) for v in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = lum(rgb(fg)), lum(rgb(bg))
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r, mode):
    need = {"text": (4.5, 7.0), "large": (3.0, 4.5), "icon": (3.0, 4.5)}[mode]
    return {"ratio": round(r, 2), "mode": mode, "AA": r >= need[0],
            "AAA": r >= need[1], "need_AA": need[0]}


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) < 2:
        raise SystemExit(__doc__)
    m = "icon" if "--icon" in sys.argv else ("large" if "--large" in sys.argv else "text")
    v = verdict(ratio(a[0], a[1]), m)
    print(f"{v['ratio']}:1 AA={'通过' if v['AA'] else '不通过'}(需>={v['need_AA']}) "
          f"AAA={'通过' if v['AAA'] else '不通过'}")
    sys.exit(0 if v["AA"] else 1)
