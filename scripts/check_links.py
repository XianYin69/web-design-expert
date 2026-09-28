"""check_links.py — 悬空链接校验＋知识库确证计数（红线：悬空=0，.md/脚本 ≤50 行）。"""
import os, re, sys
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TAG = re.compile(r"\[(联网|本地)\]")
SKIP = ("tmp", ".git", "__pycache__", ".kilo")

def scan(root):
    bad, over, online, local = [], [], 0, 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            if not f.endswith((".md", ".py")):
                continue
            p = os.path.join(dp, f)
            txt = open(p, encoding="utf-8").read()
            if len(txt.splitlines()) > 50:
                over.append((os.path.relpath(p, root), len(txt.splitlines())))
            if f.endswith(".md"):
                for m in LINK.finditer(txt):
                    t = m.group(1).split("#")[0].strip()
                    if not t or t.startswith(("http:", "https:", "mailto:")):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(dp, t))):
                        bad.append((os.path.relpath(p, root), t))
            for m in TAG.finditer(txt):
                online, local = (online + 1, local) if m.group(1) == "联网" else (online, local + 1)
    return bad, over, online, local

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    root = a[0] if a else "."
    bad, over, online, local = scan(root)
    for p, t in bad:
        print("悬空:", p, "->", t)
    for p, n in over:
        print("超长:", p, "=", n, "行")
    print("悬空链接数 =", len(bad), "| 超长文件数 =", len(over),
          "| [联网] =", online, "| [本地] =", local)
    sys.exit(1 if bad or over else 0)

main()
