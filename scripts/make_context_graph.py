#!/usr/bin/env python3
"""Draw assets/context-graph.svg, the small Obsidian-style graph in the README's
"Use it as project context" section.

It is a picture of the idea, not an index: the N most-linked entries and the
links between them, laid out with a simple force-directed pass. It does not need
to track the corpus exactly, so it is NOT part of `build.py write`; re-run it by
hand when the picture looks stale.

Drawn on its own dark panel, like the banner, so it reads the same whether the
viewer's GitHub theme and operating-system theme agree or not.

    python3 scripts/make_context_graph.py [N]      # default N = 14
"""
import math
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
OUT = ROOT / "assets" / "context-graph.svg"
LINK = re.compile(r"\]\(([a-z0-9-]+)\.md")

W, H = 440, 270                     # drawing size
PADX, PADY = 72, 26                 # inner margin; wide sideways so centered labels fit
CHAR, LINE_H = 4.7, 10              # rough label width per character, label height
PANEL, EDGE, NODE, HUB, LABEL = "#0d1117", "#3d3a5c", "#8b5cf6", "#c4b5fd", "#c9d1d9"


def links():
    """slug -> set of slugs it links to (entries only, no self-links)."""
    slugs = {p.stem for p in CONCEPTS.glob("*.md")}
    out = {}
    for p in CONCEPTS.glob("*.md"):
        targets = set(LINK.findall(p.read_text(encoding="utf-8"))) & slugs
        out[p.stem] = targets - {p.stem}
    return out


def pick(graph, n):
    inbound = {s: 0 for s in graph}
    for targets in graph.values():
        for t in targets:
            inbound[t] += 1
    return sorted(inbound, key=lambda s: (-inbound[s], s))[:n]


def layout(nodes, edges, seed, steps=400):
    """Fruchterman-Reingold, seeded so the picture is the same on every run."""
    rnd = random.Random(seed)
    pos = {v: [rnd.uniform(-1, 1), rnd.uniform(-1, 1)] for v in nodes}
    k = math.sqrt(4.0 / len(nodes))
    for step in range(steps):
        disp = {v: [0.0, 0.0] for v in nodes}
        for a in nodes:
            for b in nodes:
                if a == b:
                    continue
                dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
                d = max(math.hypot(dx, dy), 0.01)
                f = k * k / d
                disp[a][0] += dx / d * f
                disp[a][1] += dy / d * f
        for a, b in edges:
            dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
            d = max(math.hypot(dx, dy), 0.01)
            f = d * d / k
            for v, s in ((a, -1), (b, 1)):
                disp[v][0] += s * dx / d * f
                disp[v][1] += s * dy / d * f
        temp = 0.1 * (1 - step / steps) + 0.005
        for v in nodes:
            dx, dy = disp[v]
            d = max(math.hypot(dx, dy), 0.01)
            pos[v][0] += dx / d * min(d, temp)
            pos[v][1] += dy / d * min(d, temp)
    xs, ys = [p[0] for p in pos.values()], [p[1] for p in pos.values()]
    sx = (W - 2 * PADX) / ((max(xs) - min(xs)) or 1)
    sy = (H - 2 * PADY - LINE_H) / ((max(ys) - min(ys)) or 1)
    return {v: (PADX + (p[0] - min(xs)) * sx, PADY + (p[1] - min(ys)) * sy) for v, p in pos.items()}


def label_box(v, x, y, r):
    w = CHAR * len(v)
    return (x - w / 2, y + r + 1, x + w / 2, y + r + 1 + LINE_H)


def clashes(nodes, edges, pos):
    """Count label/label and label/dot overlaps, and labels leaving the panel."""
    deg = degrees(nodes, edges)
    top = max(deg.values())
    rad = {v: 2.5 + 4.5 * deg[v] / top for v in nodes}
    boxes = {v: label_box(v, *pos[v], rad[v]) for v in nodes}
    bad = 0
    for i, a in enumerate(nodes):
        x0, y0, x1, y1 = boxes[a]
        if x0 < 8 or x1 > W - 8 or y1 > H - 6:
            bad += 1
        for b in nodes[i + 1:]:
            u0, v0, u1, v1 = boxes[b]
            if x0 < u1 and u0 < x1 and y0 < v1 and v0 < y1:
                bad += 1
        for b in nodes:
            if b != a:
                cx, cy = pos[b]
                if x0 - rad[b] < cx < x1 + rad[b] and y0 - rad[b] < cy < y1 + rad[b]:
                    bad += 1
    return bad


def degrees(nodes, edges):
    deg = {v: 0 for v in nodes}
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return deg


def svg(nodes, edges, pos):
    degree = degrees(nodes, edges)
    top = max(degree.values())
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" role="img" aria-labelledby="t d">',
           '  <title id="t">Concept graph</title>',
           '  <desc id="d">An Obsidian-style graph of the wiki\'s most-linked entries and the links between them, '
           'on its own dark panel so it reads the same under any light or dark setting.</desc>',
           f'  <rect width="{W}" height="{H}" rx="16" fill="{PANEL}"/>',
           f'  <g stroke="{EDGE}" stroke-width="0.8">']
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        out.append(f'    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    out.append("  </g>")
    out.append(f'  <g font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="8.5" fill="{LABEL}" text-anchor="middle">')
    for v in nodes:
        x, y = pos[v]
        r = 2.5 + 4.5 * degree[v] / top
        fill = HUB if degree[v] == top else NODE
        out.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}"/>')
        out.append(f'    <text x="{x:.1f}" y="{y + r + 9:.1f}">{v}</text>')
    out.append("  </g>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    graph = links()
    nodes = pick(graph, n)
    edges = sorted({tuple(sorted((a, b))) for a in nodes for b in graph[a] if b in nodes})
    # Try seeds until no label collides or leaves the panel; the first clean seed wins,
    # so the result is the same on every run for the same corpus.
    best = min(range(1, 400), key=lambda s: (clashes(nodes, edges, layout(nodes, edges, s)), s))
    pos = layout(nodes, edges, best)
    left = clashes(nodes, edges, pos)
    OUT.write_text(svg(nodes, edges, pos), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(nodes)} entries, {len(edges)} links, seed {best}, "
          f"{left} label clash{'es' if left != 1 else ''})")


if __name__ == "__main__":
    main()
