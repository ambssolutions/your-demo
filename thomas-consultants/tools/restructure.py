"""Move each concept home from designs/NN-slug.html to designs/NN-slug/index.html,
rewrite links, and add the shared concept switcher to every page. Idempotent."""
import re, sys, pathlib
D = pathlib.Path(__file__).resolve().parent.parent / "designs"
SWITCH = '<script src="../../assets/concepts.js" defer></script>'

def fix_home(s, slug):
    s = re.sub(r'(["\'`(])\.\./', r'\1../../', s)                 # parent refs move one level deeper
    s = re.sub(r'(["\'`])' + re.escape(slug) + r'/', r'\1', s)    # slug/services.html -> services.html
    s = re.sub(r'(["\'`])' + re.escape(slug) + r'\.html', r'\1index.html', s)
    return s

def fix_inner(s, slug):
    return re.sub(r'(["\'`])\.\./' + re.escape(slug) + r'\.html', r'\1index.html', s)

def finish(s, slug):
    if 'data-concept=' not in s:
        s = re.sub(r'<html\b', f'<html data-concept="{slug}"', s, count=1)
    if 'assets/concepts.js' not in s:
        s = re.sub(r'</body>', SWITCH + '\n</body>', s, count=1, flags=re.I)
    return s

for slug in sys.argv[1:]:
    home, folder = D / f"{slug}.html", D / slug
    folder.mkdir(exist_ok=True)
    if home.exists():
        redirect = folder / "index.html"
        if redirect.exists() and redirect.stat().st_size < 2000:
            redirect.unlink()
        (folder / "index.html").write_text(fix_home(home.read_text(), slug))
        home.unlink()
    for p in folder.glob("*.html"):
        s = p.read_text()
        if p.name != "index.html":
            s = fix_inner(s, slug)
        p.write_text(finish(s, slug))
    print("ok", slug, sorted(x.name for x in folder.glob("*.html")))
