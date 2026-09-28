from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = [ROOT / 'index.html', ROOT / 'tools' / 'index.html', ROOT / 'tools' / 'style.css', ROOT / 'tools' / 'app.js', ROOT / 'docs' / 'index.html']

def test_public_runtime_boundary():
    forbidden = ('tokenrouter', '/home/ubuntu', 'api_key', 'AICP_REDIS_URL')
    failures = []
    for path in PUBLIC_FILES:
        text = path.read_text(encoding='utf-8').lower()
        for marker in forbidden:
            if marker.lower() in text:
                failures.append(f'{path.relative_to(ROOT)} matches {marker}')
    assert not failures, '\\n'.join(failures)
