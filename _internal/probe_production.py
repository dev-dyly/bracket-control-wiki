"""Read-only verification of production features and served application assets."""
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

import requests

ORIGIN = 'https://app.devdylnz.com'


def get(path):
    response = requests.get(urljoin(ORIGIN, path), timeout=45)
    response.raise_for_status()
    return response


health = get('/api/health').json()
features = get('/api/auth/me').json()['features']
assert health['ok']
assert all(features[name] is True for name in ('tournamentRulesRequired', 'individualParticipation', 'globalPlayerRegistration', 'serverSetupWizard'))
html = get('/app/').text
entry = re.search(r'src="(/app/assets/[^\"]+\.js)"', html).group(1)
scripts = {}
pending = {entry}
while pending:
    with ThreadPoolExecutor(max_workers=6) as pool:
        downloaded = list(pool.map(lambda path: (path, get(path).text), sorted(pending)))
    pending = set()
    for path, text in downloaded:
        scripts[path] = text
        pending.update('/app/assets/' + name for name in re.findall(r'([A-Za-z0-9_-]+-[A-Za-z0-9_-]{8}\.js)', text) if '/app/assets/' + name not in scripts)
    pending.difference_update(scripts)
content = '\n'.join(scripts.values())
labels = ['Only Global Player Registration is required.', 'Not Required', 'Manual Setup', 'Apply Configuration', 'Draft Captain Registry', 'Confirm Selected Captains', 'START CAPTAIN DRAFT', 'Report Game Victory', 'Confirm game result', 'Require Individual Player Acceptance', 'Copy Participation Link', 'Save this tournament', 'Send now to Discord', 'Correct Result', 'Preview series and bracket impact', 'Confirm reviewed correction', 'Transfer Captaincy', 'Retire Team', 'Approve transfer']
for label in labels:
    assert label in content, f'Current production assets do not contain label: {label}'
print('Health:', health)
print('Enabled production features:', features)
print('Entry asset:', entry)
print(f'PASS: {len(scripts)} served JavaScript assets; {len(labels)} current UI labels found. No authenticated or state-changing requests made.')
