from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_public_docs_route_exists():
    page = ROOT / 'docs' / 'index.html'
    assert page.is_file()
    text = page.read_text(encoding='utf-8')
    assert 'AICP' in text
    assert '../tools/' in text

def test_main_surface_has_tools_and_docs():
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    assert './tools/' in readme
    assert './docs/' in readme
